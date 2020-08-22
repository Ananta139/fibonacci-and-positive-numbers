#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
get_ipython().run_line_magic('matplotlib', 'inline')
data=pd.read_csv("datasets_727551_1263738_heart_failure_clinical_records_dataset.csv")


# In[9]:


data=pd.read_csv("datasets_727551_1263738_heart_failure_clinical_records_dataset.csv")


# In[10]:


data.head()


# In[11]:


a=data.iloc[3,1:].values


# In[21]:


#reshaping
a=a.reshape(3,4).astype('uint8')
plt.imshow(a)


# In[22]:


#preparing the data
df_x=data.iloc[:,1:]
df_y=data.iloc[:,0]


# In[25]:


#creating test
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size = 0.2, random_state=4)


# In[26]:


x_train.head()


# In[27]:


rf=RandomForestClassifier(n_estimators=100)


# In[28]:


rf.fit(x_train, y_train)


# In[29]:


pred=rf.predict(x_test)


# In[30]:


pred


# In[31]:


s=y_test.values
count=0
for i in range (len(pred)):
    if pred[i]==s[i]:
        count=count+1
    


# In[32]:


count


# In[33]:


len(pred)


# In[ ]:




