#!/usr/bin/env python
# coding: utf-8

# In[62]:


import pandas as pd


# In[65]:


import pandas as pd
df=pd.read_csv("class.csv")
df.columns


# In[66]:


name_list=df["Name"]
name_list
print(len(name_list))


# In[67]:


new_name_list=map(lambda a: a.replace(" ","%20"),name_list)
new_name_list=list(new_name_list)
new_name_list


# In[69]:


url_name_list=map(lambda a: "https://www.linkedin.com/search/results/all/?keywords="+a, new_name_list)
url_name_list=list(url_name_list)
url_name_list


# In[70]:


# df["new"]=url_name_list
df.shape


# In[ ]:


import webbrowser
for url in url_name_list:
    webbrowser.open(url)
    input(url)

