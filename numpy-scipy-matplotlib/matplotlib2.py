import numpy as np
from numpy import *
import matplotlib.pyplot as p
from matplotlib.pyplot import *
import os,time
import cv2

img=cv2.imread("roi.jpg",0)

figure()
subplot(3,1,1)
imshow(img,cmap=cm.bone) #,extent=[-25,250,50,500] gibi birşey eklerseniz
# scale yani ölçeklendirebilirsiniz.
colorbar()
title("image")
ax2=subplot(3,1,2)
hist(img); title("renk çizergesidir. her bir renk için yapılır. bir nevi fft")
subplot(3,1,3,sharex=ax2,sharey=ax2)
hist(img,30); title("renk çizergesidir. her bir renk için yapılır. 30 gibi sayılar görselliği deiştirir.")
show()

#üç boyutlu çizim
from numpy import mgrid
from scipy import special
from mayavi import mlab
from math import *
x,y=mgrid[-25:25:100j,-25:25:100j]
r=sqrt(x**2+y**2)
s=special.j0(r)*25
mlab.surf(x,y,s)
mlab.scalarbar()
mlab.axes()
