import cv2
cap = cv2.VideoCapture('vv.mp4')
template = cv2.imread('logoo.jpeg')
w, h = template.shape[:2]

if (cap.isOpened()== False):
  print("Error opening video stream or file")

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:

    frame=cv2.rotate(frame, cv2.ROTATE_180)
    res = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + 270, top_left[1] + 250)
    print(top_left)
    print(bottom_right)
    cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
    cv2.imshow('Frame',frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

  else:
    break

cap.release()
cv2.destroyAllWindows()