import cv2
import random;

img = cv2.imread('assets/Estonia Lillioru 4.jpg', -1)

img = cv2.imread('assets/Estonia Lillioru 4.jpg', -1)
img = cv2.resize(img,(0,0), fx= 0.25, fy=0.25)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)


print(img[0][10])

for i in range(100):
    for j in range(img.shape[1]):
        img[i,j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows
