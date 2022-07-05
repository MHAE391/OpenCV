import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('7.jpeg')
img2 = img.copy()
template = cv.imread('fullLogo.jpeg')
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
    bottom_right = (top_left[0] + h, top_left[1] + w)
    cropped_image = img[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0]]
    plt.axis("off")
    plt.subplot(122)
    plt.title('Cropped'), plt.xticks([]), plt.yticks([])
    plt.imshow(cv.cvtColor(cropped_image, cv.COLOR_BGR2RGB))
    plt.subplot(121)
    cv.rectangle(img, top_left, bottom_right, (0, 0, 255), 8)
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()