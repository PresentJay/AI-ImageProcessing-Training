import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import getimg


# 이미지 불러오기
roi = getimg.gImg('lenna', 'png')

r_hist = np.zeros((256),dtype=np.int)
g_hist = np.zeros((256),dtype=np.int)
b_hist = np.zeros((256),dtype=np.int)

nm_r_hist = np.zeros((256),dtype=np.int)
nm_g_hist = np.zeros((256),dtype=np.int)
nm_b_hist = np.zeros((256),dtype=np.int)

eq_r_hist = np.zeros((256),dtype=np.int)
eq_g_hist = np.zeros((256),dtype=np.int)
eq_b_hist = np.zeros((256),dtype=np.int)


for i in range(roi.shape[0]):
    for j in range(roi.shape[1]):
        b_hist[roi[i,j,0]] += 1
        g_hist[roi[i,j,1]] += 1
        r_hist[roi[i,j,2]] += 1

for _ in range(256):
    b_hist[_] = b_hist[_] / (roi.shape[0]*roi.shape[1])
    g_hist[_] = g_hist[_] / (roi.shape[0]*roi.shape[1])
    r_hist[_] = r_hist[_] / (roi.shape[0]*roi.shape[1]) 
       
    eq_b_hist[_] = nm_b_hist[0]
    eq_g_hist[_] = nm_g_hist[0]
    eq_r_hist[_] = nm_r_hist[0]

plt.subplot(1,2,1)
b,g,r = cv.split(roi)

# 12월17일은 위에꺼까지
roi_rgb = cv.merge([r,g,b])
plt.imshow(roi_rgb)
plt.subplot(1,2,2)
plt.plot(b_hist, color='b')
plt.plot(g_hist, color='g')
plt.plot(r_hist, color='r')
plt.show()