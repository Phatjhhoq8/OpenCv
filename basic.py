import cv2 as cv
img = cv.imread('Resources\Photos\cat.jpg')
cv.imshow("Cat",img)
# doi mau
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)
# lam mo
blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)
# chuoi canh
canny = cv.Canny(img,200,500)
cv.imshow("Canny",canny)
# gian no
dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow("Dilated",dilated)
# soi mon
eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow("Eroded",eroded)
# kich thuoc
resize = cv.resize(img,(200,200),interpolation=cv.INTER_CUBIC)
cv.imshow("Resize",resize)
# cat xen
crop = img[0:100,20:400]
cv.imshow("Croped",crop)
cv.waitKey(0)