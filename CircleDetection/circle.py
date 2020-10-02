import cv2
import numpy as np
from math import pi
img = cv2.imread('test.jpeg', 0)
img = cv2.medianBlur(img, 5)


        
# hough --> only in grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=30, minRadius=0, maxRadius=0)
#If the circles returns nothing(which is the case where it can't find a circle), print msg
if not(isinstance(circles, type(None))):
    circles = np.uint16(np.around(circles))
    #print(len(circles[0])/3)
    print(circles)
    for i in circles[0, :]:
        #i[0] row and i[1] column (center) + i[2] radius
        print(pi * i[2])
        # draw the outer circle
        cv2.circle(gray_img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(gray_img, (i[0], i[1]), 2, (0, 0, 255), 3)

else:
    print("Nothing found.")


#scale
resized_img = cv2.resize(gray_img, (500, 500))
cv2.imshow('detected circles', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
