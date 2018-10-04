c='yazı'
c=c.replace("a","i")
print(c)
d='kaza'
d=d.replace("a","i",1)
print(d)
d=d.replace("a","i",1)
print(d)

print("okunabilir "+"yazı")

#---string indexing---

c='Hi There';
print('Hi There [3]',c[3],type(c[3]))
print('Hi There [1]',c[1],type(c[1]))
print('Hi There [2]',c[-1],type(c[-1])) #-1 is end
print('Hi There [0]',c[0],type(c[0]))
print('Hi There [-2]',c[-2],type(c[-2]))
print('Hi There [2]',c[2],type(c[2]))
print('Hi There [0:1]',c[0:1],type(c[0:1]))
print('Hi There [0:2]',c[0:2],type(c[0:2]))
print('Hi There [0:3]',c[0:3],type(c[0:3]))
print('Hi There [:3]',c[:3],type(c[:3]))
print('Hi There [3:]',c[3:],type(c[3:]))
print('Hi There [:-1]',c[:-1],type(c[:-1]))
print('Hi There [-3:]',c[-3:],type(c[-3:]))
print('Hi There [-3:-1]',c[-3:-1],type(c[-3:-1]))



