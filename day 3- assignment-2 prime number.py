#!/usr/bin/env python
# coding: utf-8

# In[4]:


for hitu in range (2,200):
    for rawat in range (2,hitu):
        if hitu%rawat == 0:
            break
    else:
        print(hitu)

