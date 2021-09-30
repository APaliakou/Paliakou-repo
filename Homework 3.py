#!/usr/bin/env python
# coding: utf-8

# In[1]:

my_string = '''  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''


# In[2]:

#make all sentence for lower case
my_lower_string = my_string.lower()
print(my_lower_string)


# In[3]:

#create one more sentence with last words
my_list = my_lower_string.split('.')
last_words_sentence = ''
for i in range(len(my_list)-1):# говнокод с -1, не знаю как решить проблему с последним элементом списка ''
    last_word = my_list[i].split()[-1]
    last_words_sentence += str(last_word)+ str(' ')
#print(last_words_sentence)

updated_my_string = my_lower_string[:my_lower_string.rfind(' paragraph.')+len(' paragraph.')] + last_words_sentence
updated2_my_string = updated_my_string + my_lower_string[my_lower_string.rfind(' paragraph.')+len(' paragraph.'): ]
print(updated2_my_string)


# In[4]:

#replace "iz" to "is"
my_new_updated_string = updated2_my_string.replace(' iz ', ' is ')
print(my_new_updated_string)


# In[5]:

#I've got only 84 (checked manualy in notepad++ =) )
print(len(my_string) - len(my_string.replace(' ', '')))
