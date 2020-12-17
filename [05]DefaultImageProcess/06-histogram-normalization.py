import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import getimg


# 이미지 불러오기
roi = getimg.gImg('lenna', 'png')

equalizaed_roi = np.zeros((roi.shape[0], roi.shape[1], roi.shape[2]), dtype=np.uint8)

r_hist = np.zeros((256),dtype=np.int)
g_hist = np.zeros((256),dtype=np.int)
b_hist = np.zeros((256),dtype=np.int)

nm_r_hist = np.zeros((256),dtype=np.float)
nm_g_hist = np.zeros((256),dtype=np.float)
nm_b_hist = np.zeros((256),dtype=np.float)




for i in range(roi.shape[0]):
    for j in range(roi.shape[1]):
        b_hist[roi[i,j,0]] += 1
        g_hist[roi[i,j,1]] += 1
        r_hist[roi[i,j,2]] += 1

for _ in range(256):
    nm_b_hist[_] = b_hist[_] / (roi.shape[0]*roi.shape[1])
    nm_g_hist[_] = g_hist[_] / (roi.shape[0]*roi.shape[1])
    nm_r_hist[_] = r_hist[_] / (roi.shape[0]*roi.shape[1])


plt.subplot(1,2,1)
b,g,r = cv.split(roi)
roi_rgb = cv.merge([r,g,b])

plt.imshow(roi_rgb)
plt.subplot(1,2,2)

plt.plot(nm_b_hist, color='b')
plt.plot(nm_g_hist, color='g')
plt.plot(nm_r_hist, color='r')

plt.show()