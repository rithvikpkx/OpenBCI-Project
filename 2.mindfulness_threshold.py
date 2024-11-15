# This is going to print a constant flow of mindfulness metrics to calibrate my program

from brainflow.board_shim import BoardShim, BrainFlowInputParams
from brainflow.data_filter import DataFilter
from brainflow.ml_model import MLModel, BrainFlowMetrics, BrainFlowClassifiers, BrainFlowModelParams
import time

params = BrainFlowInputParams()
params.serial_port = "/dev/cu.usbserial-DP04WFZS"
BOARD_ID = 2 

board = BoardShim(BOARD_ID, params)
sampling_rate = BoardShim.get_sampling_rate(BOARD_ID)
BoardShim.disable_board_logger()
channels = board.get_eeg_channels(BOARD_ID)

board.prepare_session()
board.start_stream()

def get_data():
    time.sleep(5)
    data = board.get_board_data()

    return data

mindfulness_params = BrainFlowModelParams(BrainFlowMetrics.MINDFULNESS.value,
                                                BrainFlowClassifiers.DEFAULT_CLASSIFIER.value)
mindfulness = MLModel(mindfulness_params)
mindfulness.prepare()

while True:
    bands = DataFilter.get_avg_band_powers(get_data(), channels, sampling_rate, True)
    # print("band for band")
    #print(bands)
    feature_vector = bands[0]
    # print('feature vector')
    # print(feature_vector)

    mindfulness_level = mindfulness.predict(feature_vector)
    print('Mindfulness: ' + str(mindfulness_level))
