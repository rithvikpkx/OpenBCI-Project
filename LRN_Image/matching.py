"""

This program is meant to match and merge the EEG signals and the corresponding direction (L, R, N).
It generates an output file with the matched EEG signals, the respective direction, and the timestamps used to match them.

"""


# open/access necessary files
# --------------------
eeg_file = open("/Users/rithvikpraveenkumar/OpenBCI Project/LRN_Image/EEGData.txt", "r") # File with EEG signals and timestamps
lr_file = open("/Users/rithvikpraveenkumar/OpenBCI Project/LRN_Image/LRNImageData.txt", "r") # File with Left, Right, or None and timestamps
labeledData = open("/Users/rithvikpraveenkumar/OpenBCI Project/LRN_Image/LabeledData.txt", "w") # Final output file (starts off blank and gets written to in the end)

# Read the files
lrlines = lr_file.readlines()
eeglines = eeg_file.readlines()
# --------------------

# Loops through all the lines of the lr_file
for index in range(1, len(lrlines)):
    
    # Establishes timestamp range to look within
    lowerTimestamp = float(lrlines[index - 1].split("  ------->  ")[1])
    upperTimestamp = float(lrlines[index].split("  ------->  ")[1])

    # Establishes which action to match to within the timestamp range
    if(int(lrlines[index - 1].split("  ------->  ")[2]) == 0):
        currentAction = "Left"
    elif(int(lrlines[index - 1].split("  ------->  ")[2]) == 1):
        currentAction = "None"
    else:
        currentAction = "Right"

    # Loops through every relevant line of the eeg_file    
    for eegline in range(5, len(eeglines)):
        eeglineArray = eeglines[eegline].split(", ")
        eegTimestamp = float(eeglineArray[-3])

        # Checks whether currect timestamp is within the desired timestamp range
        if (eegTimestamp >= lowerTimestamp) and (eegTimestamp < upperTimestamp):
                # Writes the appropriate eeg, timestamp, and direction data to the output file if timestamp is within the range
                labeledData.write(str((currentAction, str(lowerTimestamp), str(eegTimestamp), str(upperTimestamp), str(eeglineArray[1:16]))) + "\n")