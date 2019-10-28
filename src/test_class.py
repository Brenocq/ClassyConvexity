import importlib

processing = importlib.import_module("processing")
#import processing.py

img = processing.PlaneProcessing(path="/home/hiram/ClassyConvexity/src")
img.findHCD(filename="hi.mock")
img.drawImage()

