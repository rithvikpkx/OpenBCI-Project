eeg_file = open("/Users/rithvikpraveenkumar/OpenBCI Project/LRN_Image/EEGData.txt", "r")
lr_file = open("/Users/rithvikpraveenkumar/OpenBCI Project/LRN_Image/LRNImageData.txt", "r")
labeledData = open("/Users/rithvikpraveenkumar/OpenBCI Project/LRN_Image/LabeledData.txt", "w")

lrlines = lr_file.readlines()
eeglines = eeg_file.readlines()

for index in range(1, len(lrlines)):
    
    lowerTimestamp = float(lrlines[index - 1].split("  ------->  ")[1])
    upperTimestamp = float(lrlines[index].split("  ------->  ")[1])


    if(int(lrlines[index - 1].split("  ------->  ")[2]) == 0):
        currentAction = "Left"
    elif(int(lrlines[index - 1].split("  ------->  ")[2]) == 1):
        currentAction = "None"
    else:
        currentAction = "Right"
        
    for eegline in range(5, len(eeglines)):
        eeglineArray = eeglines[eegline].split(", ")
        eegTimestamp = float(eeglineArray[-3])
        if eegTimestamp >= lowerTimestamp:
            if eegTimestamp < upperTimestamp:
                print(lowerTimestamp, eegTimestamp, upperTimestamp)
                labeledData.write(str((currentAction, str(lowerTimestamp), str(eegTimestamp), str(upperTimestamp), str(eeglineArray[1:16]))) + "\n")



