import importlib
import os
processing = importlib.import_module("processing")
#import processing.py

img = processing.PlaneProcessing()
#img.findHCD(filename="hi.mock")
#img.drawImage()

directory = os.getcwd()
img.generateBulk(0, str(directory) + "/../Dataset/aircraft-0", "sla0")
img.generateBulk(1, str(directory) + "/../Dataset/aircraft-1", "sla1")
img.generateBulk(2, str(directory) + "/../Dataset/aircraft-2", "sla2")
img.generateBulk(3, str(directory) + "/../Dataset/aircraft-3", "sla3")
img.generateBulk(4, str(directory) + "/../Dataset/aircraft-4", "sla4")
img.generateBulk(5, str(directory) + "/../Dataset/aircraft-5", "sla5")
