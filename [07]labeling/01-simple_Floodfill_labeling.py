import cv2 as cv
import numpy as np
from getimg import *
import random

def flood_fill4(l, j, i, label):
    if l[j,i] == -1:
        l[j,i] = label
        flood_fill4(l, j, i+1, label)  # east
        flood_fill4(l, j-1, i, label)  # north
        flood_fill4(l, j, i-1, label)  # west
        flood_fill4(l, j+1, i, label)  # south
        
        
roi = gImg('label_pig1', 'jpg')

roi = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
ret, bin_roi = cv.threshold(roi, 127, 255, cv.THRESH_BINARY)

label_img = np.zeros((bin_roi.shape[0], bin_roi.shape[1]), dtype=np.int)

# 책에서 1은 -1 0은 0으로 복사한다고 했음. 여기서는 이진화 된 값인 255와 0으로 구별하여 255이면 -1 나머지는 0으로 복사
# 이미지 밖으로 나가는것을 막기위해 맨 바깥쪽 픽셀영역은 전부 0으로 복사
for i in range(bin_roi.shape[1]):
    for j in range(bin_roi.shape[0]):
        if j == 0 or j == bin_roi.shape[0]-1 or i == 0 or i == bin_roi.shape[1] - 1 :
            label_img.itemset(j,i,0) # 경계 0으로 채우기. 끝을 검사하지 않기위해서
        elif bin_roi.item(j,i) == 255:
            #label_img[j][i] = -1
            label_img.itemset(j,i,-1) # 객체픽셀은 -1로 채움
        else:
            label_img.itemset(j,i,0) # 아니면 0  

label = 1

for i in range(1, bin_roi.shape[1]-1):
    for j in range(1, bin_roi.shape[0]-1):
        if label_img[j][i] == -1:
            flood_fill4(label_img, j, i, label)
            label+=1
            
# 라벨링된 결과를 RGB채널의 새로운 이미지로 보여줌(객체별로 다른 색상을 적용) - 책에는 없음
new_img = np.zeros((bin_roi.shape[0],bin_roi.shape[1],3),dtype=np.uint8)

for i in range(bin_roi.shape[1]):
    for j in range(bin_roi.shape[0]):
        if label_img.item(j,i) > 0:
            random.seed(label_img.item(j,i))
            new_img.itemset(j,i,0,random.randint(0,255))
            new_img.itemset(j,i,1,random.randint(0,255))
            new_img.itemset(j,i,2,random.randint(0,255))

print(label)

cv.imshow('bin img',bin_roi)
cv.imshow('label_img',new_img)

cv.waitKey(0)
cv.destroyAllWindows()
