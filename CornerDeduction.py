import numpy as np
import cv2

img = cv2.imread('assets/chessboard.png',-1);
img = cv2.resize(img, (400,400))
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#width = int(img.get(3))
#height = int(img.get(4))
corners = cv2.goodFeaturesToTrack(grey,100,0.01,10)
corners = np.int_(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),5,(255,0,0), -1)

for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0,255,size=3)))
        cv2.line(img, corner1, corner2,color,1)
        
print(corners)

cv2.imshow('Image', img)

cv2.waitKey(0)

cv2.destroyAllWindows();
