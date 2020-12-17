import cv2 as cv
import numpy as np


# 이미지 불러오기
roi = cv.imread('C:\\Users\\PresentJay\\Desktop\\ai_ml_vision\\AI-ImageProcessing-Training\\[05]DefaultImageProcess\\lenna.png')

# 원본 이미지와 같은 크기의 빈 이미지 생성
img = np.zeros((roi.shape[0], roi.shape[1],3), dtype=np.uint8)

# 원본 이미지를 돌면서 픽셀 하나씩 참조
for i in range(roi.shape[0]):
    for j in range(roi.shape[1]):
        # OpenCV에서 이미지는 bgr채널로 이루어짐.
        # 이미지 흑백화는 모든 채널값의 평균값을 각 채널에 뿌려준다.
        value = roi[i,j,0] + roi[i,j,1] + roi[i,j,2]
        
        img[i,j,0] = value/3 # b 채널의 픽셀 계산
        img[i,j,1] = value/3 # g 채널의 픽셀 계산
        img[i,j,2] = value/3 # r 채널의 픽셀 계산

cv.imshow('origin', roi) # 원본 이미지 출력
cv.imshow('greychannel', img) # 반전된 이미지 출력
cv.waitKey(0)
cv.destroyAllWindows()