import importlib
import os
processing = importlib.import_module("processing")
#import processing.py

img = processing.PlaneProcessing("aeroclasses")

# Generate features dataset from image dataset
img.generateBulk(0, "./../Data/aircraft-0")
img.generateBulk(1, "./../Data/aircraft-1")
img.generateBulk(2, "./../Data/aircraft-2")
img.generateBulk(3, "./../Data/aircraft-3")
img.generateBulk(4, "./../Data/aircraft-4")
img.generateBulk(5, "./../Data/aircraft-5")
