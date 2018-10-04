file=open("example.txt",'r')
content=file.read() #when read method calls file pointer goes to end off file thus other read methods reads empty string
print('type(file): ',type(file))
print(content)

print('-------------'*5)

file.seek(0) #file pointer goes to begin
content1=file.readlines()
print( [i.rstrip('\n') for i in content1] ) #striping \n character
file.close() #must close file after operations

print('-------------'*5)

fileFruit=open('fruits.txt','r')
contentFruit=fileFruit.readlines()
print( [i.strip().__len__() for i in contentFruit] )
