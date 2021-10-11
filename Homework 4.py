#!/usr/bin/env python
# coding: utf-8

# In[16]:


import random
import string
import collections 


listdict = []
commondict = {}

def list_of_dict(listlength):
    for i in range(listlength): 
    #here generate a length of dict and count of dict
        listdict.append({random.choice(string.ascii_lowercase): random.randint(0,100)  for i in range(random.randint(2,10))}) #Change here for debug 
    return listdict

resutl_list_of_dict = list_of_dict(random.randint(2,10)) ##set result of execution list_of_dict
print(resutl_list_of_dict)



# In[17]:


def common_dict_func(lst):
    
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
                
            
    return commondict
    
result_common_dict_func = common_dict_func(resutl_list_of_dict)
print(result_common_dict_func)
############ END of HW 2 part ###############




########### HW 3 part ################

my_string = '''  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

#make all sentence for lower case
def lower (str):
    return my_string.lower()

my_lower_string = lower(my_string)
print(my_lower_string)


# In[30]:


def last_word_sentence(V_lower_string):
    my_list = V_lower_string.split('.')
    last_words_sentence = ''
    for i in range(len(my_list)-1):# говнокод с -1, не знаю как решить проблему с последним элементом списка ''
        last_word = my_list[i].split()[-1]
        last_words_sentence += str(last_word)+ str(' ')
    #print(last_words_sentence)
    
    updated_my_string = V_lower_string[:V_lower_string.rfind(' paragraph.')+len(' paragraph.')] + last_words_sentence
    updated2_my_string = updated_my_string + V_lower_string[my_lower_string.rfind(' paragraph.')+len(' paragraph.'): ]
    return updated2_my_string
result_of_last_word_sentence = last_word_sentence(my_lower_string)
print(result_of_last_word_sentence)


# In[28]:


def repl(a, b, v_str):
    return v_str.replace(str(' ' + a + ' '), str(' ' + b + ' ') )
a = repl('iz', 'is', str(result_of_last_word_sentence))
print(a)


# In[33]:


def clc(v_str):
    return len(my_string) - len(my_string.replace(' ', ''))

a = clc(my_string)
print(a)

