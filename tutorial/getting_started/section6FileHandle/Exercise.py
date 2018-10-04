numbers = [1, 2, 3]
file=open("exercise1.txt","w+");
content=[1, 2, 3]; content=[str(item)+'\n' for item in content];
file.writelines(content)

file.seek(0)
print(file.read())

file.close()

print("-------------------"*5)
print("---file appending---")
numbers = [1, 2, 3]
file=open("exercise1.txt","a");
content=[1, 2, 3]; content=[str(item)+'\n' for item in content];
file.writelines(content)
file.close()

print("-------------------"*5)
print("---reading file appended---")
file=open("exercise1.txt","r");
file.seek(0)
print(file.read())
file.close()