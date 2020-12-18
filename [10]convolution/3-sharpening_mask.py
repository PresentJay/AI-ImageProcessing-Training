import cv2 as cv
import numpy as np
from getimg import*
#smoothing
roi = gImg('picture5','jpg')
roi_gray = cv.cvtColor(roi,cv.COLOR_BGR2GRAY)

sharpening_mask = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])

output_box = np.zeros((roi.shape[0],roi.shape[1]),dtype=np.uint8)

for j in range(1,roi.shape[0]-1):
    for i in range(1,roi.shape[1]-1):
        sum = 0
        for r in range(-1,2):
            for c in range(-1,2):
                sum += roi_gray.item(j+r,i+c)* sharpening_mask.item(r+1,c+1)  #mask 값
        if np.sum(sharpening_mask)>0:
            sum //= np.sum(sharpening_mask)
        output_box.itemset(j,i,sum)

cv.imshow('origin',roi_gray)
cv.imshow('sharpening_mask',output_box)
cv.waitKey(0)
cv.destroyAllWindows()