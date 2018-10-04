'''Yavaş python yöntemi. sadece python kodlarıyla okuma yapılıyor.
Büyük veriler için iyi değil. numpy içinde loadtxt diye güzel bir fonksiyon var.
Bu fonksiyon sayesinde cvskit kütüphanesine ihtiyacımız azalıyor.
***Ayrıca böyle dosya içindeki yazılar yüzünden bir sürü hata alacağız.
'''
from numpy import *


'''
file=open('Data.txt')
data=[]
for line in file:
    fields=line.split()
    row_data=[float(x) for x in fields] #python2 de veriler float olmadığından çevrim zorunlu oluyor.
    #data artık append ile doluyor.
    data.append(row_data)

data=array(data)
file.close()
'''
#şimdi numpy loadtxt yöntemi
arr = loadtxt('Data.txt',skiprows=1,
            dtype=int,
            delimiter=",",
            usecols=(0,1,2,),
            comments="%")
#fmt yerine i=int,f=float,e=exponential yazabilirsiniz.
#yazmazsanız exponential olarak yazacaktır.
savetxt('justData.txt',arr,fmt='%.2i')

# python için yazılmış ve çeşitli verileri okumaya yarayan modüller bulunuyor.
# hele h5py çok büyük verileri okumada çok iyi.
# cvskit,scipy.io,pytables,h5py,netcdf,netcdf4,wavfile,pil,pilutils,pyfits,obspy

