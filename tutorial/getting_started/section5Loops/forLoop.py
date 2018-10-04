emails='@gmail.com '.join(['me', 'you', 'they', '']).split()

for item in emails:
    if 'gmail' in item:
        print(item)

print("--------"*5)

mylist = [1, 2, 3, 4, 5]
for items in mylist:
    print(items)

print("--------"*5)

for items in mylist[2:]:
    print(items)