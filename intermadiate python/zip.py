sayıyla=[0,1,2,3]
yazıyla=['sıfır','bir','iki','üç']
asd=[999,8888,7777,6666]
#enumerate(yazıyla)
for i,j in zip(sayıyla,yazıyla):
    print(i,j)

print(list(zip(yazıyla,sayıyla)))
print(list(zip(yazıyla,sayıyla,asd)))
print(dict(zip(yazıyla,sayıyla)))

[print(a,b,c) for a,b,c in zip(yazıyla,sayıyla,asd)]


x = [1,2,3,4]
y = [7,8,3,2]
z = ['a','b','c','d']

#[print(x,y,z) for x,y,z in zip(x,y,z)]

for x,y,z in zip(x,y,z):
    print(x,y,z)
