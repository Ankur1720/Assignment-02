#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values?


# In[1]:


dict_1 = {}
for i in range(97,97+26):
    dict_1[chr(i)]= i
print(dict_1)


# In[ ]:




