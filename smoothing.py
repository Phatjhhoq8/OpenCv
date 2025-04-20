import cv2 as cv

img = cv.imread('Resources\Photos\cat.jpg')
cv.imshow("IMG",img)
# averaging
average = cv.blur(img,(7,7))
cv.imshow("Average blur",average)
# Gaussion blur
gaussion = cv.GaussianBlur(img,(7,7),1)
cv.imshow("Gaussian",gaussion)
# median blur
median = cv.medianBlur(img,7)
cv.imshow("Median",median)
# Bilateral lam mo 2 ben
bilateral = cv.bilateralFilter(img,5,10,10)
cv.imshow("Bilateral",bilateral)
cv.waitKey(0)