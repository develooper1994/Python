
# coding: utf-8

# In[2]:


import os
os.listdir()


# In[18]:


ar=[[5, 9, 32496, 6, 3251,65 ,54],[],[]]
type(ar)


# In[56]:


import numpy as np
n=np.arange(27)


# In[27]:


print("n.reshape(3,9): ",n.reshape(3,9))


# In[25]:


print("shape: ",n.shape)
print("size: ",n.size)


# In[22]:


m=np.asarray( ar )
print(type(m))


# In[30]:


os.listdir()


# In[29]:


import cv2


# In[38]:


# numpy dizisi yazdıracaktır. resim tipi her zaman "uint8" dir.
img_gray=cv2.imread("smallgray.png",0)
print(img_gray)
cv2.imwrite("new_smallgray.png",img_gray)


# In[45]:


# kaçıncı indexten : kaçıncı indexe kadar(dahil değil)
print(img_gray[2,4])
print(img_gray[0:2])
print(img_gray[0:2,2:4])


# In[48]:


#numpy iterationu. 2 boyutlu bir dizi olduğundan altındaki boyutu yazdırıyor.
print(img_gray)
for item in img_gray:
    print(item)


# In[54]:


# 2 boyutlu bir diziyi tek boyutlu vektörü gibi gösterdik.
print(img_gray)
print(list(img_gray.flat))
for item in img_gray.flat:
    print(item)


# In[60]:


# matrise eklemeler nasıl yapılır?
# horizontal yani yatay ekleme
ims=np.hstack( (img_gray,img_gray) )
ims


# In[62]:


# matrise eklemeler nasıl yapılır?
# vertical yani dikey ekleme
ims=np.vstack( (img_gray,img_gray) )
ims


# In[68]:


#lst=np.hsplit(ims,3) # 5 sütun var ve 3e bölmeye çalışıyoruz. tam bölünmez. HATA!
lst=np.vsplit(ims,3)
print(type(lst))  #Dikkaaat! bu bir liste tipi
print(lst)
print(lst[0])

