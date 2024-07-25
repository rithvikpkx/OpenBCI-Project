# This program move a robotic hand based on blink data from the wearer's head

import time
import serial

from brainflow.board_shim import BoardShim, BrainFlowInputParams
from brainflow.data_filter import DataFilter
from brainflow.ml_model import MLModel, BrainFlowMetrics, BrainFlowClassifiers, BrainFlowModelParams

BoardShim.disable_board_logger()

params = BrainFlowInputParams()
params.serial_port = "/dev/cu.usbserial-DP04WFZS"
BOARD_ID = 2

board = BoardShim(BOARD_ID, params)
