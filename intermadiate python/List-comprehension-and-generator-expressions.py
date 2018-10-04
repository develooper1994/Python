from pathlib import Path
path=Path('')
dirs=[x for x in path.iterdir() if x.is_file()]
print(dirs)
print(list(path.glob('**/*.py')))#örnek.txt yazdırılmıyor dikkat edin.

path=Path('')
dirs=[x for x in path.iterdir() if x.is_dir()]
print(dirs)


print("-*"*15,"\n"*3)
#tümü hafızada tutulur. büyük verilerde ram ve cache için sıkıntı
xyz=[]
for i in range(5):
    xyz.append(i)
print(xyz)


#tümü hafızada tutulur. büyük verilerde ram ve cache için sıkıntı
xyz=[i for i in range(5000000)] #evde denemeyin.
print(xyz)
#tümü hafızada tutulmaz. bu şekilde hafızada daha az yer kaplayarak çalışıabilir.
#eğer verilerin hepsi rame yüklenmek istemiyorsa işte çözüm...
xyz=(i for i in range(5000000)) #evde denemeyin.
print(xyz)

input_list=list(range(10))
def ciftmi(num):
    if num%2==0:
        return True
    else:
        return False

xyz=lambda input_list: (i for i in input_list if ciftmi(i))
xzz=(print(i) for i in xyz(input_list)) #generatorolduğundan yazdırmadı. aynı şeyi yapmıyorlar
for i in xzz:
    i #fonksiyon iterasyonu

[print(i) for i in xyz(input_list)]
'''
xyz=lambda input_list: (i for i in input_list if ciftmi(i))
[print(i) for i in xyz(input_list)]
sizin alıştığınız karşılığı
xyz=[]
for i in range(i):
    if ciftmi(i):
        xyz.append(i)

for i in xyz(input_list):
    print(i)
'''
print("-*"*15,'\n'*3)
[[print(i,ii) for i in range(5)] for ii in range(5)]
'''
eşleniği:
for i in range(5):
    for ii in range(3):
        print(i,ii)
'''

#generatorler zamandan(hızdan) listeler ramden çalar. buna göre programını buna göre optimize et.
print("-*"*15,'\n'*3)
xyz=[[(i,ii) for i in range(5)] for ii in range(5)]
print(xyz)
xyz=([(i,ii) for i in range(5)] for ii in range(5)) #generator
print(xyz)
from itertools import count
print([i for i in xyz]) #generator iterasyonu

xyz=(((i,ii) for i in range(50)) for ii in range(50)) #generator's generator

for i in xyz:
    for ii in i:
        print(ii)








