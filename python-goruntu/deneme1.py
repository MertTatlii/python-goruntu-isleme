import cv2
import numpy as np
from matplotlib import pyplot as plt

print(cv2._version_)

I=cv2.imread('images/peppers.png',1)

print(type(I))
print(I.shape)
print(I.dtype)
print(I.ndim)

# cv2.imshow('aa',I)
# cv2.imshow('aa2',I)
# cv2.waitKey(0) #ben tuşa bastığımda görüntü kapanacak 0 yazdığım için içine 100 yazsaydım 100 sn sonra kendiliğinden kapanırdı.
# cv2.destroyAllWindows() #tüm açık pencerelerin hepsini kapatıyor.

print()

print(I[50,50,:]) #I nın 50.satır 50.sütununu gösterir. bunlar sırayla R,G,B yi verir. 0:B 1:G 2:R opencvde bgr olarak gider
# print(I[50,50,2]) #sadece R'ı getirir kırmızıyı

# I[50,50,:]=[255,255,255] #0:siyah 255:beyaz

# cv2.imshow('aa2',I)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

print()

I2=I[50:54,50:54,:]
print(I2.shape) #(4,4,3)

# I[50:54,50:54,:]=np.ones((4,4,3))*255 #yukarıdaki küçük beyaz kareyi büyülttük
# cv2.imshow('aa3',I)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

print()

I3=np.array([[255,188,120,55],[0,88,178,255],[255,0,255,0],[0,255,0,255]],dtype=np.uint8) #ilk satır beyazdan siyaha gider, 2.satır siyahtan beyaza
# cv2.imshow('aa4',I3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

print()

#görüntüyü matplotlibde göstermek için bgr ı rgb'ye dönüştürmem lazım !!


Ib=I[:,:,0].copy() #[:,:,0] = B
Ig=I[:,:,1].copy() #[:,:,0] = G
Ir=I[:,:,2].copy() #[:,:,0] = R

Inew=np.zeros((384,512,3),dtype=np.uint8) #boş matris oluşturdum sipsiyah bir resim görürüm ama aslında bu renkli bir resimdir.!!!
#rgb yaptım Inew'i
Inew[:,:,0]=Ir
Inew[:,:,1]=Ig
Inew[:,:,2]=Ib

# plt.imshow(Inew)
# plt.waitforbuttonpress()
# plt.close()

# plt.imshow(Ib,cmap='Greys',interpolation='nearest') #mavi yoğunluklu yerleri siyah gösteriyor.
# plt.waitforbuttonpress()
# plt.close()

# plt.imshow(Ir,cmap='Greys',interpolation='nearest') #kırmızı yoğunluklu yerleri siyah gösteriyor.
# plt.waitforbuttonpress()
# plt.close()

print()

IIb,IIg,IIr=cv2.split(I) #I görüntüsünü split yapıp parçaladık ve atadık sol taraftakilere bgr
Inew2=cv2.merge((IIr,IIg,IIb)) #bu parçaları rgb olarak birleştirdim. resim yeniden oluşturuluyor.

# plt.imshow(Inew2)
# plt.waitforbuttonpress()
# plt.close()

# cv2.imshow('IIg',IIg) #sadece yeşil i gösteriyorum ekranda Gri tonaja döner.
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# I3=cv2.cvtColor(I,cv2.COLOR_BGR2RGB) #I orijinal bgr görüntüyü başka renge çevireceğim yukarıdaki yaptığımızın kodu kısa kodu rgbye çevirdik
I4=cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
I5=cv2.imread('images/peppers.png',0)

# cv2.imshow('I4',I4) #ikisi de aynı olur I4 VE I5
# cv2.imshow('I5',I5) #ikisi de aynı olur I4 VE I5
# cv2.waitKey(0)
# cv2.destroyAllWindows()

I6=cv2.cvtColor(I,cv2.COLOR_BGR2HSV) #HSV 'ye çevirdik bgr'ı
# cv2.imshow('Orj',I)
# cv2.imshow('I6',I6)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# cv2.imwrite('hsv_image.tif',I6) #hsv li görüntüyü kaydettik.


# I8=I #I8 değişince I da değişiyor heap mantığı I'yı da değiştiriyorum.
I8=I.copy() #I orj durur I8 yeşil olur
cv2.line(I8,(250,80),(450,80),(0,255,0),thickness=3) #bgr g yi 255 yaptığından yeşil çizecek thickness=3 kalınlık
# cv2.imshow('I8',I8)
# cv2.imshow('I',I)
# cv2.waitKey(0)
# cv2.destroyAllWindows()