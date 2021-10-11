#!/usr/bin/env python
# coding: utf-8

# In[2]:


#pip install PyPDF2


# In[4]:


from PyPDF2 import PdfFileReader


# In[7]:


def getTextPDF(pdfFileName, password = ''):
    pdf_file = open(pdfFileName, 'rb')
    print('getTextPDF 입장')
    read_pdf = PdfFileReader(pdf_file)
    if password !='':
        read_pdf.decrypt(password)
    text = []
    for i in range(0, read_pdf.getNumPages()):
        text.append(read_pdf.getPage(i).extractText())
    return '\n'.join(text)


# In[ ]:





# In[ ]:




