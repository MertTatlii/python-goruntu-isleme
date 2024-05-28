import cv2
import numpy as np
import pylab as pl
from matplotlib import pyplot as plt

I = cv2.imread('images/peppers.png',0)
kernel1 = np.array([[0,0,0],
                    [0,1,0],
                    [0,0,0]])

# kernel_x = np.array([[-1,1]])
# kernel_y = np.array([[-1],[1]])

kernel_x = np.array([[-1,0,1],
                     [2,0,-2],
                     [1,0,-1]
                     ])

kernel_y = np.array([[1,2,1],
                     [0,0,0],
                     [-1,-2,-1]])

I2_x = cv2.filter2D(I, -1, kernel_x)
I2_y = cv2.filter2D(I, -1, kernel_y)

I2_x_sobel = cv2.Sobel(I, -1, dx=1, dy=0)
I2_y_sobel = cv2.Sobel(I, -1, dx=0, dy=1)

I3 = np.sqrt(np.float32(I2_x)**2+ np.float32(I2_y)**2)

# I2 = cv2.filter2D(I, -1, kernel1)

cv2.imshow('I',I)
# cv2.imshow('I2',I2)
cv2.imshow('I2_x',I2_x)
cv2.imshow('I2_y',I2_y)

cv2.imshow('I2_x_sobel',I2_x_sobel)
cv2.imshow('I2_y_sobel',I2_y_sobel)

cv2.imshow('I3', np.uint8(I3)+50) #burdaki +50 parlaklık
cv2.waitKey()
cv2.destroyAllWindows()











