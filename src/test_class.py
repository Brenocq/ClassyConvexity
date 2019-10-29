import importlib
import os
processing = importlib.import_module("processing")
#import processing.py

img = processing.PlaneProcessing("aeroclasses")
#img.findHCD(filename="hi.mock")
#img.drawImage()

img.generateBulk(0, "./../Dataset/aircraft-0", "sla0")
img.generateBulk(1, "./../Dataset/aircraft-1", "sla1")
img.generateBulk(2, "./../Dataset/aircraft-2", "sla2")
img.generateBulk(3, "./../Dataset/aircraft-3", "sla3")
img.generateBulk(4, "./../Dataset/aircraft-4", "sla4")
img.generateBulk(5, "./../Dataset/aircraft-5", "sla5")
