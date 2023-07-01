#!/usr/bin/env python
# coding: utf-8

# ## Name: Manish Singh

# ### Importing Required Libraries

# In[58]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
print(" All required packages included successfully!")


# ### Importing Data Set

# In[22]:


data = pd.read_csv('powerconsumption.csv')


# In[3]:


data


# In[23]:


data.info()


# In[24]:


r,c = data.shape
print("Number of rows    = ",r)
print("Number of columns = ",c)


# In[25]:


data.shape


# In[26]:


data.describe()


# In[27]:


data.head()


# In[28]:


data.tail()


# In[29]:


pd.isna(data)


# In[30]:


data.isna().sum()


# In[31]:


dfnew = data
dfnew.head()


# In[32]:


dfnew.head()


# In[36]:


dfnew['Year']=pd.DatetimeIndex(dfnew['Datetime']).year


# In[37]:


dfnew.head()


# In[41]:


dfnew['Year'].value_counts()


# In[42]:


dfnew['Month']=pd.DatetimeIndex(dfnew['Datetime']).month


# In[43]:


dfnew.head()


# In[44]:


dfnew['Month'].value_counts()


# In[46]:


#Analysing month wise commercial power consumption
Mpc=dfnew.groupby('Month')['PowerConsumption_Zone1'].sum()
Mpc=pd.DataFrame(Mpc)
Mpc.reset_index(inplace=True)
print(Mpc)


# In[47]:


plt.pie('PowerConsumption_Zone1',autopct='%1.1f%%',labels='Month',radius=2,data=Mpc)
plt.show()


# ### Conclusion: August month of 2017 has recorded highest amount of PowerConsumption_zone1

# In[48]:


Mpc=dfnew.groupby('Month')['PowerConsumption_Zone2'].sum()
Mpc=pd.DataFrame(Mpc)
Mpc.reset_index(inplace=True)
print(Mpc)


# In[49]:


plt.pie('PowerConsumption_Zone2',autopct='%1.1f%%',labels='Month',radius=2,data=Mpc)
plt.show()


# In[50]:


Mpc=dfnew.groupby('Month')['PowerConsumption_Zone3'].sum()
Mpc=pd.DataFrame(Mpc)
Mpc.reset_index(inplace=True)
print(Mpc)


# In[51]:


plt.pie('PowerConsumption_Zone3',autopct='%1.1f%%',labels='Month',radius=2,data=Mpc)
plt.show()


# In[52]:


Mpc=dfnew.groupby('Month')['Temperature'].sum()
Mpc=pd.DataFrame(Mpc)
Mpc.reset_index(inplace=True)
print(Mpc)


# In[53]:


plt.pie('Temperature',autopct='%1.1f%%',labels='Month',radius=2,data=Mpc)
plt.show()


# In[54]:


Mpc=dfnew.groupby('Month')['Humidity'].sum()
Mpc=pd.DataFrame(Mpc)
Mpc.reset_index(inplace=True)
print(Mpc)


# In[55]:


plt.pie('Humidity',autopct='%1.1f%%',labels='Month',radius=2,data=Mpc)
plt.show()


# In[56]:


Mpc=dfnew.groupby('Month')['WindSpeed'].sum()
Mpc=pd.DataFrame(Mpc)
Mpc.reset_index(inplace=True)
print(Mpc)


# In[57]:


plt.pie('WindSpeed',autopct='%1.1f%%',labels='Month',radius=2.5,data=Mpc)
plt.show()


# # Thank You !
