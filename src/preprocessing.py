import numpy as np
import cv2
import matplotlib.pyplot as plt
#Images are found in the folder ...

'''
this file implements image processing, including treatment

'''

#filename: string

# Read image
img = cv2.imread("0.jpg")

cv2.imshow("Image", img)
cv2.waitKey(0)

#apply gray, blur
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to grayscale

#cv2.imshow("Image", gray)
#cv2.waitKey(0)

blur = cv2.blur(gray, (3, 3)) # blur the image

#cv2.imshow("Image", blur)
#cv2.waitKey(0)

#binarize the image
ret, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)

# Finding contours for the binarized
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#print(contours)

# TODO remove the contours that do not relate to the aeroplane itself
'''
for contour in contours:
	print(len(contour))
	if (len(contour) == 4):
		print("outer box! removing")
		contours.remove(contour)

print(contours)
'''

# create hull array for convex hull points
hull = []
hull_defects = []

#TODO BRENO LÊ ISSO DAQUI
"""
TA MANO, O QUE FALTA FAZER AQUI:
	-TIRAR ESSA CAIXA QUE FICA FORA DA IMAGEM.
	-TIRAR ESSA BOLINHA ESTRANHA QUE APARECE.
"""

# calculate points for each contour
for i in range(len(contours)):
    # creating convex hull object for each contour
    hull.append(cv2.convexHull(contours[i], False))
    hull_defects.append(cv2.convexHull(contours[i], returnPoints = False))

#print(hull)

# create an empty black image
drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)

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

print(defects)

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
cv2.imshow('img',img)
cv2.waitKey(0)

cv2.imshow("Image", drawing)
cv2.waitKey(0)
cv2.destroyAllWindows()
