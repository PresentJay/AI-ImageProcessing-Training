import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np


# 이미지 불러오기
roi = cv.imread('C:\\Users\\PresentJay\\Desktop\\ai_ml_vision\\AI-ImageProcessing-Training\\img\\lenna.png')

grey_img = np.zeros((roi.shape[0], roi.shape[1],3), dtype=np.uint8)
equalized_roi = np.zeros((roi.shape[0], roi.shape[1], roi.shape[2]), dtype=np.uint8)

# 원본 이미지를 돌면서 픽셀 하나씩 참조
for i in range(roi.shape[0]):
    for j in range(roi.shape[1]):
        # OpenCV에서 이미지는 bgr채널로 이루어짐.
        # 이미지 흑백화는 모든 채널값의 평균값을 각 채널에 뿌려준다.
        value = roi[i,j,2]*0.299 + roi[i,j,1]*0.587 + roi[i,j,0]*0.114
        
        grey_img[i,j,0] = value # b 채널의 픽셀 계산
        grey_img[i,j,1] = value # g 채널의 픽셀 계산
        grey_img[i,j,2] = value # r 채널의 픽셀 계산

r_hist = np.zeros((256),dtype=np.int)
g_hist = np.zeros((256),dtype=np.int)
b_hist = np.zeros((256),dtype=np.int)

nm_r_hist = np.zeros((256),dtype=np.float)
nm_g_hist = np.zeros((256),dtype=np.float)
nm_b_hist = np.zeros((256),dtype=np.float)

c_r_hist = np.zeros((256),dtype=np.float)
c_g_hist = np.zeros((256),dtype=np.float)
c_b_hist = np.zeros((256),dtype=np.float)

eq_r_hist = np.zeros((256),dtype=np.int)
eq_g_hist = np.zeros((256),dtype=np.int)
eq_b_hist = np.zeros((256),dtype=np.int)

for i in range(roi.shape[0]):
    for j in range(roi.shape[1]):
        b_hist[grey_img[i,j,0]] += 1
        g_hist[grey_img[i,j,1]] += 1
        r_hist[grey_img[i,j,2]] += 1

for _ in range(256):
    nm_b_hist[_] = b_hist[_] / (roi.shape[0]*roi.shape[1])
    nm_g_hist[_] = g_hist[_] / (roi.shape[0]*roi.shape[1])
    nm_r_hist[_] = r_hist[_] / (roi.shape[0]*roi.shape[1]) 
       
c_b_hist[0] = nm_b_hist[0]
c_g_hist[0] = nm_g_hist[0]
c_r_hist[0] = nm_r_hist[0]

for _ in range(1,256):
    c_b_hist[_] = c_b_hist[_-1] + nm_b_hist[_]
    c_g_hist[_] = c_g_hist[_-1] + nm_g_hist[_]
    c_r_hist[_] = c_r_hist[_-1] + nm_r_hist[_]
    
for _ in range(256):
    eq_b_hist[_] = round(c_b_hist[_] * 255)
    eq_g_hist[_] = round(c_g_hist[_] * 255)
    eq_r_hist[_] = round(c_r_hist[_] * 255)

for i in range(roi.shape[0]):
    for j in range(roi.shape[1]):
        equalized_roi[i,j,0] = eq_b_hist[grey_img[i,j,0]]
        equalized_roi[i,j,1] = eq_g_hist[grey_img[i,j,1]]
        equalized_roi[i,j,2] = eq_r_hist[grey_img[i,j,2]]

plt.subplot(1,2,1)
b,g,r = cv.split(grey_img)
roi_rgb = cv.merge([r,g,b])
plt.imshow(roi_rgb)

plt.subplot(1,2,2)
b,g,r = cv.split(equalized_roi)
roi2_rgb = cv.merge([r,g,b])
plt.imshow(roi2_rgb)

plt.show()