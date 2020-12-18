import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from getimg import *

# 임계값 (threshold) T -> T를 넘으면 1, 아니면 0

roi = gImg('lenna','png')

THRESHOLD = 127

# roi 이미지를 그레이 채널로 바꿈
gray = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)

# 이진화 채널 초기화
binary = np.zeros((gray.shape[0],gray.shape[1]), dtype= np.uint8)

for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        if gray[i,j] >= THRESHOLD:
            gray[i,j] = 255
        else:
            gray[i,j] = 0

plt.subplot(1,2,1)
b,g,r = cv.split(roi)
roi_rgb = cv.merge([r,g,b])
plt.imshow(roi_rgb)

plt.subplot(1,2,2)

plt.imshow(gray, cmap='gray')
plt.show()