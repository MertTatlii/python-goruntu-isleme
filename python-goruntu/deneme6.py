import time

import cv2
import numpy as np
import pylab as pl
from matplotlib import pyplot as plt

'''
I=cv2.imread('images/peppers.png',-1)
#slayttaki turkuaz sorusu 
I2=(I[:,:,0]>220) &(I[:,:,1]>220)&(I[:,:,2]>220) #bgr sırasıyla 220den büyükleri bool yapar true-false
print('I2 dtype: ',I2.dtype)
I3=np.uint8(I2)*255 #0-1 e dönüştürdüğü için *255 yazdık

I4=cv2.morphologyEx(I3,cv2.MORPH_OPEN,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))) #I3 üstünden açınım işlemi yaptık.
print('I4 dtype: ',I4.dtype)

indis=np.bool_(I4) #I4 uint8 den bool a çevirdik
Inew=I.copy()
Inew[indis,0]=200
Inew[indis,1]=214
Inew[indis,2]=48

cv2.imshow('I',I)
cv2.imshow('I3',I3)
cv2.imshow('I4',I4)
cv2.imshow('Inew',Inew)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
#ETİKETLEME :birbirine değen nesneler üzerinde işlem yapar!! 0 arkaplan sayılır istediğin yer için +1 ekle
I= cv2.imread('images/coins_filled.jpg',0)
th,I2=cv2.threshold(I,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) #gri renkli görüntüyü siyah-beyaz a çevirdik.
print('threhold değeri: ',th)

count,I3,stats,xy=cv2.connectedComponentsWithStats(I2)
print('daire sayısı: ',count-1) #0 olan arka planı da dahil ediyor o yüzden daire sayısını hesaplayabilmek için -1 yapmalısın etietlerde +1 yapmalısın
print(I3.dtype)
print(I3.shape)
print('stats: ',stats)
print('koordinat: ',xy)

cv2.imshow('I',I)
cv2.imshow('I2',I2)
cv2.imshow('1. para',np.uint8(I3==1)*255) #sağdan sola doğru sayıyor sırayla
cv2.imshow('2. para',np.uint8(I3==2)*255)
cv2.waitKey(0)
cv2.destroyAllWindows()

# #ANİMASYONLU YAPMA
# for i in range(1,count):
#     cv2.imshow('para',np.uint8(I3==i)*255)
#     cv2.waitKeyEx(1000)
'''

'''
#KENAR BULMA: 1.türevin tepe noktaları kenarları verir, 2.türev kenarın yönünü verir!! Kenarlar türevin uç noktalarına gelir
#1.türevi aldığında sobel operatörünü de hesaplamış olursun.
I=cv2.imread('images/blobs.jpg',0)
I2=cv2.bitwise_not(I) #beyazın üstünde siyah olduğu için siyah beyaza çevirmem gerekiyor. arkaplana bakmak istemiyorum
print(I2.dtype)
tt,I2=cv2.threshold(I2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

I3=cv2.Sobel(I2,ddepth=-1,dx=1,dy=0,ksize=5) #ksize= aradaki değişime bakıyor hassaslık ne kadar önemliyse ona göre sayı verirsin.
I4=cv2.Sobel(I2,ddepth=-1,dx=0,dy=1,ksize=5)
I5=cv2.Sobel(I2,ddepth=-1,dx=1,dy=1,ksize=5)

cv2.imshow('I',I)
cv2.imshow('I2',I2)
cv2.imshow('I3',I3)
cv2.imshow('I4',I4)
cv2.imshow('I5',I5)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''

I=cv2.imread('images/blobs.jpg',0)
I2=cv2.bitwise_not(I) #beyazın üstünde siyah olduğu için siyah beyaza çevirmem gerekiyor. arkaplana bakmak istemiyorum

I3 = cv2.Canny(I2,threshold1=200, threshold2=100)

cv2.imshow('I2',I2)
cv2.imshow('I3',I3)
cv2.waitKey()
cv2.destroyAllWindows()
'''


I = cv2.imread('images/coins.png',0)
th_value, I2 = cv2.threshold(I,127,255,cv2.THRESH_BINARY)
mask = np.zeros((I2.shape[0]+2,I2.shape[1]+2), dtype=np.uint8)

I4 = I2.copy()
cv2.floodFill(I4, mask, (0,0), 255)
I5 = cv2.bitwise_not(I4)
I6 = I5 | I2


sayi, I7, stats, merkez = cv2.connectedComponentsWithStats(I6)
#------------------------------------------------------------------------------------------------------------------------------------------
#Burda centrid ile yarıçap hesaplatma sorabailir hoca finalde
#------------------------------------------------------------------------------------------------------------------------------------------

enbuyuk_label = (np.argmax(stats[1:, -1])+1)
I8 = I7 == enbuyuk_label
I8 = np.uint8(I8)*255

I9 = cv2.Canny(I8, threshold1=100, threshold2=200)
I9_ind = np.bool_(I9)
I_bgr = np.zeros((I.shape[0],I.shape[1],3), dtype=np.uint8)

I_bgr[:, :, 0]= I
I_bgr[:, :, 1]= I
I_bgr[:, :, 2]= I

I_bgr[I9_ind,0]= 0
I_bgr[I9_ind,1]= 0
I_bgr[I9_ind,2]= 255





cv2.imshow('I',I)
cv2.imshow('I2',I2)
cv2.imshow('I5',I5)
cv2.imshow('I4',I4)
cv2.imshow('I6',I6)
cv2.imshow('I8', np.uint8(I8)*255)
cv2.imshow('I9', I9)
cv2.imshow('I_BGR', I_bgr)
cv2.waitKey()
cv2.destroyAllWindows()