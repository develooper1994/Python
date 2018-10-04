import numpy as np
from numpy import *
import matplotlib.pyplot as p
from matplotlib.pyplot import *
import os,time
import cv2

#aslen plot
x=linspace(0,2*pi,50)
plot(x,cos(x),"r-^",x,cos(x)+sin(x),"r-^")
show()
p.close()

#scatter
x=linspace(0,2*pi,50)
y=sin(x)
p.scatter(x,y)
p.show()
close()

#daha iyi scatter
x=random.rand(200)
y=random.rand(200)
size=random.rand(200)*30
color=random.rand(200)
scatter(x,y,size,color)
colorbar()
p.show()
close()

#figure l-er
t=linspace(0,2*pi,50)
x=cos(t)
y=sin(t)
figure()
plot(x);show()
figure()
plot(y);show()
#subplotlar #subplot(rows,cols,actif plot)
figure()
subplot(2,1,1)
plot(x)
subplot(2,1,2)
plot(y)
show()

#hold ve legend
plot(sin(t),label="sin"); hold(True); plot(cos(t),label="cos"); legend() #hold yok
plot(sin(t));hold(False); plot(cos(t)); legend(['sin', 'cos'])
plot(sin(t));hold(True); plot(cos(t)); legend(['sin', 'cos'])

plot(t,sin(t)); xlabel('radiens'); ylabel("amplitude",fontsize="large"); title("Sin(x)")
axis("tight")
tight_layout()
grid() #koordinat sistemini açar.
#clf() #grafik penceresini temizle
#close() #birini kapatır. deneme yaparken...
#close("all") #matplotlib de ne açıksa kapatır. deneme yaparken...
savefig('tight-sin-grid-plot.png')


