import cv2

method = cv2.TM_SQDIFF_NORMED
small = cv2.imread('Small.png')
large = cv2.imread('Large.png')
(height1, width1) = small.shape[:2]
(height2, width2) = large.shape[:2]

small_image = cv2.resize(small, (int(width1 / 2), int(height1 / 2)), interpolation = cv2.INTER_CUBIC)
large_image = cv2.resize(large, (int(width2 / 2), int(height2 / 2)), interpolation = cv2.INTER_CUBIC)




res = cv2.matchTemplate(small,large,method)
mn1,_,mnloc1,_=cv2.minMaxLoc(res)
mpx,mpy=mnloc1
trows1,tcols1 = small.shape[:2]



result = cv2.matchTemplate(small_image, large_image, method)
mn,_,mnLoc,_ = cv2.minMaxLoc(result)
MPx,MPy = mnLoc
trows,tcols = small_image.shape[:2]


cropped_image = large [mpy:mpy+trows1,mpx:mpx+tcols1]
cv2.imshow("Res", cropped_image)


cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)
cv2.imshow('Result',large_image)
cv2.waitKey(0)