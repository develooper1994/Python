örnek=['sıfır','bir','iki','üç']
#yaptığın
for i in range(len(örnek)):
    print(i,örnek[i])
print('*-'*10)
#olması gereken
for i,s in enumerate(örnek):
    print(i,s)

dicted=dict(enumerate(örnek))
print(dicted)

[print(i,j) for i,j in enumerate(dicted)]





