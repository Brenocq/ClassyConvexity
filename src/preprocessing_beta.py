import numpy as np
import cv2
import matplotlib.pyplot as plt
import os

#Images are found in the folder ...

from scipy.spatial import ConvexHull # maybe we need a correct implementation of convexhull. Just maybe

'''
this file implements image processing, including treatment

'''
#filename: string


#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


class PlaneProcessing:

    def __init__(self, path):
        onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        print(onlyfiles)
    
    def findHCD(self, file):

        img = cv2.imread("0.jpg")                                     # Read image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                  # Convert to grayscale
        blur = cv2.blur(gray, (3, 3))                                 # Blur the image
        ret, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY) # Binarize the image
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,\
                                             cv2.CHAIN_APPROX_SIMPLE) # Finding contours for the binarized

        for contour in contours:
            for point in contour:
                if (point[0][0] == 0 or point[0][0] == width-1 or point[0][1] == 0 \
                    or point[0][1] == heigth-1):
                    print("outer box! removing")
                    contours.remove(contour)
                    break

        #This reversely sorts the contours found, and selects the one with
        #largest number of elements
        self.contour = sorted(contours, key = lambda x: x.shape[0], reverse=True)[0]
        self.convexhull = cv2.convexHull(self.contour, False)
        self.convexity_defects = cv2.convexityDefects(self.contour, self.convexhull)

        return contour, convexhull, convexityefects

    def drawImage(self):
        # create an empty black image
        drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
        
        #draw contour
        if self.contour is not None:
            cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
        
        # draw convex hull
        if self.hull is not None:
            cv2.drawContours(drawing, hull, i, color, 1, 8)

        #if kwargs['defects'] is not None:
        #    cv2.drawContours(drawing, hull, i, color, 1, 8)
        cv2.imshow("Image", drawing)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def generate():
        pass


'''
# draw contours and hull points, and find convexity defects
defects = [] 

for i in range(len(contours)):
	color_contours = (0, 255, 0) # green - color for contours
	color = (255, 0, 0) # blue - color for convex hull
	# draw ith contour
	cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
	# draw ith convex hull object
	cv2.drawContours(drawing, hull, i, color, 1, 8)
	#print(len(hull[i]))
	defects.append(cv2.convexityDefects(contours[i], hull_defects[i]))

cv2.imshow("Image", drawing)
cv2.waitKey(0)
print(defects)
'''
'''
TENDO AGORA OS CONTOURS E ETC, TEMOS QUE APRENDER A ENCONTRAR:
	-OS PONTOS DE BICO E RABO DO AVIAO
	-A PONTA DE CADA ASA
	-A ÁREA DO AVIÃO/ÁREA DO CH
	-OS DEFEITOS DE CONVEXIDADE, QUE JÁ TÃO QUASE TODOS IMPLEMENTADOS
'''


'''
for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img,start,end,[0,255,0],2)
    cv2.circle(img,far,5,[0,0,255],-1)
'''

