#!/usr/bin/env python
# coding: utf-8

# # While Loop

# In[2]:


# 5,9,12,14,15

sum = 0
n = int(input("N : "))
while n<=10:
    sum = sum+n
    n+=2
    print("Sum : ",sum)
print("Bye")


# In[2]:


sum = 0
n = int(input("N : "))
while n>0:
    sum = sum+n
    n-=1
    print("Sum : ",sum)
print("Bye")


# In[5]:


sum = 5
n = int(input("N : "))
while n>0:
    sum = sum+n
    n-=2
    print("Sum : ",sum)

print("Bye")


# # Simple For Loop

# In[20]:


word = ["Python","Java","Angular"]
for i in word:
    print(i,'=',len(i))


# # Nested For Loop

# In[24]:


# *
# **
# ***
# ****
# *****
# range(start point,end point,step(jump))

for i in range(1,6):
    for j in range(i):
         print("*",end="")
    print()


# In[29]:


for i in range(5,0,-1):
    for j in range(i):
         print("*",end="")
    print()


# In[ ]:




