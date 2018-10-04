file=open('example.txt','w')
file.write("Line 1")
file.close()

print("---------------"*5)

file=open('example.txt','w+')
file.write("Line 2")
file.seek(0)
print(file.read())
file.close()

print("---------------"*5)

file=open('example.txt','w+')
file.write("Line 1")
file.write("Line 2")
file.seek(0)
print(file.read())
file.close()

print("---------------"*5)

file=open('example.txt','w+')
file.writelines(["Line 1\n"
                 "Line 2\n",
                 "Line 3"])
file.seek(0)
print(file.read())
file.close()