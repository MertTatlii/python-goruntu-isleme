import cv2
import numpy as np

I=cv2.imread('images/peppers.png',1)
print(I.shape)

#Boyut değiştiriyorum:
# I2=cv2.resize(I,(100,255)) #widht,height orj bilgiler yok olur.
I2=cv2.resize(I,(50,38),interpolation=cv2.INTER_CUBIC) #5000,3800 yazıp küçültsen çok da bir bozulma yaşamıyorsun. interpolation=cv2.INTER_CUBIC 16lık hesaplar
print(I2.shape) #255,100 gelir farkı unutma yukarıdakiyle matris karşılığı bu gelen. ters yazıyorsun!

I3=cv2.resize(I2,(512,384)) #görüntü bozuldu I2 üzerinde işlem yaptık bilgiler yok olduğu için bulanıklaştı.

#ölçek kullanarak boyut değiştirme
I4=cv2.resize(I,None,fx=1.5,fy=0.5) #fx:width, fy:height

#Kırpma
I5=I[120:170,380:430] #height,width olur matris gibi
print(I5.shape)
print(I5.dtype)

I6=I[280:330,440:490]

# I[280:330,440:490]=I[120:170,380:430] #I5 ten elde ettiğim görüntüyü I6da elde ettiğim yere atadım.

print()

#Affine
M1=cv2.getRotationMatrix2D((I.shape[1]//2,I.shape[0]//2),45,1) #width,height giriyorsun!! I.shape[1]:sütun, shape[0]:satır, // virgülü atar. GAÖRÜNTÜNÜN ORTASINDAN SAAT YÖNÜ TERSİNDE 45 DERECE DÖNDÜRME. -45 yazarsan saat yönünde döndürür.
print(M1)

print()

test1=np.array([[np.cos(np.pi/4),np.sin(np.pi/4)],[-np.sin(np.pi/4),np.cos(np.pi/4)]]) #np.pi/4 45 derece radyan olduğu için böyle yazdık
print(test1)

I7=cv2.warpAffine(I,M1,None)

print()

#Aynalama yapıyorum. Xekseninde simetri aldım gibi. slayttaki görselin kodu
height,width=I.shape[:2]
pts1=np.array([[0,0],[width-1,0],[0,height-1]],dtype=np.float32)
pts2=np.array([[width-1,0],[0,0],[width-1,height-1]],dtype=np.float32)

M2=cv2.getAffineTransform(pts1,pts2)
print(M2)

I8=cv2.warpAffine(I,M2,None)


cv2.imshow('Orj',I)
# cv2.imshow('I2',I2)
# cv2.imshow('I3',I3)
# cv2.imshow('I4',I4)
# cv2.imshow('I5',I5)
# cv2.imshow('I6',I6)
# cv2.imshow('I7',I7)
cv2.imshow('I8',I8)
cv2.waitKey(0)
cv2.destroyAllWindows()
# döndürme formül sınavda çıkabilir
