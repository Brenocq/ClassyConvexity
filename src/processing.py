import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
from scipy.spatial import ConvexHull # maybe we need a correct implementation of convexhull. Just maybe

class PlaneProcessing:

    def __init__(self):
        print("init")
    
    def findHCD(self, filename):
        self.convexhull = []
        print (filename)
        img = cv2.imread(filename)
        #cv2.imshow("read", img)                                     # Read image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                  # Convert to grayscale
        blur = cv2.blur(gray, (3, 3))                                 # Blur the image
        ret, self.thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY) # Binarize the image
        contours, \
            hierarchy = cv2.findContours(self.thresh, cv2.RETR_TREE,\
                                             cv2.CHAIN_APPROX_SIMPLE) # Finding contours for the binarized

        for contour in contours:
            for point in contour:
                if (point[0][0] == 0 or point[0][0] == img.shape[0]-1 or point[0][1] == 0 \
                    or point[0][1] == img.shape[1]-1):
                    #print("outer box! removing")
                    contours.remove(contour)
                    break

        self.contour = sorted(contours, \
            key = lambda contour: cv2.contourArea(contour), reverse=True)
        
        '''
        for contour in self.contour:
            print("area: {}".format(cv2.contourArea(contour)))
        '''
            
        # calculate hull points for each contour
        for i in range(len(contours)):
            self.convexhull.append(cv2.convexHull(contours[i], False))
        
        #convex hull specific for hull defects
        hull_defects = cv2.convexHull(contours[0], returnPoints = False)

        self.contour    = [self.contour[0]]
        self.convexhull = [self.convexhull[0]]
        self.convexity_defects = cv2.convexityDefects(self.contour[0], hull_defects)
        #print(self.convexity_defects.shape)
        self.area_ratio = cv2.contourArea(self.contour[0]) / cv2.contourArea(self.convexhull[0])
        #print("ratio {}" .format(self.area_ratio))

    def findDistances(self, point_array):
        distance_set = set()
        for point_1 in point_array:
            for point_2 in point_array:
                distance_set.add(round(cv2.norm(point_1, point_2), 3))
        distance_set = sorted (distance_set, reverse=True)
        #
        #print("main axis distance {}".format(distance_set[0]))
        self.main_axis_distance = distance_set[0]

    def sortDefects(self):
        defects_values = []

        if self.convexity_defects is not None:
            for defect in self.convexity_defects:
                defects_values.append(defect[0][3])
        defects_values.sort()
        self.defect_values = defects_values
        #print(defects_values)
        #print(defects_values[0], defects_values[-1])


    def compute(self, filename):
        self.findHCD(filename)
        self.findDistances(self.convexhull[0])
        self.sortDefects()

    def drawImage(self):
        color_contours = (0, 255, 0) # green - color for contours
        color = (255, 0, 0) # blue - color for convex hull

        # create an empty black image
        drawing = np.zeros((self.thresh.shape[0], self.thresh.shape[1], 3), np.uint8)
        
        #print(self.contour)
        #print("hull is {}".format(self.convexhull[0]))

        #print("contours area {}\nhull area {}"\
        #            .format(cv2.contourArea(self.contour[0]),\
        #                    cv2.contourArea(self.convexhull[0])))

        #self.findDistances(self.convexhull[0])
        #print (type(self.convexity_defects))
        #self.sortDefects()
        #draw contour
        if self.contour is not None:
            cv2.drawContours(drawing, self.contour, 0, color_contours, 1, 8)
        
        #draw convex hull
        if self.convexhull is not None:
            cv2.drawContours(drawing, self.convexhull, 0, color, 1, 8)

        cv2.imshow("Image", drawing)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def generateBulk(self, classif, directory, out_file_name):
        data = open(str(out_file_name) + ".csv", "w")
        #head class, main_axis, max_defect, min_defect, area_ratio
        
        onlyfiles = [f for f in os.listdir(directory) \
        if os.path.isfile(os.path.join(directory, f))]
        print(onlyfiles)
        data.write("class, main_axis, max_defect, min_defect, area_ratio\n")
        '''
        for directory in self.path:
            #find files
            for file in directory_list:
            self.compute(file)
            data.write("{}, {}, {}, {}, {}"\
                    .format(self.obj_class,\
                            self.main_axis_distance,\
                            self.defect_values[-1],\
                            self.defect_values[0],\
                            self.area_ratio))
        '''
        for file in onlyfiles:
            self.obj_class = 0
            self.compute(directory + "/" + file)
            data.write("{}, {}, {}, {}, {}\n"\
                    .format(self.obj_class,\
                            self.main_axis_distance,\
                            self.defect_values[-1],\
                            self.defect_values[0],\
                            self.area_ratio))
        data.close()
        pass
