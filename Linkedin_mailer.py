#!/usr/bin/env python
# coding: utf-8

# In[62]:


import pandas as pd
import os.path
from os import path
import webbrowser
import pandas as pd
import re

def name_check(word):
    if re.search(r"^[A-Z]",word):
        return word
            
def clean_csv():
    df=pd.read_csv("class_raw.csv")
    raw_name_list=df['0']
    new_name_list=list(map(lambda word:name_check(word),raw_name_list))
    new_name_list=list(filter(None,new_name_list))
    new_name_set=set(new_name_list)
    new_name_list=list(new_name_set)
    new_name_df=pd.DataFrame()
    new_name_df["Name"]=new_name_list
    new_name_df.to_csv("class.csv")   


if path.exists("class_raw.csv"):
    clean_csv()


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

base_url="https://www.linkedin.com/search/results/all/?keywords="
url_name_list=map(lambda a: base_url+a, new_name_list)
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

print("Press q to exit at any point in time")
print("press a to add university of Washington to the search")
print("press s to search only using forst and last names")


def open_browser(url):
    webbrowser.open(url)
    return input(url)


for i,url in enumerate(url_name_list):
            if i <=start_index:
                continue
            
            with open ("checkpoint.txt",'w') as f:
                f.write(str(i))
            user_response=open_browser(url)
            if user_response =='q' or user_response == 'Q':
                break
            elif user_response == 'a' or user_response == 'A':
                url=url+"%20University"+"%20"+"of"+"%20"+"Washington"
                user_response=open_browser(url)
            elif user_response == 's' or user_response == 'S':
                firstname=new_name_list[i].split("%20")[0]
                lastname=new_name_list[i].split("%20")[-1]
                url=base_url+firstname+'%20'+lastname
                user_response=open_browser(url)
                if user_response == 'a' or user_response == 'A':
                    url=url+"%20University"+"%20"+"of"+"%20"+"Washington"
                    user_response=open_browser(url)

            
