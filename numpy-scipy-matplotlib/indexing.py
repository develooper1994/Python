from numpy import *
from matplotlib.pyplot import *
import os
sil=lambda :os.system('cls')
#numpy ile daha iyi index işlemleri
a=arange(0,80,2)
print('arange(0,80,10)=',a,'\n')
asize=a.size
a.shape = asize/5,asize/8
#a.shape=(-1,-1)  #bu bir fanteziydi :) ve hata veriyor.
print('a.shape = asize/5,asize/8=\n',a,'\n')
a=reshape(a,(5,4,2))
print('a.reshape((5,4,2))=\n',a,'\n')
a=reshape(a,a.size)
print('a=reshape(a,a.size)=\n',a,'\n')


#şimdi başlıyoruz.
a=reshape(a,(5,-1))
mask=a>=50
print('a[mask]=\n',a[mask])
indices=[0,1,-1]
print('a.ndim=2 , a[indices]=\n',a[indices])
a=reshape(a,a.size)
indices=[0,1,-1,-3,3]
print('a.ndim=1 , a[indices]=\n',a[indices])


# indexlemeyi biraz daha ileri götürelim.
a=arange(56)
a=a.reshape((-1,7)) #self olarak fonksiyon kullanımı.
print('arange(56)=',a,'\n')
print('a[(0,1,2,3,4),(1,2,3,4,5)]= ',a[(0,1,2,3,4),(1,2,3,4,5)])
print(' sağ taraf a.diagonal(1)=',a.diagonal(1),'sol taraf a.diagonal(-1)=',a.diagonal(-1),'orta a.diagonal(0)=',a.diagonal(0))
print('a[3:,[0,2,5]]= ',a[3:,[0,2,5]])
#şarta bağlı indexing
mask=array([1,0,1,0,0,1,0,0],dtype=bool) #[1,0,1,0,0,1] sadece böyle derseniz işlemi yapar sadece bir uyarı verir.
print('a[mask,2]= ',a[mask,2])
print('a[:3]= \n',a[:3],'\n')
print('a[2::2,::2]= \n',a[2::2,::2],'\n')

a=array([0,12,5,20])
loc=where(a>10) # 10dan büyük elemanların yerleri. bu fonksiyon maalesef tuple üretir.
print('tuple where(a>10)= \n',loc,'\n') # parantezleri ve virgülleri görüyorsunuz.
print('where(a>10)[0]= \n',loc[0],'\n')
print('a[loc]= ',a[loc],'\n')
#diyelimki 10dan büyük kaç tane var öğrenmek istiyorsunuz.
mask=a>10
print('diyelimki 10dan büyük kaç tane var öğrenmek istiyorsunuz= ',sum(mask),'\n')


# diyelimki iki vektörleri alt alta eklemek istiyoruz.
#listelerde [:-1.1:-1] gibi birşey yapamazsınız, [:-1][1:-1] boş liste verir.
#numpy array kullanın.
b=array([5,9,6,2])
c2=[a,b]
print('[a,b][0][1:-1]=\n',c2[0][1:-1],'\n') #[a,b][0][1:-1] olarak da yazabilirsiniz.
c1=array([a,b])
print('c1=',c1,'\n')


#diyelimki iki vektörleri yan yana eklemek istiyoruz.
#çok ilkel bir yol.
print('array([list(a)+list(b)])= \n',array([list(a)+list(b)]),'\n')
print('hstack(b)= ',hstack((a,b)),'\n')
print('vstack(b)= \n',vstack((a,b)),'\n')
#diyelimki bunlar iki tane 2 boyutlu(tek kanallı) resim olsun.
# bu sayede opencvdeki ürettiğimiz resimleri yanyana birleştirebiliriz.
a=array([[0,0,255,0,0],[0,0,0,255,0],[0,0,0,0,255],[255,0,0,0,0],[0,255,0,0,0]])
b=array([[2,0,2,0,0],[0,2,0,2,0],[0,0,2,0,2],[2,0,0,2,0],[0,2,0,2,0]])
print('hstack(b)= \n',hstack((a,b)),'\n')
print('vstack(b)= \n',vstack((a,b)),'\n')
#diğer şekilde...
print('concatenate((a, b), axis=0)= \n',concatenate((a, b), axis=0),'\n')
print('concatenate((a, b), axis=1)= \n',concatenate((a, b), axis=1),'\n')


