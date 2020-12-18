import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from getimg import *

# 임계값 (threshold) T -> T를 넘으면 1, 아니면 0

roi = gImg('lenna','png')

cv.namedWindow('original')
cv.namedWindow('binarization')

def emptyFortrackbar(x):
    pass

cv.createTrackbar('threshold', 'binarization', 0, 250, emptyFortrackbar)
cv.setTrackbarMax('threshold', 'binarization', 250)
cv.setTrackbarMin('threshold', 'binarization', 10)
cv.setTrackbarPos('threshold', 'binarization', 127)

# roi 이미지를 그레이 채널로 바꿈
gray = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
cv.imshow('original', gray)

while True:
    threshold = cv.getTrackbarPos('threshold', 'binarization')

    # 이진화 채널 초기화
    binary = np.zeros((gray.shape[0],gray.shape[1]), dtype= np.uint8)
    black_cnt = 0
    white_cnt = 0

    for i in range(gray.shape[0]):
        for j in range(gray.shape[1]):
            if gray[i,j] >= threshold:
                binary[i,j] = 255
                white_cnt+=1
            else:
                binary[i,j] = 0
                black_cnt+=1

    print("black = {}, white = {}".format(black_cnt, white_cnt))
    cv.imshow('binarization', binary)
    
    k = cv.waitKey(1)
    
    if k==27:
        break
    
cv.destroyAllWindows()