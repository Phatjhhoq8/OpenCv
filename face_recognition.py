import numpy as np
import cv2 as cv
import os
haar_cascade = cv.CascadeClassifier('haar_face.xml')
people = []
DIR =r'C:\Users\Phat\Desktop\OpenCv\Resources\Faces\train'
for i in os.listdir(DIR):
    people.append(i)
haar_cascade = cv.CascadeClassifier('haar_face.xml')
# features = np.load('features.npy')
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'C:\Users\Phat\Desktop\OpenCv\Resources\Faces\train\Madonna\12.jpg')
gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Person",gray)

faces_rect = haar_cascade.detectMultiScale(gray,1.1,4)
for (x,y,w,h) in faces_rect:
    face_roi = gray[y:y+h,x:x+h]
    label, confident = face_recognizer.predict(face_roi)
    print(f'Label = {people[label]} with a confidence {confident}')
    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow("Dectect face",img)
cv.waitKey(0)