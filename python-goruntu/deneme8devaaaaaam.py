#highfilter
import cv2
import numpy as np
import pylab as pl
from matplotlib import pyplot as plt

I = cv2.imread('images/peppers.png',1)
kernel1 = np.array([[0,-1,0],
                    [-1,5,-1],
                    [0,-1,0]])

I2 = cv2.filter2D(I,-1,kernel1)
I3 = np.concatenate((I,I2), axis=1)
I4 = np.uint8(np.float32(I)+0.1*np.float32(I-I2))

cv2.imshow('I3',I3)
cv2.imshow('I4',I4)
cv2.waitKey()
cv2.destroyAllWindows()