from os import walk

f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break



print("---Directory Path---")
for item in dirpath: print(item)
print("---Directory Names---")
for item in dirnames: print(item)
print("---File Names---")
for item in filenames: print(item)