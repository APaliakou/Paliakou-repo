#!/usr/bin/env python
# coding: utf-8

# In[40]:


import random
##create list of 100 random numbers from 0 to 1000
rndlist = random.sample(range(0, 1000), 100)
print(rndlist)


# In[41]:


#sort numbers in list
new_list = [] #define new list
for i in range(len(rndlist)): #define range of itteration
    new_list.append(min(rndlist)) #search min number in list and adding to new
    rndlist.remove(min(rndlist)) #remove min number from old list. That allow us to find the same number on the next step
print(new_list)


# In[45]:


even_list = [] #define new list of even numbers
odd_list = [] #define new list of odd numbers

for i in range(len(new_list)): #create range lenght of list.
    if new_list[i] % 2 == 0: # check that number with position i devided without modulo
        even_list.append(new_list[i]) # if yes add this number to even_list
    else:
        odd_list.append(new_list[i]) # if modulo > 0 then add to the odd_list
##print(new_list)
print(even_list)
print(odd_list)


# In[46]:


print(sum(even_list)/len(even_list))
print(sum(odd_list)/len(odd_list))


# In[ ]:




