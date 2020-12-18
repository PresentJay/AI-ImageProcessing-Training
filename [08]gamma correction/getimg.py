import cv2 as cv

def gImg(str, format):
    roi = cv.imread('C:\\Users\\PresentJay\\Desktop\\ai_ml_vision\\AI-ImageProcessing-Training\\img\\{}.{}'.format(str, format))
    return roi
    