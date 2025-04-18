import cv2 as cv
import numpy as np
blank = np.zeros((500,500,3),dtype='uint8')
# cv.imshow("Blank",blank)
# 1 To mau tat ca hinh anh
blank[:] = 0,155,0
cv.imshow("Green",blank)
# 2 Ve hinh chu nhat
cv.rectangle(blank,(100,100),(300,300),(25,10,100),thickness=cv.FILLED)
cv.imshow("Rectangle",blank)
# 3 Ve hinh tam giac
cv.circle(blank,(50,50),250,(12,60,180),thickness=2)
cv.imshow("Circle",blank)
# 4 Ve duong thang
cv.line(blank,(50,100),(100,250),(130,25,98),thickness=4)
cv.imshow("Line",blank)
# 5 Viet chu
cv.putText(blank,"Hello world",(50,100),cv.FONT_HERSHEY_SIMPLEX,1.0,(120,56,42),thickness=3)
cv.imshow("Text",blank)
cv.waitKey(0)