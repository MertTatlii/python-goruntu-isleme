import cv2
import numpy as np

I=cv2.imread('images/fig1.jpg',-1) #-1 koyarsan rengine dokunmazsın neyse o gelir. 0 gri tonlu yapar
I3_orj=cv2.imread('images/circles.png',0) #0 koydum gri gelcek

se=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(35,35)) #(35,35):BOYUTUNU GİRDİK
se2=np.array([[0,0,0,0,0],[1,1,1,1,1],[0,0,0,0,0]],dtype=np.uint8) #uint8 : görüntü gelmesi için bunu yazıyorum.
print(se.shape)
print(se.dtype)
print(se)

#AŞINMA YAPIYORUM hem sayı hem koordinatını bulabilirim, gürültüyü temizliyorum.GÖRÜNTÜNÜN BOYUTU DEĞİŞİR
I2=cv2.erode(I,se) #(35,35) filtreleme yaptım.
# I2=cv2.erode(I,se2)

#deliting yapıyorum GÖRÜNTÜNÜN BOYUTU DEĞİŞİR
I4=cv2.dilate(I3_orj,se)

#opening yapıyorum GÖRÜNTÜNÜN BOYUTU DEĞİŞMEZ
I5=cv2.morphologyEx(I,cv2.MORPH_OPEN,se)

#closing yapıyorum GÖRÜNTÜNÜN BOYUTU DEĞİŞMEZ
I6=cv2.morphologyEx(I3_orj,cv2.MORPH_CLOSE,se)

#closing önce dilate sonra erode yapar bunun kontrolünü yapıyoruz.
I7_kntrl1=cv2.morphologyEx(I3_orj,cv2.MORPH_DILATE,se)
I7_kntrl2=cv2.erode(I7_kntrl1,se)

print(np.sum(np.sum(I6-I7_kntrl2))) #sonuç 0 çıkıyor aynı boyut olduğunu gördük.

# cv2.imshow('se',se*255) #*255 in sebebi bunu yazmazsak göremiyoruz 0-1 arasındaki renkleri anlayamıyoruz 255 ile çarptık o yüzden
cv2.imshow('Orj',I)
# cv2.imshow('I2',I2)
cv2.imshow('OrjI3',I3_orj)
# cv2.imshow('I4',I4)
# cv2.imshow('I5',I5)
cv2.imshow('I6',I6)

cv2.imshow('I7_kntrl',I7_kntrl2)

cv2.waitKey(0)
cv2.destroyAllWindows()