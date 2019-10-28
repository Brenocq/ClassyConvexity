import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
from scipy.spatial import ConvexHull # maybe we need a correct implementation of convexhull. Just maybe

class PlaneProcessing:

    def __init__(self, path):
        onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        self.convexhull = []
        #print(onlyfiles)
    
    def findHCD(self, filename):

        img = cv2.imread("0.jpg")                                     # Read image
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
                    print("outer box! removing")
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
        print(self.convexity_defects.shape)
        self.area_ratio = cv2.contourArea(self.contour[0]) / cv2.contourArea(self.convexhull[0])
        print("ratio {}" .format(self.area_ratio))

    def findDistances(self, point_array):
        distance_set = set()
        for point_1 in point_array:
            for point_2 in point_array:
                distance_set.add(round(cv2.norm(point_1, point_2), 3))
        distance_set = sorted (distance_set, reverse=True)
        #
        print("main axis distance {}".format(distance_set[0]))
        self.main_axis_distance = distance_set[0]

    def compute(self, filename):
        pass

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

        self.findDistances(self.convexhull[0])
        print (self.convexity_defects)
        #draw contour
        if self.contour is not None:
            cv2.drawContours(drawing, self.contour, 0, color_contours, 1, 8)
        
        #draw convex hull
        if self.convexhull is not None:
            cv2.drawContours(drawing, self.convexhull, 0, color, 1, 8)

        cv2.imshow("Image", drawing)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def generateBulk(self, in_path, out_file):
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

