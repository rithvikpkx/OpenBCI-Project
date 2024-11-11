# eeg_file = open("/Users/rithvikpraveenkumar/Documents/OpenBCI_GUI/Recordings/OpenBCISession_2024-07-25_22-30-57/OpenBCI-RAW-2024-07-25_22-31-22.txt", "r+")
# /Users/rithvikpraveenkumar/OpenBCI Project/LRN Image/
eeg_file = open("/Users/rithvikpraveenkumar/OpenBCI Project/LRN Image/EEGData.txt", "r")
# lr_file = open("/Users/rithvikpraveenkumar/OpenBCI Project/LRN Image/dataLog.txt", "r+")
lr_file = open("/Users/rithvikpraveenkumar/OpenBCI Project/LRN Image/LRNImageData.txt", "r")

labeledData = open("/Users/rithvikpraveenkumar/OpenBCI Project/LRN Image/LabeledData.txt", "w")

lrlines = lr_file.readlines()
eeglines = eeg_file.readlines()

# eeglines = templines[5:]

# dict = {"Left" : [], "None" : [], "Right" : []} # Dictionary to store all eeg data corresponding to action



for index in range(1, len(lrlines)):
    
    lowerTimestamp = float(lrlines[index - 1].split("  ------->  ")[1])
    upperTimestamp = float(lrlines[index].split("  ------->  ")[1])

    # print("bluh", int(lrlines[index - 1].split("  ------->  ")[2]))

    if(int(lrlines[index - 1].split("  ------->  ")[2]) == 0):
        currentAction = "Left"
    elif(int(lrlines[index - 1].split("  ------->  ")[2]) == 1):
        currentAction = "None"
    else:
        currentAction = "Right"
        
    for eegline in range(5, len(eeglines)):
        eeglineArray = eeglines[eegline].split(", ")
        eegTimestamp = float(eeglineArray[-3])
        # eegchar = str(eeglineArray[0])
        # timeStamp = str(eeglineArray[-1])
        if eegTimestamp >= lowerTimestamp:
            if eegTimestamp < upperTimestamp:
                print(lowerTimestamp, eegTimestamp, upperTimestamp)
                # dict[currentAction].append(str(eegline) + " ***** " + str(eegTimestamp))
                labeledData.write(str((currentAction, str(lowerTimestamp), str(eegTimestamp), str(upperTimestamp), str(eeglineArray[1:16]))) + "\n")



# print(dict.items())





# eegline = eeglines[5].split(", ")


# print(lrline1[1], lrline1[2])
# print(lrline2[1], lrline2[2])
# print(float(eegline[-3]))

# eegts = None
# lower = None
# upper = None

# lrline1 = lrlines[0].split("  ------->  ")
# lrline2 = lrlines[1].split("  ------->  ")

# lower = float(lrline1[1])
# upper = float(lrline2[1])

# counter = 1
# for line in eeglines:
#     eegts = float(line.split(", ")[-3])

#     if (eegts >= lower) and (eegts < upper):
#         # print(eegts)
#         print("mid")
#         print(eegts, lower, upper, counter)
#         # dict["Left"].append(line)
#     elif eegts < lower:
#         print('lower')
#         pass
#     elif eegts >= upper:
#         print('more')
#         lower = float(lrlines[counter].split("  ------->  ")[1])

#         if counter == len(lrlines):
#             counter = len(lrlines) - 1
#             print("bluhh")
#         else:
#             counter += 1

#         upper = float(lrlines[counter].split("  ------->  ")[1])

#         print(eegts, lower, upper, counter)