print("----------------------"*5)
print("---os module---")

import os

print(os.listdir())
print(dir(os)) #list all os properties and methods

print("----------------------"*5)
print("---glob2 module---")
os.system("pip install glob2") #ensure to requirements already satisfied.

import glob2
print(glob2.glob("*"))
print(glob2.glob("*.txt")) #only .txt extantion
print(glob2.glob("*.py")) #only .py extantion

