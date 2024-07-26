from PIL import Image, ImageTk
import tkinter as tk
import random
import datetime
import time


# List of image file paths
image_files = ["/Users/rithvikpraveenkumar/OpenBCI Project/LRN Image/Left Arrow Drawing.jpg", "/Users/rithvikpraveenkumar/OpenBCI Project/LRN Image/None drawing.jpg", "/Users/rithvikpraveenkumar/OpenBCI Project/LRN Image/Right Arrow Drawing.jpg"]
timings = {}

file = open("/Users/rithvikpraveenkumar/OpenBCI Project/LRN Image/dataLog.txt", "a")

# Function to display a random image
def display_random_image():
    random_image = random.choice(image_files)
    # 0 --> left
    # 1 --> none
    # 2 --> right
    # timings[]
    img = Image.open(random_image)
    # img = img.resize((1200, 1200))  # Resize if needed
    img_tk = ImageTk.PhotoImage(img)
    label.config(image=img_tk)
    label.image = img_tk

    ct = str(datetime.datetime.now())
    ts = str(time.time())
    # rounded_timestamp = ct[:-3]
    write_msg = ct + "  ------->  " + ts + "  ------->  " + str(image_files.index(random_image)) + "\n"
    file.write(write_msg)
    print(str(ct) + "  ------->  " + str(ts) + "  ------->  " + str(image_files.index(random_image)))

    # Schedule next image display after a random interval
    random_interval = random.randint(2, 4)  # Change interval range as needed
    root.after(random_interval * 1000, display_random_image)

# Create a Tkinter window
root = tk.Tk()
root.title("Random Image Display")

# Create a label widget to display the images
label = tk.Label(root)
label.pack()

# Start displaying images
display_random_image()

# Run the Tkinter event loop
root.mainloop()