a=2;
b=3;
print('type(a)',type(a))
print('type(b)',type(b))
print('toplam',a+b)
print('çıkartma',a-b)
print('çarpma',a*b)
print('bölme',a/b)
print('sayıyı böl ve virgülden sonrasını alma',a//b)
print('mod işlemi mod(2,3)',a%b)
ac='2';
bc='3';
print('type(a)',type(ac))
print('type(b)',type(bc))
print('toplam',ac+bc) #str verileri yan yana ekleniyor.
#print('çıkartma',ac-bc) #str verisi yan yana eklenemiyor.
#print('çarpma',ac*bc) #str verileri yan yana çarpılamıyor.
print('çarpma',ac*3) #str verisi 3 kez tekrarlanıyor ;)
#print('bölme',ac/bc) #str verileri bölünemiyor.
#print('sayıyı böl ve virgülden sonrasını alma',ac//bc) #str verileri bölünemiyor.
#print('mod işlemi mod(2,3)',ac%bc) #str verilerinde mod işlemi yapılamıyor.

print('\n'*5,'YENİ ŞEYLER')
age=input('Enter your age: '); #not: input daima veriyi str olarak alır.
new_age=age+int(50);
print(new_age)




