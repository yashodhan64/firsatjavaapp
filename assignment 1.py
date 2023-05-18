#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[13]:


lst=[1,2,3,4,5]
a1=np.array(lst)
print(a1)


# In[21]:


lst=[[1,2,3,4,5],[6,7,8,9,10]]
a2=np.array(lst)
print(a2)


# In[27]:


lst=[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]]
a3=np.array(lst)
print(a3)


# In[24]:


print(a2.ndim)
print(a2.shape)
print(a2.dtype)
print(a2.size)


# In[25]:


print(a1.ndim)
print(a1.shape)
print(a1.dtype)
print(a1.size)


# In[28]:


print(a3.ndim)
print(a3.shape)
print(a3.dtype)
print(a3.size)


# In[30]:


lst=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
a=np.array(lst)
print(a)


# In[31]:


a.empty(2)


# In[32]:


print(a.empty(2))


# In[39]:


a=np.empty((3,2))
print(a)


# In[41]:


a=np.full(3,2)
print(a)


# In[42]:


a=np.full(3,0)
print(a)


# In[45]:


a=np.ones((3,5),dtype=int)
print(a)


# In[46]:


a=np.zeros((3,5),dtype=int)
print(a)


# In[47]:


a=np.arange(14,41,dtype=int)
print(a)


# In[49]:


a=np.arange(1,41).reshape(8,5)
print(a)


# In[50]:


print(a.ndim)
print(a.shape)
print(a.dtype)
print(a.size)


# In[51]:


a=reshape(4,10)
print(a)


# In[52]:


b=a.reshape(4,10)
print(b)


# In[53]:


c=np.arr()
print(c)


# In[55]:


a=np.arange(1,16).reshape(5,3)
print(a)


# In[56]:


a+4


# In[60]:


print(a+2)
print(a*2)
print(a-3)
print(a/2)


# In[67]:


b=np.arange(1,10).reshape(3,3)
print(b)


# In[65]:


d=np.arange(11,20).reshape(3,3)
print(d)


# In[66]:


f=print(d+b)
print(d-b)
print(d*b)
print(d/b)


# In[69]:


print(d.min(axis=0))
print(d.max(axis=0))
print(d.sum())


# In[ ]:




