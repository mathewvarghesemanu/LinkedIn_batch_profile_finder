#!/usr/bin/env python
# coding: utf-8

# In[62]:


import pandas as pd
import os.path
from os import path
import webbrowser
# In[65]:


import pandas as pd
df=pd.read_csv("class.csv")
df.columns


# In[66]:


name_list=df["Name"]
name_list
#print(len(name_list))


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
start_index=0
if path.exists("checkpoint.txt"):
    resp=input("Do you want to continue where you left off?(y/n)")
    if resp in {'n','N'}:
        start_index=0
    elif resp in {'y','Y'}:
        start_index=0;
        with open ("checkpoint.txt") as f:
            index=f.readline()
        start_index=int(index)

for i,url in enumerate(url_name_list):
            if i <=start_index:
                continue
            webbrowser.open(url)
            input(url)
            with open ("checkpoint.txt",'w') as f:
                f.write(str(i))
            
