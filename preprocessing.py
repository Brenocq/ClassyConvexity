import numpy
import cv2 as cv
import matplotlib.pyplot as plt
#Images are found in the folder ...

#First, we need to crop the images, the 20 lowest rows must be discarded
img = cv.imread("0127508.jpg")

#here we set the size
y = 20
h = img.shape[0]
x = 0
w = img.shape[1]
crop_img = img[:h-y, :w-x]
#cv.imshow("cropped", crop_img)
#print(crop_img.shape[:])

'''
imgray = cv.cvtColor(crop_img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(im2, contours, -1, (0,0,255), 3)

cv.imshow("contours", im2)

cv2.waitKey(0)
'''
blur = cv.GaussianBlur(crop_img,(7,7),0)

#laplacian = cv.Laplacian(blur,cv.CV_64F)
cv.imshow("lapla", blur);
cv.waitKey(0)

edges = cv.Canny(blur,60,140)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()

