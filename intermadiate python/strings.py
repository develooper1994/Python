names=['şemsiye','tayyare','kalem','klavye']
for i in names:
    print("merhaba "+i)
print("-*"*15)
#print(" kullandım, ".join(['aaa',names]))
print(" kullandım, ".join(names))
print("-*"*15)



#eğer dosyaları göstermek ve işletim sisteminde dolaşmak istiyorsanız bu yöntemden kolayı ve hızlısı yoktur.
import os

loc_of_files="C:\\Users\\selcu\\Desktop\\proje\\intermadiate python"
file="örnek.txt"
#print(loc_of_files+"\\"+file) #Her bir dosya için tek tek yazmak iyi bir yöntem değil.

with open(os.path.join(loc_of_files,file)) as f:
    print("dosya okundu:\n"+f.read())

print("-*"*15)
#bilgileri string içine yazmanın daha iyi ve genel geçer bir yolu var.
isim="selçuk"
yas="22"
print(isim,'bence mahsuru yok. Benimde yaşım',yas)
print('{}bence mahsuru yok. Benimde yaşım{}'.format(isim,yas))
print('{0}bence mahsuru yok. Benimde yaşım{1}'.format(isim,yas))
print('{1}bence mahsuru yok. Benimde yaşım{0}'.format(isim,yas))
#print('{1}bence mahsuru yok. Benimde yaşım{2}'.format(isim,yas)) #python 0 tabanlı indekse sahiptir



