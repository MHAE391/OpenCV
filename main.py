import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('Large.png')
img2 = img.copy()
template = cv.imread('Small.png')
w, h = template.shape[:2]
# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
for meth in methods:
    img = img2.copy()
    method = eval(meth)
    res = cv.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(img,top_left, bottom_right, 255, 2)
    cropped_image = img[bottom_right[0]:bottom_right[1],top_left[0]:top_left[1]]
    plt.subplot(122), plt.imshow(cropped_image)
    plt.title('Cropped'), plt.xticks([]), plt.yticks([])
    plt.subplot(121), plt.imshow(img)
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()