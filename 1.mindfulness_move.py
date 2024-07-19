# This code works to move a robotic hand based on mindfulness

import time
import serial

from brainflow.board_shim import BoardShim, BrainFlowInputParams
from brainflow.data_filter import DataFilter
from brainflow.ml_model import MLModel, BrainFlowMetrics, BrainFlowClassifiers, BrainFlowModelParams

BoardShim.disable_board_logger()

params = BrainFlowInputParams()
params.serial_port = "/dev/cu.usbserial-DP04WFZS" # serial port of the BrainWave Bluetooth Usb dongle
BOARD_ID = 2 # 2 corresponds to Cyton-Daisy Board

board = BoardShim(BOARD_ID, params)
sampling_rate = BoardShim.get_sampling_rate(BOARD_ID)
eeg_channels = BoardShim.get_eeg_channels(BOARD_ID)

mindfulness_params = BrainFlowModelParams(BrainFlowMetrics.MINDFULNESS.value, BrainFlowClassifiers.DEFAULT_CLASSIFIER.value)
mindfulness = MLModel(mindfulness_params)

ser = serial.Serial('/dev/cu.usbmodem101', 9600)


def get_data():
    board.prepare_session()
    board.start_stream()
    time.sleep(4)  # recommended window size for eeg metric calculation is at least 4 seconds, bigger is better
    data = board.get_board_data()
    board.stop_stream()
    board.release_session()

    return data


def get_mindfulness_level():
    mindfulness.prepare()
    mindfulness_level = mindfulness.predict(feature_vector)
    mindfulness.release()

    return mindfulness_level


while True:
    bands = DataFilter.get_avg_band_powers(get_data(), eeg_channels, sampling_rate, True)
    # print("band for band")
    # print(bands)
    feature_vector = bands[0]
    # print(feature_vector)

    mindfulness_level = str(get_mindfulness_level())

    print('Mindfulness: ' + mindfulness_level)

    # print("Establishing connection with hand...")


    MINDFULNESS_THRESHOLD = 0.20
    if mindfulness_level > MINDFULNESS_THRESHOLD:
        time.sleep(3)
        ser.write(str(99).encode())
        
    time.sleep(7)
        
