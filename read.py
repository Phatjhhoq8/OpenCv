import cv2 as cv
# doc hinh anh
# img = cv.imread('Resources\Photos\cat.jpg')
# cv.imshow('IMG',img)
# doc video
capture = cv.VideoCapture('Resources\Videos\dog.mp4')
while True:
    isTrue,frame=capture.read()
    if not isTrue: break
    cv.imshow("Video",frame)
    if cv.waitKey(20) & 0xFF==ord('d'): break
capture.release()
cv.destroyAllWindows()
cv.waitKey(0)