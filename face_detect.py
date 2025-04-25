import cv2 as cv
img = cv.imread('Resources\Photos\group 1.jpg')
cv.imshow("Person",img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)
haar_cascade = cv.CascadeClassifier('haar_face.xml')
face_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=3)
for (x,y,w,h) in face_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
cv.imshow("Face ",img)
cv.waitKey(0)