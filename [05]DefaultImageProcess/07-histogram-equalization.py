import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import getimg


# 이미지 불러오기
roi = getimg.gImg('lenna', 'png')
equalized_roi = np.zeros((roi.shape[0], roi.shape[1], roi.shape[2]), dtype=np.uint8)

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
        b_hist[roi[i,j,0]] += 1
        g_hist[roi[i,j,1]] += 1
        r_hist[roi[i,j,2]] += 1

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
        equalized_roi[i,j,0] = eq_b_hist[roi[i,j,0]]
        equalized_roi[i,j,1] = eq_g_hist[roi[i,j,1]]
        equalized_roi[i,j,2] = eq_r_hist[roi[i,j,2]]

plt.subplot(1,2,1)
b,g,r = cv.split(roi)
roi_rgb = cv.merge([r,g,b])
plt.imshow(roi_rgb)

plt.subplot(1,2,2)
b,g,r = cv.split(equalized_roi)
roi2_rgb = cv.merge([r,g,b])
plt.imshow(roi2_rgb)

plt.show()