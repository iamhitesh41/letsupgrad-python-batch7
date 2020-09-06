#!/usr/bin/env python
# coding: utf-8

# In[13]:


a = int(input("Enter your altitude in ft."))


# In[14]:


if a<=1000:
    print("Sir land plane here")
elif a>=1000 and a<=5000:
    print("sir come down to 1000ft.")
else:
    print("Go around")

