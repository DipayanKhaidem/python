#!/usr/bin/env python
# coding: utf-8

# In[4]:


def myfunc(name):
    print('Hello {}'.format(name))

myfunc("Dipayan")


# In[5]:


def myfunc(a,b):
    #returns 5% of the sum of a and b
    return sum((a,b))*0.05


# In[6]:


myfunc(40,60)


# In[7]:


def myfunc(*args):
    return sum(args)*0.05
    


# In[8]:


myfunc(40,60,100)


# In[9]:


def myfunc(*args): #treats the arguments as a tuple and allows us to pass any number of arguments
    print(args)


# In[10]:


myfunc(40,60,100)


# In[12]:


def myfunc(**kwargs): #returns a dictionary
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice {}'.format(kwargs['fruit']))
    else:
        print('I didnt find any fruit here')


# In[13]:


myfunc(fruit='apple',veggie='lettuce')


# In[15]:


#using *args and **kwargs in combination
def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))


# In[16]:


myfunc(10,20,30,fruit='orange',food='eggs',animal='dog')


# In[ ]:




