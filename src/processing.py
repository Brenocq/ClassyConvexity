import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
from scipy.spatial import ConvexHull, convex_hull_plot_2d
import math

class PlaneProcessing:

    def __init__(self, out_file_name):
        self.out_name = out_file_name
        data = open(str(out_file_name) + ".csv", "w")
        data.write("class,main_axis,area_ratio,max_defect,min_defect\n")
        data.close()
        print("init")

    def refineConvexhull(self, hull):
        '''
        This function removes errors on the convex hull and returns the convex hull ordered points
        '''

        points = []

        #----- Calculate convex hull points -----#
        for contour in hull:
            for point in contour:
                if(point[0][0]!=0 and point[0][0]!=199 and point[0][1]!=0 and point[0][1]!=199):
                    points.append([point[0][0], point[0][1]])

        indexhull = ConvexHull(points)

        n = 0
        hullPoints = []

        for simplex in indexhull.simplices:
            hullPoints.append([points[simplex[0]][0], points[simplex[0]][1]])
            n=n+1


        #----- Center point -----#
        centerPoint = [0,0]

        for hullPoint in hullPoints:
            centerPoint[0]+= hullPoint[0]
            centerPoint[1]+= hullPoint[1]

        centerPoint[0]/=n
        centerPoint[1]/=n

        #----- Sort points around center point -----#
        angles = [None] * n
        for i in range(0, n):
            angles[i] = math.atan2(hullPoints[i][1]-centerPoint[1], hullPoints[i][0]-centerPoint[0]);

        # Sorting
        for i in range(0, n):
            for j in range(0, n):
                if(angles[j]>=angles[i]):
                    tempAngle = angles[i]
                    tempPoint = hullPoints[i]

                    hullPoints[i] = hullPoints[j]
                    angles[i] = angles[j]
                    hullPoints[j] = tempPoint
                    angles[j] = tempAngle

        return n,hullPoints

    def calcAreaAircraft(self, img):
        '''
        Return the aircraft area (black pixels)
        '''
        totalNumPixels = 40000.
        numBlackPixels = 0.
        cont = 0
        
        # Sum number of black pixels
        for i in img:
            for j in i:
                cont=cont+1
                if(j==0):
                    numBlackPixels=numBlackPixels+1

        return numBlackPixels/totalNumPixels*100

    def calcAreaConvexhull(self, hull):
        '''
        Return the convex hull area using the shoelace formula 
        '''
        n, hullPoints = self.refineConvexhull(hull)

        #----- Calculates area -----#
        area = 0.0

        # Calculate value of shoelace formula
        j = n - 1
        for i in range(0,n):
            area += (hullPoints[j][0] + hullPoints[i][0]) * (hullPoints[j][1] - hullPoints[i][1])
            j = i   # j is previous vertex to i


        return abs(0.5*area/40000*100)


    def findHCD(self, filename):
        '''
        Compute convex hull and main image features
        '''
        self.convexhull = []
        print (filename)
        img = cv2.imread(filename)                                    # Read image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                  # Convert to grayscale
        blur = cv2.blur(gray, (3, 3))                                 # Blur the image
        ret, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY) # Binarize the image
        contours, \
            hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,\
                                             cv2.CHAIN_APPROX_SIMPLE) # Finding contours for the binarized

        for contour in contours:
            for point in contour:
                if (point[0][0] == 0 or point[0][0] == img.shape[0]-1 or point[0][1] == 0 \
                    or point[0][1] == img.shape[1]-1):
                    contours.remove(contour)
                    break

        self.contour = sorted(contours, \
            key = lambda contour: cv2.contourArea(contour), reverse=True)

  
        # calculate hull points for each contour
        for i in range(len(contours)):
            self.convexhull.append(cv2.convexHull(contours[i], False))

        #convex hull specific for hull defects
        hull_defects = cv2.convexHull(contours[0], returnPoints = False)

        # Calculate areas
        self.areaAircraft = self.calcAreaAircraft(thresh)
        self.areaConvexhull = self.calcAreaConvexhull(self.convexhull)
        self.area_ratio = self.areaAircraft/self.areaConvexhull

        self.contour    = [self.contour[0]]
        self.convexhull = [self.convexhull[0]]
        self.convexity_defects = cv2.convexityDefects(self.contour[0], hull_defects)

    def findDistances(self, point_array):
        '''
        Find maximum distance between two points and plot the line
        '''
        distance_set = set()
        for point_1 in self.convexhullPoints:
            for point_2 in self.convexhullPoints:
                if(point_1[0]!=point_2[0] and point_1[1]!=point_2[1]):
                    dX = point_1[0]-point_2[0]
                    dY = point_1[1]-point_2[1]
                    dist = math.sqrt(dX*dX + dY*dY)
                    distance_set.add(dist)

        distance_set = sorted (distance_set, reverse=True)

        self.main_axis_distance = distance_set[0]/self.areaConvexhull

    def sortDefects(self):
        '''
        Sort convex hull defects
        '''
        defects_values = []

        if self.convexity_defects is not None:
            for defect in self.convexity_defects:
                defects_values.append(defect[0][3])
        defects_values.sort()
        self.defect_values = defects_values

    def compute(self, filename):
        '''
        Calculates convex hull and all image features
        '''
        self.findHCD(filename)
        self.findDistances(self.convexhull[0])
        self.sortDefects()

    def drawImage(self):
        '''
        Draw image with convex hull
        '''
        color_contours = (0, 255, 0) # green - color for contours
        color = (255, 0, 0) # blue - color for convex hull

        # Create an empty black image
        drawing = np.zeros((self.thresh.shape[0], self.thresh.shape[1], 3), np.uint8)
        if self.contour is not None:
            cv2.drawContours(drawing, self.contour, 0, color_contours, 1, 8)

        # Draw convex hull
        if self.convexhull is not None:
            cv2.drawContours(drawing, self.convexhull, 0, color, 1, 8)

        cv2.imshow("Image", drawing)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def generateBulk(self, classif, directory):
        '''
        Generate the features dataset of a class
        '''
        data = open(str(self.out_name) + ".csv", "a")

        onlyfiles = [f for f in os.listdir(directory) \
        if os.path.isfile(os.path.join(directory, f))]
        print(onlyfiles)

        # Write data to the file
        for file in onlyfiles:
            self.obj_class = classif
            self.compute(directory + "/" + file)

            maxDefect = self.defect_values[-1]
            minDefect = self.defect_values[0]

            data.write("{}, {}, {}, {}, {}\n"\
                    .format(self.obj_class,\
                            self.main_axis_distance,\
                            self.area_ratio,\
                            maxDefect,\
                            minDefect))
        data.close()
        pass
