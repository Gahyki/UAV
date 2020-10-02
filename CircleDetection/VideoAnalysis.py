import numpy as np
import cv2

frame = cv2.imread('test3.mp4')

#cap = cv2.VideoCapture('test.mp4')
fgbg = cv2.createBackgroundSubtractorMOG()

while(1):
    #ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()