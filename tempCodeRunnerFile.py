sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely =cv.Sobel(gray,cv.CV_64F,0,1)
cv.imshow("Sobel x",sobelx)
cv.imshow("Sobel y",sobely)