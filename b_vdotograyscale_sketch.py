import numpy as np
import cv2
capture = cv2.VideoCapture('VideoFromCamera.mp4')
def nothing(x):
    pass
cv2.namedWindow('sketch')
while(capture.isOpened()):
    ret, frame = capture.read()
    if ret== True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur= cv2.GaussianBlur(gray, (5,5), 0)
        canny =cv2.Canny(blur, 100,150)
        ret, frame = cv2.threshold(canny, 20, 177, cv2.THRESH_BINARY)
        cv2.imshow('Sketch', canny)
        if cv2.waitKey(10) & 0xFF==27:
            break
capture.release()
cv2.destroyAllWindows()