import importlib
import os
processing = importlib.import_module("processing")
#import processing.py

img = processing.PlaneProcessing("aeroclasses")
#img.findHCD(filename="hi.mock")
#img.drawImage()

directory = os.getcwd()
img.generateBulk(0, str(directory) + "/../Dataset/aircraft-0")
img.generateBulk(1, str(directory) + "/../Dataset/aircraft-1")
img.generateBulk(2, str(directory) + "/../Dataset/aircraft-2")
img.generateBulk(3, str(directory) + "/../Dataset/aircraft-3")
img.generateBulk(4, str(directory) + "/../Dataset/aircraft-4")
img.generateBulk(5, str(directory) + "/../Dataset/aircraft-5")
