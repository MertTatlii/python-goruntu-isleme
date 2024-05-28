import cv2
import numpy as np
import numpy as np7
import  pylab as pl
from matplotlib import pyplot as plt

I=cv2.imread('images/peppers.png',0)
I_histeq=cv2.equalizeHist(I) #HİSTOGRAM EŞİTLEME

#CLAHE HİSTOGRAM EŞİTLEME
clahe1=cv2.createCLAHE(2,(8,8)) #range girerken parantez içine alırsın
I_clahe=clahe1.apply(I)

#GÖRÜNTÜ EŞİKLEME (S-B (ikili,binary,)YAPARSIN GRİ TONLU GÖRÜNTÜYÜ)
I2=cv2.imread('images/threshold.jpg',0) #0 griye çevirdim -1 koyup shape ine bak boyut gidiyo
print(I2.shape)

tvalue1,I3=cv2.threshold(I2,3,255,cv2.THRESH_BINARY) #eşitliğin solunu böyle yazmayı UNUTMA!!!! tvalue1 i yazmazsan direkt I3 yazarsan thresvalue gözükür ekranda
tvalue2,I4=cv2.threshold(I2,127,255,cv2.THRESH_BINARY)
tvalue3,I5=cv2.threshold(I2,240,127,cv2.THRESH_BINARY) #240 tan büyükleri 127 renk tonu yaptık gri 255 yazarsan beyaz olur.

print('Threshold value: ',tvalue1)
print('Threshold value: ',tvalue2)
print('Threshold value: ',tvalue3)

#OTSU EŞİKLEME
tvalue4,I6=cv2.threshold(I2,240,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print('Threshold value: ',tvalue4)

#BOŞLUKLARI DOLDURMA
I7=cv2.imread('images/coins.png',0)
th,I8=cv2.threshold(I7,127,255,cv2.THRESH_BINARY) #siyah beyaz yaptık I7'yi
I9=I8.copy()
maske=np.zeros((I9.shape[0]+2,I9.shape[1]+2),np.uint8) #+2 eklememizin sebebi pikselleri eşitlemek sağdan soldan üstten aşağıdan.
cv2.floodFill(I9,maske,(0,0),255) #(0,0) arka plandan aldığım yer 255 orayı 255 yapıcam
I10=cv2.bitwise_not(I9) #I9 un tersini aldık
I11=I8|I10 #I8 ve I10 u or'ladık
I12=cv2.bitwise_or(I8,I10) # YUKARIDAKİYLE AYNI ŞEY

I13=np.bool_(I12) #içi dolu yerler bana doğrudan indis bilgisiyle gelecek. bool ile çevirdim.
# I7[I13]=127 #burası

#KOORDİNAT ELDE ETME
I14=cv2.morphologyEx(I10,cv2.MORPH_CLOSE,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(15,15))) #içini doldurdum
I15=cv2.morphologyEx(I14,cv2.MORPH_OPEN,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))) #etraftaki küçük şeyler de gitti sadece nesnem aldı etrafta
xy=np.column_stack(np.where(I15>0)) #
I16=I7[np.min(xy[:,0]):np.max(xy[:,0])+1,np.min(xy[:,1]):np.max(xy[:,1])+1] #sonu dahil olmadığı için +1 yazıyoruz ekleyebilmek için dahil olsun diye
I17=I7[np.min(xy[:,0])-3:np.max(xy[:,0])+4,np.min(xy[:,1])-3:np.max(xy[:,1])+4]


# cv2.imshow('I',I)
# cv2.imshow('I_histogram',I_histeq)
# cv2.imshow('I_clahe',I_clahe)
# cv2.imshow('I2',I2)
# cv2.imshow('I3 Thres:3',I3)
# cv2.imshow('I4 Thres:127',I4)
# cv2.imshow('I5 Thres:240',I5)
# # cv2.imshow('I6 Thres OTSU',I6)
cv2.imshow('I7',I7)
# cv2.imshow('I8',I8)
# cv2.imshow('I9',I9)
# cv2.imshow('I10',I10)
# cv2.imshow('I11',I11)
# cv2.imshow('I7',I7) #burası
# cv2.imshow('I14',I14)
cv2.imshow('I15',I15)
cv2.imshow('I16',I16)
cv2.imshow('I17',I17)

cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.hist(I.flat,100,(0,255)) #flat : düzleştiriyor. bunda düzleştirmek gerekir
# # plt.hist(I_histeq.flat,100,(0,255))
# plt.hist(I_clahe.flat,100,(0,255))
# plt.waitforbuttonpress()
# plt.close()

aa=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(aa)
bb=aa!=5
print(bb)
print(bb.dtype)
aa[bb]=88
print(aa)

cc=np.array([1,2,1,0,6,0,1,0]) #0'lar false geri hepsi true olur!!
print(np.bool_(cc))