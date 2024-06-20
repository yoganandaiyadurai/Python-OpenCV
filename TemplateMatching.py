import numpy as np
import cv2

imgFootballMatchC = cv2.resize(cv2.imread('assets/footballmatch.jpg',-1), (0,0), fx=0.5, fy=0.5)
imgFootballMatch = cv2.resize(cv2.imread('assets/footballmatch.jpg',0), (0,0), fx=0.5, fy=0.5)

templateBall = cv2.resize(cv2.imread('assets/football.png',0), (0,0), fx=0.5, fy=0.5)

imgFootballMatchCopy = imgFootballMatch.copy()

th, tw = templateBall.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = imgFootballMatch.copy()
    img3 = imgFootballMatchC.copy()
    
    result = cv2.matchTemplate(img2, templateBall, method)
    minVal, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(min_loc, max_loc)
    
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
    
    bottom_right = (location[0] + tw, location[1] + th)    
    img3 = cv2.rectangle(img3, location, bottom_right, 255, 5)
    cv2.imshow('Match', img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
    
    
    
    
    
