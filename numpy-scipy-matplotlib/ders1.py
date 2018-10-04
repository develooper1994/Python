import numpy as np
from numpy import *
import matplotlib.pyplot as p
from matplotlib.pyplot import *
import os, time
import cv2

'''
script non-interactive moddur ve ona göre çalışmak gerekir. mesela show() en sona konmalı
merak ettiğiniz bir fonksiyonu sonuna soru işareti koyarak bulabilirsiniz.
'''

print("np.__version__= ", np.__version__)
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print("Bu bir liste birleşmesidir.", "a= ", a);
print("b= ", b);
print("c= ", c)

a = array([1, 2, 3])
b = array([4, 5, 6])
c = a + b
print("Bu bir vektör toplamıdır.", "a= ", a);
print("b= ", b);
print("c= ", c)
# HATA 3 ELEMANLIYLA 4 ELEMANLI TOPANANMAZ! VEYA ONUN GİBİ BİRŞEY
'''
a=array([1,2,3,4])
b=array([4,5,6])
c=a+b
print("Bu bir vektör toplamıdır.","a= ",a); print("b= ",b); print("c= ",c)
'''
# İKİ BOYUTLU
a = array([[1, 2, 3], [4, 5, 6]])
b = array([[4, 5, 6], [7, 8, 9]])
c = a + b
print("Bu bir vektör toplamıdır.", "a= ", a);
print("b= ", b);
print("c= ", c)
# HATA 3 ELEMANLIYLA 4 ELEMANLI TOPANANMAZ! VEYA ONUN GİBİ BİRŞEY
'''
#İKİ BOYUTLU
a=array([[1,2,3],[4,5,6]])
b=array([[4,5,6],[7,8,9]])
c=a+b
print("Bu bir vektör toplamıdır.","a= ",a); print("b= ",b); print("c= ",c)
'''

# arange örneği
a = arange(21) * 2 * pi / 21
print("arange(21)*2*pi/21= ", a)
b = sin(a)
# çizdir
# ion() #toogle mantığıyla çalışır. hemen grafik yenilensin mi yenilenmesin mi?
# tüm veriler işlendikten sonra grafik çizdirmek istersen diye
p.plot(a, b)
p.show()
time.sleep(1)
p.close()
b *= a

print("arange(21)*2*pi/21= ", a)
p.plot(a, b, "y*")
p.show()
time.sleep(1)
p.close()
