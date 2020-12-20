import cv2
import numpy as np
import sys
import os
import math
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QSlider
from PyQt5 import uic
from math import cos, sin, pi, trunc, exp

form_class = uic.loadUiType('C:\\Users\\PresentJay\\Desktop\\ai_ml_vision\\AI-ImageProcessing-Training\\ui\\{}.ui'.format("Log"))[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Slider = self.SigmaValue
        self.Svalue = 1.0
        self.Slider.valueChanged[int].connect(self.changeValue)
        
        self.image = cv2.imread('C:\\Users\\PresentJay\\Desktop\\ai_ml_vision\\AI-ImageProcessing-Training\\img\\{}.{}'.format("image","jpg"))
        self.image = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0],self.image.strides[0],QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap.fromImage(self.image)
        self.pixmap = self.pixmap.scaledToWidth(self.image.width())
        self.label.setPixmap(self.pixmap)
        self.show()
        self.pushButton.clicked.connect(self.show_LOG_image)
    

    def show_LOG_image(self):
        LogSize = (int)(6*self.Svalue)
        ab = 0
        if LogSize%2==0:
            LogSize += 1
        self.label_4.setNum(LogSize)
        LogFilter = np.zeros((LogSize,LogSize))
        for x in range(LogSize):
            for y in range(LogSize):
                a = (((y-(LogSize//2))**2) + ((x-(LogSize//2))**2) - 2*(self.Svalue**2))/self.Svalue**4
                b = math.exp(-1 * (((y-(LogSize//2))**2) + ((x-(LogSize//2))**2)) / (2*(self.Svalue**2)))/(2 * math.pi * (self.Svalue**2))
                LogFilter[x,y] = a*b

        gap_image = QtGui.QImage(self.image.width(), self.image.height(),QtGui.QImage.Format_RGB888).rgbSwapped()
        maxi = 0
        Log_image = np.zeros((self.image.width(),self.image.height()))
        for k in range(LogSize):
            for t in range(LogSize):
                ab += LogFilter[k,t]
        for i in range(gap_image.width()):
            for j in range(gap_image.height()):
                G = 0
                for x in range(i-(LogSize//2), i+(LogSize//2)+1):
                    for y in range(j-(LogSize//2), j+(LogSize//2)+1):
                        if x >= 0 and y >= 0 and x < gap_image.width() and y < gap_image.height():
                            pixelData = self.image.pixel(x, y)
                            G += QtGui.qRed(pixelData) * LogFilter[x - i + 1, y - j + 1]
                            
                if G > maxi:
                    maxi = G
                Log_image[i,j] = G
                      
        for i in range (1,gap_image.width()-1):
            for j in range (1,gap_image.height()-1):
                gap = 0
                count = 0
                zero_count = 0
                if (Log_image[i-1,j] > 0 and  Log_image[i+1,j] < 0) or (Log_image[i-1,j] < 0 and  Log_image[i+1,j] > 0):
                    zero_count += 1
                    gap = math.fabs(Log_image[i-1,j-1]-Log_image[i+1,j+1])
                    if gap > maxi*0.05:
                        count += 1
                for k in range(-1,2):
                    if ( Log_image[i+k,j-1] > 0 and  Log_image[i-k,j+1] < 0) or ( Log_image[i+k,j-1] < 0 and  Log_image[i-k,j+1] > 0):
                        zero_count += 1
                        gap = math.fabs(Log_image[i-1,j-1]-Log_image[i+1,j+1])
                        if gap > maxi*0.05:
                            count += 1
                if zero_count > 2 and zero_count == count:
                    gap_image.setPixel(i,j,QtGui.qRgb(0,0,0))
                else :
                    gap_image.setPixel(i,j,QtGui.qRgb(255,255,255))

                
                
        self.label_6.setNum(maxi*0.05)
        pixmap2 = QtGui.QPixmap.fromImage(gap_image)
        pixmap2 = pixmap2.scaledToWidth(gap_image.width())
        self.label_2.setPixmap(pixmap2)

    def changeValue(self, value):
        self.label_3.setNum(value/10)
        self.Svalue = float(value/10)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    display_image_widget = MainWindow()
    display_image_widget.show()
    sys.exit(app.exec_())
            
        

