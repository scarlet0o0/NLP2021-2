#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install python-docx')


# In[4]:


import docx


# In[6]:


def getTexWord(wordFileName):
    doc = docx.Document(wordFileName)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)


# In[ ]:




