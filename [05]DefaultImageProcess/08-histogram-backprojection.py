import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
from math import *
from getimg import *

# I 채널 : 명암 (intensity)
# H 채널 : 색상 (hue)
# S 채널 : 채도 (saturation)

# 얼굴 검출에서, 명암은 쉽게 변하기 때문에 피부 영역을 구별하기 힘듬


# 양자화 : quantize
# 전체 영상에서 최대 h값을 찾아서, 개선하고자 하는 점의 h값을 분자, 최대 h값을 분모로 하면 영상 전체에 대한 값을 0과 1로 양자화 가능

# 이미지 불러오기
roi = gImg('model', 'png')
target = gImg('target', 'png')

# hsv채널로 변환
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
hsv_target = cv.cvtColor(target, cv.COLOR_BGR2HSV)

# openCV 윈도우 생성
cv.namedWindow('img')

def emptyFortrackbar():
    pass

# 트랙바 추가 (기본값은 64)
cv.createTrackbar('scale', 'img', 0, 128, emptyFortrackbar)
cv.setTrackbarMin('scale', 'img', 32)
cv.setTrackbarMax('scale', 'img', 128)
cv.setTrackbarPos('scale', 'img', 64)

while True:
    
    # 책에서 q단계로 줄인 2차원 히스토그램을 만든다.
    # 여기서는 트랙바의 값을 q로 사용한다.
    scale = cv.getTrackbarPos('scale', 'img')
    
    # 06~7단계에서 한 histogram처럼 L^2 크기의 히스토그램을 만들면, 소규모 화소에 적합하지 않음
    
    # 각각 q단계인 model HS hist와 target HS hist를 만든다.
    model_HS_hist = np.zeros((scale, scale))
    target_HS_hist = np.zeros((scale, scale))
    
    # normalized historgram (Using Algorithm 2-2)
    for _ in range(hsv_roi.shape[1]):
        for j in range(hsv_roi.shape[0]):
            model_HS_hist[trunc(hsv_roi.item(j,_,0)*(scale-1)/180), trunc(hsv_roi.item(j,_,1)*(scale-1)/255)]+=1

    for _ in range(scale):
        for j in range(scale):
            nm_model_hist = model_HS_hist / (hsv_roi.shape[0] * hsv_roi.shape[1])    
            
    for _ in range(hsv_target.shape[1]):
        for j in range(hsv_target.shape[0]):
            target_HS_hist[trunc(hsv_target.item(j,_,0) * (scale-1)/180), trunc(hsv_target.item(j,_,1)*(scale-1)/255)]+=1

    for _ in range(scale):
        for j in range(scale):
            nm_target_hist = target_HS_hist / (hsv_target.shape[0] * hsv_target.shape[1])
    
    # 정규 히스토그램
    find_hist = np.zeros((scale, scale), dtype=np.float64)
    
    for i in range(scale):
        for j in range(scale):
            if nm_target_hist[j,i] > 0:
                find_hist[j,i] = nm_model_hist[j,i] / nm_target_hist[j,i]
            else:
                find_hist[j,i] = 0
    
    find_hist = np.minimum(find_hist, 1)
    
    # 타겟 이미지와 같은 크기를 가지는 빈 이미지를 만든다.
    backProjection = np.zeros((target.shape[0], target.shape[1]), dtype= np.float64)
    
    # 빈 이미지에서 역투영을 통해 target에서 어느 부분이 관심영역과 일치하는지 알아내어, 0.0 ~ 1.0 값으로 이미지 위에 나타낸다.
    for i in range(hsv_target.shape[1]):
        for j in range(hsv_target.shape[0]):
            backProjection[j,i] = find_hist[trunc(hsv_target.item(j,i,0)*(scale-1)/180), trunc(hsv_target.item(j,i,1)*(scale-1)/255)]
    
    cv.imshow('img', backProjection)
    
    k = cv.waitKey(1)
    
    if k==27:
        break
    
    
cv.destroyAllWindows()