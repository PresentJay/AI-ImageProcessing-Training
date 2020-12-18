import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from getimg import *

# Otsu79 (Optimization algorithm)
""" 임계값 T를 기준으로 화소를 두 집합으로 나누었을 때,
각 집합의 명암 분포가 균일할수록 (분산이 작을수록) 좋다. """

roi = gImg('pic1', 'JPG')
gray = cv.cvtColor(roi,cv.COLOR_BGR2GRAY)

binary = np.zeros((gray.shape[0],gray.shape[1]),dtype=np.uint8)

# 임계값 t를 0 ~ L-1 로 반복하여 어떤 임계값이 최소치인지 확인
# 가중치 w0는 t값 이전까지의 hat값의 총합이다.
# 가중치 w1은 t값 초과부터 L-1까지의 hat값의 총합이다.

# 히스토그램 생성
gray_hist = np.zeros(256)
# 정규화된 히스토그램 생성
norm_hist = np.zeros(256,dtype=np.float)

# 기본 히스토그램을 구한다.
for i in range(gray.shape[1]):
    for j in range(gray.shape[0]):
        gray_hist[gray.item(j,i)]+=1
# 정규화 시켜서 저장한다.
for i in range(256):
    norm_hist[i] = gray_hist[i] / (gray.shape[0]*gray.shape[1])

vwlist = []

for i in range(1,256): #T값을 결정하기위해서 1부터~256단계까지 바꾸어 나간다
    w0 = 0.0
    w1 = 0.0
    u0 = 0.0
    u1 = 0.0
    v0 = 0.0
    v1 = 0.0
    for j in range(i):
        w0 += norm_hist[j] #T가 1이라면  정규화된 값을 넣고
    for j in range(i+1,256):
        w1 += norm_hist[j] # 나머지값(2부터255까지 누적값 더하기)을 w1에넣고
    if w0 == 0 or w1 == 0:
        continue
    for j in range(i):
        u0 += j*norm_hist[j]
    u0 /= w0
    for j in range(i+1,256):
        u1 += j*norm_hist[j]
    u1 /= w1
    for j in range(i):
        v0 += norm_hist[j]*(j-u0)**2
    v0 /= w0
    for j in range(i+1,256):
        v1 += norm_hist[j]*(j-u1)**2
    v1 /= w1
    v_within = w0 * v0 + w1 * v1
    
    vwlist.append(v_within)
    
    
t_argmin = np.argmin(vwlist)
print(t_argmin, vwlist[t_argmin])

plt.plot(vwlist)
plt.show()

for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        if gray[i,j] >= t_argmin:
            binary[i,j] = 255
        else:
            binary[i,j] = 0

cv.imshow('binary img',binary)
cv.waitKey(0)
cv.destroyAllWindows()