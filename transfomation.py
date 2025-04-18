import cv2 as cv
import numpy as np
img = cv.imread('Resources\Photos\cat.jpg')
cv.imshow("Cat",img)
# dich hinh
def translate(frame,x,y):
    transMatrix = np.float32([[1,0,x],[0,1,y]])
    dimensions = (frame.shape[1],frame.shape[0])
    return cv.warpAffine(frame,transMatrix,dimensions)
img_translate= translate(img,100,100)
cv.imshow("Translated ",img_translate)
# xoay hinh
def rotate(frame,angle,poitRoot=None):
    (height,width) = frame.shape[:2]
    if poitRoot==None:
        poitRoot = (width//2,height//2)
    rotMax = cv.getRotationMatrix2D(poitRoot,angle,1.0)
    dimensions = (width,height)
    return cv.warpAffine(frame,rotMax,dimensions)
img_rotate = rotate(img,45)
cv.imshow("Rotated",img_rotate)
# lat hinh
flip = cv.flip(img,-1)
cv.imshow("Filp",flip)
cv.waitKey(0)