#lowfilter
import cv2
import numpy as np
import pylab as pl
from matplotlib import pyplot as plt

I = cv2.imread('images/peppers.png')
I2 = I.copy()


prob = 0.05
rnd1 = np.random.random(I.shape[0:2])
I2[rnd1<(prob/2)]= 0
I2[rnd1> 1-(prob/2)]= 255
I3 = cv2.medianBlur(I2,3)


I_circle = cv2.imread('images/circles.png')
I2_circle = I_circle.copy()
noise2 = np.random.random(I2_circle.shape[0:2])
I2_circle[noise2<(prob/2)]= 0
I2_circle[noise2> 1-(prob/2)]= 255

I3_circle = cv2.medianBlur(I2_circle,3)


Ibilateral = cv2.bilateralFilter(I2, 7, sigmaColor=75, sigmaSpace=75)
I_circlebilateral = cv2.bilateralFilter(I2_circle, 7, sigmaColor=75, sigmaSpace=75)



cv2.imshow('I', I)
cv2.imshow('Salt and Pepper noise', I2)
cv2.imshow('I3 median blur', I3)
cv2.imshow('I bilateral', Ibilateral)

cv2.imshow('I_circle', I_circle)
cv2.imshow('I2_circle', I2_circle)
cv2.imshow('I3_circle median blur', I3_circle)
cv2.imshow('I_ circle bilateral', I_circlebilateral)

cv2.waitKey()
cv2.destroyAllWindows()