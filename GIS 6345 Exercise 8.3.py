#!/usr/bin/env python
# coding: utf-8

# In[1]:


def is_palindrome(string):
    return string == string[::-1]


# In[2]:


print is_palindrome(Hippopotamus)


# In[3]:


print is_palindrome('Hippopotamus')


# In[4]:


def is_palindrome(word):
    if len(word) <= 2 and word[0] == word[-1]:
        print 'True'
    elif word[0] == word[-1]:
        is_palindrome(word[1:-1])
    else:
        print 'False'


# In[5]:


def is_palindrome(word):
    if len(word) <= 2 and word[0] == word[-1]:
        print ('True')
    elif word[0] == word[-1]:
        is_palindrome(word[1:-1])
    else:
        print ('False')


# In[6]:


def is_palindrome(word):
    return word == word[::-1]


# In[7]:


print is_palindrome('Hippopotamus')


# In[8]:


def is_palindrome(string):
    string = str(string)
    return string == string[::-1]


# In[9]:


print(is_palindrome('hippopotamus'))


# In[ ]:





# In[10]:


def is_palindrome(string):
    string = str(string)
    return string == string[::-1]


# In[11]:


print(is_palindrome('hippopotamus'))


# In[12]:


def is_palindrome(string):
    string = str(string)
    return string == string[::-1]


# In[13]:


print(is_palindrome('nana'))


# In[14]:


def is_palindrome(string):
    string = str(string)
    return string == string[::-1]


# In[15]:


print(is_palindrome('noon'))


# In[ ]:




