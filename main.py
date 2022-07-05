import cv2


small = cv2.imread('Small.png')   #بيقرا الصوره الصغيره اللي  هي اللجو اللي  انا هدور عليه ف الصوره الكبيره
large = cv2.imread('Large.png')   # بيقرا الصوره الكبيره اللي هيدور فيها ع اللوجو
(height1, width1) = small.shape[:2]  #بحسب الطول و العرض بتوع الصوره اللوجو
(height2, width2) = large.shape[:2]  #بحسب الطول و العرض بتوع الصوره الكبيره
small_image = cv2.resize(small, (int(width1 / 2), int(height1 / 2)), interpolation = cv2.INTER_CUBIC) #بصغر حجم الصوره للنص عشان كانت  كبيره
large_image = cv2.resize(large, (int(width2 / 2), int(height2 / 2)), interpolation = cv2.INTER_CUBIC) #بصغر حجم الصوره للنص عشان كانت  كبيره


method = cv2.TM_SQDIFF_NORMED    # الطريقه اللي هنقارن بيها بين الصورتين

res = cv2.matchTemplate(small,large,method)  # بيجيب مكان اللوجو ف الصوره الكبيره
mn1,_,mnloc1,_=cv2.minMaxLoc(res)  # بيجيب مكان البدايه والنهايه
mpx,mpy=mnloc1 # بيجيب مكان البدايه والنهايه
trows1,tcols1 = small.shape[:2] # بيجيب الكول  والعرض بتوع الصوره الصغيره

#الاربع سطور اللي جايين دول  نفس اللي فوق  بس بينفذهم ع الصوره بعد ما غيرت حجمها
result = cv2.matchTemplate(small_image, large_image, method)
mn,_,mnLoc,_ = cv2.minMaxLoc(result)
MPx,MPy = mnLoc
trows,tcols = small_image.shape[:2]

cropped_image = large [mpy:mpy+trows1,mpx:mpx+tcols1] # بيقص اللوجو من الصوره الكبيره ويعرضه
cv2.imshow("Res", cropped_image)


cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2) # بيرسم المستطيل حولين اللوجو في الصوره الكبيره
cv2.imshow('Result',large_image)
cv2.waitKey(0)