# This code works to move a robotic hand based on mindfulness

import time
import serial

from brainflow.board_shim import BoardShim, BrainFlowInputParams
from brainflow.data_filter import DataFilter
from brainflow.ml_model import MLModel, BrainFlowMetrics, BrainFlowClassifiers, BrainFlowModelParams


params = BrainFlowInputParams()
params.serial_port = "/dev/cu.usbserial-DP04WFZS" # serial port of the BrainWave Bluetooth Usb dongle
BOARD_ID = 2 # 2 corresponds to Cyton-Daisy Board

while True:
    board = BoardShim(BOARD_ID, params)
    sampling_rate = BoardShim.get_sampling_rate(BOARD_ID)
    board.prepare_session()
    board.start_stream()
    time.sleep(4)  # recommended window size for eeg metric calculation is at least 4 seconds, bigger is better
    data = board.get_board_data()
    board.stop_stream()
    board.release_session()

    print('hehe')

    eeg_channels = BoardShim.get_eeg_channels(BOARD_ID)
    bands = DataFilter.get_avg_band_powers(data, eeg_channels, sampling_rate, True)
    print("band for band")
    print(bands)
    feature_vector = bands[0]
    # print(feature_vector)

    mindfulness_params = BrainFlowModelParams(BrainFlowMetrics.MINDFULNESS.value,
                                                BrainFlowClassifiers.DEFAULT_CLASSIFIER.value)
    mindfulness = MLModel(mindfulness_params)
    mindfulness.prepare()
    mindfulness_level = mindfulness.predict(feature_vector)
    mindfulness.release()
    print('Mindfulness: %s' % str(mindfulness_level))

    print("Establishing connection with hand...")
    ser = serial.Serial('/dev/cu.usbmodem101', 9600)


    MINDFULNESS_THRESHOLD = 0.20
    if mindfulness_level > MINDFULNESS_THRESHOLD:
        time.sleep(3)
        ser.write(str(99).encode())
        
    time.sleep(5)
        
