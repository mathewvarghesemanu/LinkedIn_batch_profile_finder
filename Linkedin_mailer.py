#!/usr/bin/env python
# coding: utf-8

#imports
import pandas as pd
import os.path
from os import path
import webbrowser
import pandas as pd
import re
import pyperclip

base_url="https://www.linkedin.com/search/results/all/?keywords="
uw_url="%20University"+"%20"+"of"+"%20"+"Washington"


def read_message():
    '''
    reads message.txt from file and returns it
    input : None
    output : Message<String>
    '''
    with open("message.txt",'r') as f:
        message=f.read()
    return message

def name_check(word):
    '''
    checks if the passed item is a name
    input : string
    output: word if word found, else None
    '''
    if re.search(r"^[A-Z]",word):
        return word
    else:
        return None

def clean_csv():
    '''
    cleans CSV and save
    input : None
    output : None
    ''' 
    df=pd.read_csv("class_raw.csv")
    raw_name_list=df['0']
    new_name_list=list(map(lambda word:name_check(word),raw_name_list))
    new_name_list=list(filter(None,new_name_list))
    unique_name_list=[]
    for item in new_name_list:
        if item not in unique_name_list:
            unique_name_list.append(item)
    new_name_list=unique_name_list    
    new_name_df=pd.DataFrame()
    new_name_df["Name"]=unique_name_list
    new_name_df.to_csv("class.csv")   

def get_start_index():    
    '''
    Checks if checkpoint exists and
    input : None 
    output : Start index
    ''' 
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
    return start_index

def open_browser(url):
    '''
    Open input url and takes user input
    input : Url<string>
    output : user input<string>
    '''
    # webbrowser.open(url)
    return input(url)


message=read_message()

if path.exists("class_raw.csv"):
    clean_csv()

start_index=get_start_index()

df=pd.read_csv("class.csv")
name_list=df["Name"]

new_name_list=list(map(lambda a: a.replace(" ","%20"),name_list))
url_name_list=list(map(lambda a: base_url+a, new_name_list))

print("Press q to exit at any point in time")
print("press a to add university of Washington to the search")
print("press s to search only using forst and last names")

for i,url in enumerate(url_name_list):
            if i <start_index:
                continue


            firstname=new_name_list[i].split("%20")[0]
            lastname=new_name_list[i].split("%20")[-1]
            invite=message.replace("<name>",firstname)
            pyperclip.copy(invite)
            with open ("checkpoint.txt",'w') as f:
                f.write(str(i))
            url_new=url+"%20University"+"%20"+"of"+"%20"+"Washington"
            user_response=open_browser(url_new)
            if user_response =='q' or user_response == 'Q':
                break
            elif user_response == 'a' or user_response == 'A':
                # url=url+"%20University"+"%20"+"of"+"%20"+"Washington"
                user_response=open_browser(url)
            elif user_response == 's' or user_response == 'S':
                url=base_url+firstname+'%20'+lastname
                user_response=open_browser(url)
                if user_response == 'a' or user_response == 'A':
                    url=url+uw_url
                    user_response=open_browser(url)

            
