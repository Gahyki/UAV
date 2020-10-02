import cv2
import numpy as np
from math import pi
img = cv2.imread('test.jpeg', 0)
img = cv2.medianBlur(img, 5)

print(img)
input_image = []
for i in range(len(img)):
    print(i)
    for x,y,z in img[i]:
        ipt = np.uint16(np.around(im)

