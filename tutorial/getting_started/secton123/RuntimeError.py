a=1;
b="2";
print(int(2.5)) #true
print(a+int(b)) #true
print(str(a)+b) #not always true
#print(int(2.5) #false
#print(a+b) #number+string is runtime error. different types
#print(c) #c is not defined
#print(a/0) #ZeroDivisionError

#fixing runtime error.runtime
try:
	print(a/0)
except ZeroDivisionError:
	a=0
print(a)

def divide(a,b):
	try:
		return a/b
	except ZeroDivisionError:
		return "Zero division is meaningless"
print(divide(1,2))
print(divide(1,0))