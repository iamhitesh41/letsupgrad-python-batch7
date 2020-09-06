#!/usr/bin/env python
# coding: utf-8

# In[ ]:


b = int(input("enter the value"))
c = int(input("enter the value"))
for a in range (b,c):
    result=a
    sum=0
    i=len(str(a))
    while a!=0:
        rem=a%10
        sum=sum+pow(rem,i)  
        a=a//10
    if result==sum:
        print("it is amongstrong",result)
        
else:
    print("no amongstrong")