#bazı istatislik hesapları
#nansum. sum olsa nan verecek burada nan değerlerini ihmal ediyor.
a=array([[1,1,nan],[5,nan,nan]])
print('nansum(a)= ',nansum(a))
print('nansum(a,axis=0)= \n',nansum(a,axis=0))
print('nansum(a,axis=1)= \n',nansum(a,axis=1))
a=array([[2,6,8],[5,4,7]])
#axis=0 aşağı doğru yani herbir satır
#axis=1 sağa doğru yani her bir sütun
print('sum(a)= ',sum(a))
print('sum(a,axis=0)= \n',sum(a,axis=0))
print('sum(a,axis=1)= \n',sum(a,axis=1))
print('a.sum()= ',a.sum())
print('a.sum(axis=0)= \n',a.sum(axis=0))
print('a.sum(axis=1)= \n',a.sum(axis=1),'\n')
print('cumsum(a)= \n',cumsum(a))
print('a.cumsum()= \n',a.cumsum())
print('a.cumsum(axis=0)= \n',a.cumsum(axis=0))
print('a.cumsum(axis=1)= \n',a.cumsum(axis=1),'\n')
#difference
#diff(a)= [[6-2, 8-6], [4-5, 7-4]]
print('diff(a)= ',diff(a))
#diff(a,axis=0)= [[5-3, 4-6, 7-8]]
print('diff(a,axis=0)= \n',diff(a,axis=0))
#diff(a,axis=1)= [[6-2, 8-6], [4-5, 7-4]]
print('diff(a,axis=1)= \n',diff(a,axis=1))
#prod
print('a.prod(axis=0)= \n',a.prod(axis=0))
print('prod(a)= ',prod(a),'\n')
#cumprod
print('cumprod(a)= \n',cumprod(a))
print('a.cumprod()= \n',a.cumprod())
print('a.cumprod(axis=0)= \n',a.cumprod(axis=0))
print('a.cumprod(axis=1)= \n',a.cumprod(axis=1),'\n')
#average
print('average(a)= ',average(a))
#varyans
print('var(a)= ',var(a))
print('a.var()= ',a.var())
#gradient
'''
The gradient is computed using central differences in the interior and first differences at the boundaries.
and

The default distance is 1
This means that in the interior it is computed as
dirach[f](x)=f(x+h*1/2)-f(x-h*1/2)
where h = 1.0
deltah[f](x)=f(x+h)-f(x)
and at the boundaries
-----------------------------------------------------------------------------------
Also in the documentation:
>>> x = np.array([1, 2, 4, 7, 11, 16], dtype=np.float)
>>> np.gradient(x)
array([ 1. ,  1.5,  2.5,  3.5,  4.5,  5. ])
So, the gradient between the points in the array (assumes a y delta of 1) is:

1-2: 1
1-3: 1.5 (4-1)/2
2-4: 2.5 (7-2)/2
3-5: 3.4 (11-4)/2
etc...
You could find the minima of all the absolute
values in the resulting array to find the turning points of a curve, for example.
'''
x = np.array([0, 1, 2, 3, 4])
dx=gradient(x)
y=x**2
print('gradient(y,dx,edge_order=0)= ',gradient(y,dx,edge_order=0))
print('gradient(y,dx,edge_order=1)= ',gradient(y,dx,edge_order=1))
print('gradient(y,dx,edge_order=2)= ',gradient(y,dx,edge_order=2))

#crosproduct vectörlerin çapraz çarpımı dik bir vektör oluşturuyordu.
x=[1,2,3]; y=[4,5,6]
print('cross(x,y)= ',cross(x,y))
#trapz kuralı. grafiğin integralini alırken kullanılır ve örnekleme yoluyla
#integral aldığından hata payı vardır. scipy.imtegrate içindeki quad daha iyidir.
'''
quad kullanımı
from scipy.integrate import quad
ans, err = quad(lambda x: x**3, 0, 2)
print (ans)
---------------------VEYA------------------------
from scipy.integrate import quad
def integrand(x):
    return x**3
ans, err = quad(integrand, 0, 2)
print (ans)
'''
#varsayılan olarak dx=1dir.
#https://en.wikipedia.org/wiki/Trapezoidal_rule      linkinden bakabilirsiniz.
#canlandırması da: https://en.wikipedia.org/wiki/File:Composite_trapezoidal_rule_illustration.png
'''
def abs_trapz(y, x=None, dx=1.0):
    y = np.asanyarray(y)
    if x is None:
        d = dx
    else:
        x = np.asanyarray(x)
        d = np.diff(x)
    ret = (d * (y[1:] +y[:-1]) / 2.0)
    return ret[ret>0].sum()  #The important line

'''


print('trapz([1,2,3])= ',trapz([1,2,3]))
print('trapz([1,2,3], dx=-1)= ',trapz([1,2,3], dx=-1))
print('trapz([1,2,3], dx=0)= ',trapz([1,2,3], dx=0))
print('trapz([1,2,3], dx=1)= ',trapz([1,2,3], dx=1))
print('trapz([1,2,3], dx=2)= ',trapz([1,2,3], dx=2))
print('trapz([1,2,3], dx=3)= ',trapz([1,2,3], dx=3),'\n')

print('trapz([1,2,3,4,5,6])= ',trapz([1,2,3,4,5,6]))
print('trapz([1,2,3,4,5,6], axis=-1)= ',trapz([1,2,3,4,5,6], axis=-1))
print('trapz([1,2,3,4,5,6], axis=0)= ',trapz([1,2,3,4,5,6], axis=0))



#convolution
#bir fonksiyon diğerinin üzerinden kayarak toplanıyor. bu yüzden iki parametresi zorunludur.
#çok boyutlu diziler için conv2 ve conv3 gibi fonksiyonlar mevcut
#scipy üzerinde ve opencv üzerinde convolution filtreler var.
#bilgisayardaki yapılabilecek en iyi işlem diyebiliriz.
#convolve(a,v)=[inf->inf][a[m]*v[n-m]]
print('convolve([1,2,3],[4,5,6])= ',convolve([1,2,3],[4,5,6]))
#en ortadaki değeri döndürür. kenarlardakileri boş verir.
print("""convolve([1,2,3],[0,1,0.5], 'valid')= """,convolve([1,2,3],[0,1,0.5], 'valid'))
#ortadaki değerleri döndürür. kenarlardakileri boş verir.
print("""convolve([1,2,3],[0,1,0.5], 'same')= """,convolve([1,2,3],[0,1,0.5], 'same'))










a=linspace(0,2*pi,21)# başlangıç,bitiş,adım. kafama göre yazabilirim.
b=sin(a)
plot(a,b,'r')
mask = b>=0
plot(a[mask],b[mask],'r*')
mask= (b>=0) & (a<=pi/4)
plot(a[mask],b[mask],'go')
axis('tight')
show()





