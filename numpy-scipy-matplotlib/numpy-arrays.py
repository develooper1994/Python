import numpy as np
from numpy import *
import matplotlib.pyplot as p
from matplotlib.pyplot import *

a=array([[0,1,2,3],[4,5,6,7]])
print("a= ",a)
print("type(a)= ",type(a))
print("a.dtype= ",a.dtype)
print("a.itemsize= ",a.itemsize)
print("a.shape= ",a.shape)
print("shape(a)= ",shape(a))
print("a.size= ",a.size)
print("size(a)= ",size(a))
print("ndim(a)= ",ndim(a))
print("a.ndim= ",a.ndim)
#print("nbytes(a)= ",nbytes(a)) #yok öyle birşey
print("a.nbytes= ",a.nbytes)
print("bytes(a)= ",bytes(a))
#print("a.bytes= ",a.bytes) #yok öyle birşey
#indexing ####daha devam edecek.
#var[alt:üst:adım]
print("\n\nindexing:\n")
a=array([
        [0,1,2,3],
        [4,5,6,123],
        [45,56,78,98]
        ]
) #mümkünse tüm satırlar
#aynı eleman sayısında olsun.
print("a= ",a)
print("a[0]= ",a[0])
print("a[1]= ",a[1])
print("a[1:]= ",a[1:])
print("a[1][2:]= ",a[1][2:])
print("a[2:]= ",a[2:])
print("a[2][::2]= ",a[2][::2])
print("a[::2]= ",a[::2])
print("a[-1][:-1]= ",a[-1][:-1])
print("a[-1][::-1]= ",a[-1][::-1])
print("a[-1][:-1]= ",a[0:][:-1])
a[1,3]=-1
print("a= ",a)
print("a[1,3]= ",a[1,3]) #böylesi çok daha iyi
print("a[1:2,:]= ",a[1:2,:])
print("a[2::2,::2]= ",a[2::2,::2])
print("a[1:,1:]= \n",a[1:,1:])
print("a[1:3,1:3]= \n",a[1:3,1:3])
#move mu copy mi? işte burada copy işlemi var. referans değil.
b=a
b[1,3]=-111
print("a=\n",a)
print("b=\n",b)
b=a.copy()
b[1,3]=-111
print("a=\n",a)
print("b=\n",b)



#bir türev ve integral probleminin kolay ve hızlı yöntemi. (midpoint derivative)
x=linspace(0,2*pi,50)
y=sin(x)
dy=y[1:]-y[:-1]
dx=x[1:]-x[:-1]
dy_dx=dy/dx
centers_x=(x[1:]+x[:-1])/2
print("dy/dx= ",dy_dx)
print("centers_x= ",centers_x)
subplot(1,2,1); plot(centers_x,dy_dx,'rx',centers_x,cos(centers_x),'b-')
title(r'$\rm(Derivative\ of)\sin(x)$')
avg_hight=(y[1:]+y[:-1])/2
int_sin=cumsum(dx*avg_hight)

closed_form=-cos(x)**2
subplot(1,2,2); plot(x[1:],int_sin,'rx',x,closed_form,'b-')
legend(('numerical','actual' ))
title(r"$\int \, sin(x) \,dx$")
show()



#hazır diziler
print("\n\nhazır diziler:\n")
print("a= ",a)
a.fill(0) #4x3 ama 4 eleman 3 [] içinde olduğundan...
print("a.fill(0)= ",a)
a[:]=1
print("a= ",a,"\na.dtype",a.dtype)
a.fill(-4.8)  #sanırım python3 olduğu için -4.8 yapabiliyor ama diğer şekilde python2de
# -4 yazardı.
print("a= ",a)