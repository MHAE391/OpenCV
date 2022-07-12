import numpy as np
import cv2 as cv

cap=cv.VideoCapture(0)
template = cv.imread('fullLogo.jpeg')
w, h = template.shape[:2]
while True:
    ret,frame=cap.read()
    res = cv.matchTemplate(frame, template, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + h, top_left[1] + w)
    cv.rectangle(frame, top_left, bottom_right, (0, 0, 255), 4)
    cv.imshow('frame',frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()