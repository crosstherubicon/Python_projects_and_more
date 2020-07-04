#!/usr/bin/env python
# coding: utf-8

# In[15]:


import smtplib


# In[16]:


smtp_object = smtplib.SMTP('smtp.gmail.com', 587) #587 is the port number of gmail server


# Next step: EHLO method command which greets the server and establishes the connection. It should be created right after object is created. 

# In[17]:


smtp_object.ehlo()


# This means it is connected to the server now. 

# In[18]:


smtp_object.starttls()


# In[19]:


password: input('What is your password: ')


# In[20]:


import getpass #secure was of typing your password for hiding typed characters. 


# In[21]:


passowrd = getpass.getpass('Type your password: ')


# In[22]:


email = getpass.getpass("Email: ")
password = getpass.getpass("Password: ")
smtp_object.login(email, password)


# This password should be created using Google app password generator, not the regular gmail password for that gmail account. 

# In[23]:


from_address = email
to_address = email
subject = input("enter the subject line: ")
message = input("enter the body message: ")
msg = "Subject: " + subject +'\n' + message

smtp_object.sendmail(from_address, to_address, msg)


# In[24]:


smtp_object.quit()


# In[ ]:




