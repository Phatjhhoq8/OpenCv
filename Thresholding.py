import cv2 as cv
import numpy as np

img = cv.imread('Resources\Photos\cats.jpg')
cv.imshow("Cats",img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)
# don gian
threshold, thresh =cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow("Simple Thresholded",thresh)
threshold, thresh_inv =cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow("Simple Thresholded_INV",thresh_inv)
# thich ung maty tinh tu chon diem thich ung
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow("Adaptive",adaptive_thresh)
cv.waitKey(0)