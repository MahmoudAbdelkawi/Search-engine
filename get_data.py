from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import json
import time
import random
import os



# ":",'--'
# "/",'___'


path =r'D:\Project\big data scraping\InvertedIndexProblem\input'
list_of_files = []

for root, dirs, files in os.walk(path):
	for file in files:
		list_of_files.append(os.path.join(root,file))

file1 = open("links.txt", "r",encoding = "utf-8") 
links = file1.readlines()

def link_format(link):
    link=link.replace(":",'--')
    link = link.replace("/",'___')
    return link

def check_if_file_is_found(link):
    path = f'./input/{link}.txt'
    # print(r'./input/https--______nypost.com___news___.txt')
    isExist = os.path.exists(path)
    return isExist

def save_in_file(link , data):
    link = link_format(link)
    my_file = open(r"./input/"+link+'.txt',"w+" ,encoding='utf-8-sig')
    my_file.write(data)

# errors = []

for index , link in enumerate(links):
    # if index < len(list_of_files):
    #     continue
    try:
        link = str(link).strip().replace('\ufeff', '')
        if not check_if_file_is_found(link_format(link)):
            print(index)
            r = requests.get(link)
            soup = BeautifulSoup(r.content,'html.parser')
            html = soup.body
            pageData = ""
            for text in html.strings:
                pageData+=text
                pass
            save_in_file(link , pageData)
        else:
            continue
    except Exception as e :
        # errors.append(index)
        print(link)
        print(f"Error in Link {index+1}")

# ignore 2867