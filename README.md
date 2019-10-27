# ClassyConvexity
_By Breno Cunha Queiroz and Henrique Hiram Libutti Núñez_

# Introduction
In this project we aim to classify airplanes using convex hull and machine learning techniques. The first step was to segment our dataset. After that, we calculated the area of each airplane and compared with the convex hull area. At the end, we trained a Support Vector Machine with the area data to classify the aircrafts.

## Dataset
We created our own dataset because this is how we do in Brazil, yo.

## Data Processing
The code contained here uses OpenCV-Python for image operations such as:
-Blurrying and finding contours
-Finding the convex hull and convexity defects
-Measuring distances between given points.

## Training
For classifying the data, the works uses scikit-learn SVM implementation, using RBF kernel. More details on the paper provided in [References]

## Results

## Installation
First, you need to install scikit, follow the steps [here](https://scikit-image.org/docs/dev/install.html)
  `pip install -m requirements.txt`

###References
-Do we have any ?
