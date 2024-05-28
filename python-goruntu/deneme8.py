import cv2
import numpy as np
import pylab as pl
from matplotlib import pyplot as plt

I = cv2.imread('images/peppers.png', 1)

I2 = cv2.blur(I, (5,5))

kernel1 = np.ones((5,5), np.float32)*(1/25)
I3 = cv2.filter2D(I, -1, kernel1)

np.sum(np.abs(I2-I3))
print(np.sum(np.abs(I2-I3))) #I3 ile I2 aynı mı kontrol ettik

I4 = cv2.GaussianBlur(I, ksize=(5,5), sigmaX=0, sigmaY=0)


cv2.imshow('I', I)
cv2.imshow('I2', I2)
cv2.imshow('I3', I3)
cv2.imshow('I4', I4)
cv2.waitKey()
cv2.destroyAllWindows()