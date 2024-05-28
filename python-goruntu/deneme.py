import cv2
import matplotlib as plt
import numpy as np

I=cv2.imread('images/peppers.png',1)
height, width = I.shape[:2]
center = (height/2,width/2)


# rotatematrix =cv2.getRotationMatrix2D(center=center, angle=45, scale=1)
# rotated_image = cv2.warpAffine(I,rotatematrix,(width,height))


input_pts = np.float32([
    [0,0],
    [width-1,0],
    [0,height-1]
])
output_pts = np.float32([
    [0,height-1],
    [width-1,height-1],
    [0,0]
])
M = cv2.getAffineTransform(input_pts,output_pts)
print(M)
new_image = cv2.warpAffine(I,M,(width,height))

cv2.imshow('orj', I)
cv2.imshow('rotatedaffine',new_image)
# cv2.imshow('rotated', rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()