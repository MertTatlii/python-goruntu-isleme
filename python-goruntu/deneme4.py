import cv2
import numpy as np
from matplotlib import pyplot as plt

I=cv2.imread('images/peppers.png',1)
print(I.shape)

M=np.array([[2,0,0],[0,0.5,0]],dtype=np.float32) #width 2 kat artacak height ise 0.5 kat

height,width=I.shape[0:2] #0'ı height a 1'i width e atadım.

I2=cv2.warpAffine(I,M,(width*2,height//2)) #None yazdığında resmi kırpıyor (width*2,height/2) bunu yazarsan tüm görüntü geliyor. width'i 2 katına çıkardığım için 2 ile çarptım height'ı da yarıya indirdim diye böldüm 0.5 ile de çarpabilirdin.
print(I2.shape)


#ÖTELEME
M2=np.array([[1,0,100],[0,1,50]],dtype=np.float32) #görüntü 100 birim sağa 50 birim aşağı kayacak
I3=cv2.warpAffine(I,M2,None)

#KONTRAST
I4=cv2.imread('images/cameraman.tif',-1) #-1 görüntüye müdahele etmiyor.
print(I4.shape)#0-255 arası gri tonlu üstü renkli tonlu
print(I4.dtype)

# I5=I4+50 #+ yaparsan renk açılır - de renk koyulaşır.
# I6=I4-50 #koyulaşacaktı ama uint8 ile hesap yaptığımız için sıkıntı çıkıyor.

#Yukarıdaki hatayı ortadan kaldırmak için yapıyorum!!
I5=np.int16(I4)+50
I6=np.int16(I4)-50

#min-max-ort yazdırdık
print('I4 min',np.min(I4))
print('I4 max',np.max(I4))
print('I4 mean',np.mean(I4))
print()
print('I5 min',np.min(I5))
print('I5 max',np.max(I5))
print('I5 mean',np.mean(I5))
print()
print('I6 min',np.min(I6))
print('I6 max',np.max(I6))
print('I6 mean',np.mean(I6))

I5[I5>255]=255
I5[I5<0]=0

I6[I6>255]=255
I6[I6<0]=0

#yukarıdaki işlemlerden sonra değişikliği göstermek için yazdık aşağıdakini
# print('I4 min',np.min(I4))
# print('I4 max',np.max(I4))
# print('I4 mean',np.mean(I4))
# print()
# print('I5 min',np.min(I5))
# print('I5 max',np.max(I5))
# print('I5 mean',np.mean(I5))
# print()
# print('I6 min',np.min(I6))
# print('I6 max',np.max(I6))
# print('I6 mean',np.mean(I6))

I5=np.uint8(I5) #görüntüyü gösterebilmek için yeniden uint8'e çeviriyoruz. UNUTMA!!
I6=np.uint8(I6)

#önemli bir şey değil
# hh=np.array([255],dtype=np.uint8)
# print(hh)
# hh=hh+1
# print(hh)

IN=255-I4 #negatif alma

#HİSTOGRAM
IH=cv2.calcHist([I4],[0],None,[256],(0,256))
# plt.plot(IH,'r')
# plt.waitforbuttonpress()
# plt.close()

# plt.hist(I4.flat,256,(0,256)) #tek vektör şelinde vermem lazım. tek boyuta indirgedi: reshape(-1)
# plt.waitforbuttonpress()
# plt.close()

#bgr çizdirme
I7_orj=cv2.imread('images/peppers.png',1)
color=('b','g','r')

for i,renk in enumerate(color):
    I8=cv2.calcHist([I7_orj],[i],None,[256],(0,256))
    plt.plot(I8, color=renk)

plt.waitforbuttonpress()
plt.close()

cv2.imshow('I',I)
cv2.imshow('I2',I2)
# cv2.imshow('I3',I3)
# cv2.imshow('I4',I4)
# cv2.imshow('I5',I5)
# cv2.imshow('I6',I6)
# cv2.imshow('IN',IN)
# cv2.imshow('I7_orj',I7_orj)
cv2.waitKey(0)
cv2.destroyAllWindows()