# This program will print all the data on the board repeatedly


#brainflow python library download required
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
import time

#initialized and populated BrainFlowInputParams() object with serial-port for mac
parameters = BrainFlowInputParams()
parameters.serial_port = "/dev/cu.usbserial-DP04WFZS"

#board-id 2 corresponds to cyton-daisy board
board_id = 2

board = BoardShim(board_id, parameters)
board.prepare_session()
board.start_stream()
time.sleep(10)
data = board.get_board_data()
board.stop_stream()
board.release_session()

print(data)