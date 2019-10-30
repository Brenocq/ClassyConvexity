# ClassyConvexity
_By Breno Cunha Queiroz and Henrique Hiram Libutti Núñez_

<p align="center">
<img src="./Data/AircraftsConvexHull.png?raw=true" height="200">
</p>


# Introduction
This project aims to classify binary images of aircrafts using convex hull and image processing techniques. Here we generate our own dataset and extracted features from these images into a `.csv` file. In the end, we use different machine learning techniques to classify the images.

## Dataset
We generated our aircraft data based on images of binarized aircrafts found on internet. To augment our dataset and try to recreate real-world situations where airplanes are viewed from different angles we perform transformations on top of images to generate images from other angles. Some of the transformations were: translation, rotation, zoom, and flip. We generated different 100 for each class.

Original:
<p align="center">
<img src="https://github.com/Brenocq/ClassyConvexity/blob/master/Dataset/aircraft-0/0.jpg?raw=true" height="100">
<img src="https://github.com/Brenocq/ClassyConvexity/blob/master/Dataset/aircraft-1/0.jpg?raw=true" height="100">
<img src="https://github.com/Brenocq/ClassyConvexity/blob/master/Dataset/aircraft-2/0.jpg?raw=true" height="100">
<img src="https://github.com/Brenocq/ClassyConvexity/blob/master/Dataset/aircraft-3/0.jpg?raw=true" height="100">
<img src="https://github.com/Brenocq/ClassyConvexity/blob/master/Dataset/aircraft-4/0.jpg?raw=true" height="100">
</p>
Transformed:
<p align="center">
<img src="https://github.com/Brenocq/ClassyConvexity/blob/master/Dataset/aircraft-0/1.jpg?raw=true" height="100">
<img src="https://github.com/Brenocq/ClassyConvexity/blob/master/Dataset/aircraft-1/2.jpg?raw=true" height="100">
<img src="https://github.com/Brenocq/ClassyConvexity/blob/master/Dataset/aircraft-2/3.jpg?raw=true" height="100">
<img src="https://github.com/Brenocq/ClassyConvexity/blob/master/Dataset/aircraft-3/4.jpg?raw=true" height="100">
<img src="https://github.com/Brenocq/ClassyConvexity/blob/master/Dataset/aircraft-4/5.jpg?raw=true" height="100">
</p>

## Data Processing
After getting all your data generated, we started to extract features from our images to create an features dataset.  Were chosen four features to generate the new data set: main axis length, area ratio, maximum convex hull defect, minimum convex hull defect.

Before taken the convex hull, we blur the image and found contours. First we are using _OpenCV_ to calculate the convex hull, but it returns a wrong convex hull. To solve this problem, we are also using the _scipy_ convex hull calculation to perform a second convex hull, which is more accurate.

With the convex hull calculated, we found the ratio between the area of the aircraft and the area of the convex hull. Also, we used OpenCV functions to found the main axis length, and the maximum and minimum convex hull defect.

With that information, we generated [this csv file](https://github.com/Brenocq/ClassyConvexity/blob/master/src/aeroclasses.csv). You can see the images we used to train our model in [this folder](https://github.com/Brenocq/ClassyConvexity/tree/master/Dataset).

## Training
For classifying the data, this work uses different machine learning techniques. this work uses _scikit-learn_ for SVM(Support Vector Machine) and Random Forest implementation. We tested with linear, rbf and polynomial SVM kernels.

## Results
For each training, we generated a confusion matrix, our results below:

<center>

**Linear SVM**

<img src="./Data/ResLinearSVM.png?raw=true" height="200">
<br><br><br>

**Polynomial SVM**

<img src="./Data/ResPolySVM.png?raw=true" height="200">
<br><br><br>

**RBF SVM**

<img src="./Data/ResRbfSVM.png?raw=true" height="200">
<br><br><br>

**Decision Tree**

<img src="./Data/ResDecisionTree.png?raw=true" height="200">
<br><br><br>

**Random Forest**

<img src="./Data/ResRandomForest.png?raw=true" height="200">
<br><br><br>

</center>

## How to use
There are 4 files to check and test our data. They were written using jupyter notebook.
You will found them inside `src`:
- **0 - Generate Data:** Here you can generate the image data to the `Data` folder.
- **1.0 - Visualization Feature Extraction:** To view convex hulls from aircraft images.
- **1.1 - Feature Extraction:** To extract image features and generate the `.csv` file.
- **2 - Training:** To train different models using the `.csv` data.

## Installation
To install **Scikit**. Follow the steps [here](https://scikit-image.org/docs/dev/install.html).

To install **Pandas**. Follow steps [here](https://pandas.pydata.org/pandas-docs/stable/install.html).

To install **OpenCV**:
```
$ pip install opencv-python
```

To install **Keras Preprocessing**:
```
pip install Keras-Preprocessing
```
