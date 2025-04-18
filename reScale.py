import cv2 as cv
def reScale(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    area=(width,height)
    return cv.resize(frame,area,interpolation=cv.INTER_AREA)
# doc hinh anh
img = cv.imread('Resources\Photos\cat.jpg')
img_rescale = reScale(img)
cv.imshow('IMG',img_rescale)
# doc video
capture = cv.VideoCapture('Resources\Videos\dog.mp4')
while True:
    isTrue,frame=capture.read()
    if not isTrue: break
    frame_rescale = reScale(frame)
    cv.imshow("Video",frame_rescale)
    if cv.waitKey(20) & 0xFF==ord('d'): break
capture.release()
cv.destroyAllWindows()
cv.waitKey(0)