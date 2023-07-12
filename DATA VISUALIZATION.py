#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ## DATA VISUALIZATION

# In[4]:


x=np.array([101,102,103,104,105,106])
y=np.array([0,10,9,2,20,50])


# In[5]:


x,y


# In[6]:


plt.plot(x,y)


# #Making a graph without line

# In[7]:


plt.plot(x,y,'*')


# solid line
# : dotted line
# -->dashed line 
# -.-. dashed/doted line

# ## Format String 

# In[8]:


#syntax: marker |line|color


# In[9]:


plt.plot(x,y,'d--g')


# In[10]:


# r = red
#g=green 
#b=blue
#y=yellow and many more


# In[11]:


plt.plot(y,marker='*',ms=10)


# In[12]:


#for color  mec=marker edge color
plt.plot(y,marker='*',ms=10,mec='y')


# In[13]:


#marker face color 
plt.plot(y,marker='*',ms=10,mfc='m')


# linestyle

# In[14]:


plt.plot(y,linestyle='dotted')


# In[15]:


plt.plot(y,linestyle='dotted',color='m')


# In[16]:


plt.plot(y,linestyle='dotted',color='y',linewidth='10')


# In[17]:


plt.plot(x)


# In[18]:


plt.plot(y)


# In[19]:


plt.plot(x)
plt.plot(y)


# In[20]:


x=[3,8,1,10]
y=[6,2,10,11]
plt.plot(y)
plt.plot(x)


# #Labels

# In[23]:


plt.plot(y)
plt.plot(x)

plt.xlabel('height')
plt.ylabel('weight')


# title

# In[24]:


plt.plot(y)
plt.plot(x)
plt.title('height v/s weight graph')

plt.xlabel('height')
plt.ylabel('weight')


# In[27]:


plt.plot(y)
plt.plot(x)
modification ={'color':'magenta','size':15,'family':'serif'}
plt.title('Height v/s Weight Graph',fontdict=modification)

plt.xlabel('height')
plt.ylabel('weight')


# subplot

# In[29]:


x=[1,2,3,4,5,6]
y=[10,20,30,40,50,60]
#plt.subplot(rows,coloumns,plt_number)
plt.subplot(1,2,1)
plt.plot(x,y)

x=[3,8,1,10]
y=[6,2,10,11]
plt.subplot(1,2,2)
plt.plot(x,y)


# for horizontal way

# In[30]:


x=[1,2,3,4,5,6]
y=[10,20,30,40,50,60]
#plt.subplot(rows,coloumns,plt_number)
plt.subplot(2,1,1)
plt.plot(x,y)

x=[3,8,1,10]
y=[6,2,10,11]
plt.subplot(2,1,2)
plt.plot(x,y)


# In[31]:


x=[1,2,3,4,5,6]
y=[10,20,30,40,50,60]
#plt.subplot(rows,coloumns,plt_number)
plt.subplot(2,3,1)
plt.plot(x,y)

x=[3,8,1,10]
y=[6,2,10,11]
plt.subplot(2,3,2)
plt.plot(x,y)


x=[1,2,3,4,5,6]
y=[10,20,30,40,50,60]
#plt.subplot(rows,coloumns,plt_number)
plt.subplot(2,3,3)
plt.plot(x,y)

x=[3,8,1,10]
y=[6,2,10,11]
plt.subplot(2,3,4)
plt.plot(x,y)

x=[1,2,3,4,5,6]
y=[10,20,30,40,50,60]
#plt.subplot(rows,coloumns,plt_number)
plt.subplot(2,3,5)
plt.plot(x,y)

x=[3,8,1,10]
y=[6,2,10,11]
plt.subplot(2,3,6)
plt.plot(x,y)


# supertitle

# In[32]:


x=[1,2,3,4,5,6]
y=[10,20,30,40,50,60]
#plt.subplot(rows,coloumns,plt_number)
plt.subplot(2,3,1)
plt.plot(x,y)

x=[3,8,1,10]
y=[6,2,10,11]
plt.subplot(2,3,2)
plt.plot(x,y)


x=[1,2,3,4,5,6]
y=[10,20,30,40,50,60]
#plt.subplot(rows,coloumns,plt_number)
plt.subplot(2,3,3)
plt.plot(x,y)

x=[3,8,1,10]
y=[6,2,10,11]
plt.subplot(2,3,4)
plt.plot(x,y)

x=[1,2,3,4,5,6]
y=[10,20,30,40,50,60]
#plt.subplot(rows,coloumns,plt_number)
plt.subplot(2,3,5)
plt.plot(x,y)

x=[3,8,1,10]
y=[6,2,10,11]
plt.subplot(2,3,6)
plt.plot(x,y)
plt.suptitle('ANIMALS')


#  ticks

# In[35]:



x=[3,8,1,10]
y=[6,2,10,11]
#plt.set_
#plt.subplot(2,3,6)
plt.plot(x,y)
fig=plt.figure()
ax=fig.add_axes([1,2,5,5])
ax.plot(x,y)


#  GRAPHS
#  scatterplot

# In[37]:


x=[3,8,1,10 ,5,8,112,44,56,77]
y=[6,2,10,11,13,40,56,78,99,100]
plt.scatter(x,y)


# barplot

# In[38]:


x=["One","Two","Three","Four"]
y=[6,9,1,20]
plt.bar(x,y,color="magenta")


# HISTOGRAM

# In[39]:


x=np.random.normal(200,10,300)


# In[40]:


x


# In[42]:


plt.hist(x,color='yellow')


# In[43]:


#pie


# In[45]:


x=[25,25,25,24,1]
plt.pie(x,labels=["chocolates",'vanilla','apple','blackcurrent','mango'])


# In[ ]:




