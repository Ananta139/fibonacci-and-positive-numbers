#!/usr/bin/env python
# coding: utf-8

# In[2]:


#fibonacci series
x=0
y=1
z=0
n= input("enter no. of digits you want to see: ")
for i in range(0,int(n)):
    print(z, end=" ")
    z=x+y
    x=y
    y=z
    


# In[13]:


#selecting positive numbers from a list
list=[-10,9,-4,-5,6,7,8,-19]
for n in list:
    if n>=0:
        print (n, end=' ')


# In[ ]:




