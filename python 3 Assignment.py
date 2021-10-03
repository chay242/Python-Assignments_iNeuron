#!/usr/bin/env python
# coding: utf-8

# In[9]:


#'x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz'
lc1=[i*j for i in 'xyz' for j in range(1,5)]
lc1


# In[13]:


#['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz'] 
lc2 = [i*j for j in range(1,5) for i in 'xyz']
lc2


# In[23]:


#[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
lc3=[[i+j] for i in range(2,5) for j in range(3)]
lc3


# In[31]:


#[[2, 3, 4, 5], [3, 4, 5, 6],[4, 5, 6, 7], [5, 6, 7, 8]]
lc4= [[i+j for j in range(2,6)] for i in range(4)]
lc3


# In[75]:


#[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
lc5=[(j,i) for i in range(1,4) for j in range(1,4)]
lc4


# In[1]:


#Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()
def myfilter(fn,l):
    m=[]
    if fn==None:
        for j in l:
            if j in [0,None,[],{},False]:
                pass
            else:
                yield(j)
       
    else:
        for k in l:
            if fn(k) is True:
                yield(k)


# In[ ]:


#Write a Python program to implement your own myreduce() function which works exactly like Python's built-in function filter()
def myreduce(fn,iterable,init=None):
    i=iter(iterable)
    if init is None:
        value=next(i)
        
    else:
        value=init
    for j in i:
        print(j)
      
        value=fn(value,j)
    return value

