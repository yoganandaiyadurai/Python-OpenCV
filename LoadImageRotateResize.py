import cv2

img = cv2.imread('assets/green earth.jpg',-1);
img = cv2.resize(img, (200,400))

width = int(img.get(3))
height = int(img.get(4))

cv2.imshow('Image', img)

cv2.waitKey(0)

cv2.destroyAllWindows();
