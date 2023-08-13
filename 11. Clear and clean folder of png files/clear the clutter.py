# This program will organize all the png files in the folder

import os

files = os.listdir("D:/My Github repositories/-python-projects-collection/1. Python Starter Projects/Clear and Clean Folder of png files/clutteredfolder")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
    os.rename(f"D:/My Github repositories/-python-projects-collection/1. Python Starter Projects/Clear and Clean Folder of png files/clutteredfolder/{file}", f"D:/My Github repositories/-python-projects-collection/1. Python Starter Projects/Clear and Clean Folder of png files/clutteredfolder/{i}.png")
    i += 1
