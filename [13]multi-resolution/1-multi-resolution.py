import cv2 as cv
import numpy as np

roi = cv.imread('C:\\Users\\PresentJay\\Desktop\\ai_ml_vision\\AI-ImageProcessing-Training\\img\\{}.{}'.format("lenna", "png"))
Burt83a_mask = np.array([
    [0.0025,0.0125,0.0200,0.0125,0.0025],
    [0.0125,0.0625,0.1000,0.0625,0.0125],
    [0.0200,0.1000,0.1600,0.1000,0.0200],
    [0.0125,0.0625,0.1000,0.0625,0.0125],
    [0.0025,0.0125,0.0200,0.0125,0.0025]])

output = np.zeros((roi.shape[0]//2,roi.shape[1]//2,roi.shape[2]),dtype=np.uint8)

for j in range(2,output.shape[0]-2):
    for i in range(2,output.shape[1]-2):
        for k in range(3):
            sum = 0
            for r in range(-2,3):
                for c in range(-2,3):
                    sum += Burt83a_mask.item(r+2,c+2) * roi.item(j*2+r,i*2+c,k)
            output.itemset(j,i,k,sum)
cv.imshow('origin',roi)
cv.imshow('result',output)
cv.waitKey(0)
cv.destroyAllWindows()
