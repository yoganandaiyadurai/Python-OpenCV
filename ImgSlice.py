import cv2
import random;

img = cv2.imread('assets/yogi.jpg', -1)

#img = cv2.resize(img,(0,0), fx= 0.25, fy=0.25)


tag = img[148:253, 0:57]
img[168:273, 20:77] = tag


#cv2.imshow('Image', img)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
