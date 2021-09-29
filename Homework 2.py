#!/usr/bin/env python
# coding: utf-8

# In[1]:


# create a list of random number of dicts (from 2 to 10)

#dict's random numbers of keys should be letter,
#dict's values should be a number (0-100),
#example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

import random
import string
import collections 

listlength = random.randint(2,10) #generate length for the list. Change here for debug
listdict = [] #declare empty list. Will append dicts as list's element

#starting adding dict for each index of list
for i in range(listlength): 
    #here generate a length of dict and count of dict
    listdict.append({random.choice(string.ascii_lowercase): random.randint(0,100)  for i in range(random.randint(2,10))}) #Change here for debug 
    
#random.choice(string.ascii_lowercase) --- generates random lowercase letter for a key
#random.randint(0,100) --- generates random number for a value
#for i in range(random.randint(2,10)) --- define length of each dict
    
print(listdict)


# In[2]:


#get previously generated list of dicts and create one common dict:

#if dicts have same key, we will take max value, and rename key with dict number with max value
#if key is only in one dict - take it as is,
#example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

commondict = {}

for i in range(len(listdict)):
    tmpdict = listdict[i]
    for j in tmpdict:
        #check that key already exist in final dict and his value more that existed
        if j in commondict and commondict[j] < tmpdict[j]:
            #update existed key. Generate updated key and his value
            newpair = {str(j)+'_'+str(i+1):tmpdict.get(j)} 
            #adding updated key and value to final dict
            commondict.update(newpair)
            #remove old key with value
            commondict.pop(j)
         #cath cases when key exists and his value more. Do not nothing   
        elif j in commondict and commondict[j] > tmpdict[j]:
            False
         #adding new key/value if key doesn't exist in final 
        else:
            newpair = {j:tmpdict.get(j)}
            commondict.update(newpair)
            
        
print(commondict)
