from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import json
import time
import random

# ":",'--'
# "/",'___'




URLs = ['https://nypost.com/news/' ,
        'https://www.usatoday.com/news/','https://www.msn.com/en-us/news',
        'https://news.yahoo.com/?fr=sycsrp_catchall','https://www.nbcnews.com/',
        'https://www.nfl.com/','https://www.foxnews.com/',
        'https://www.britannica.com/sports/football-soccer', 
        'https://edition.cnn.com/','https://edition.cnn.com/' , 
        'https://www.nytimes.com/' , 'https://www.reuters.com/' , 
        'https://www.bbc.com/news', 'https://en.wikipedia.org/wiki/CNN' , 
        'https://en.wikipedia.org/wiki/BBC' , 'https://en.wikipedia.org/wiki/The_Guardian' , 
        'https://en.wikipedia.org/wiki/The_Sun_(United_Kingdom)' ,'https://en.wikipedia.org/wiki/The_Times' , 
        'https://en.wikipedia.org/wiki/The_Washington_Post' ]

def save(link , data):
    link=link.replace(":",'--')
    link = link.replace("/",'___')
    my_file = open(r"./input/"+link+'.txt',"w+" ,encoding='utf-8-sig')
    my_file.write(data)

def get_text(url , soup):
    try: 
        html = soup.body
        pageData = ""
        for text in html.strings:
            pageData+=text
            pass
    # print(pageData)
        save(url , pageData)
    except Exception as e:
        print(e)

total_links = []
for index, url in enumerate(URLs):
    # try :
        r = requests.get(url)
        soup = BeautifulSoup(r.content,'html.parser')
        links = soup.find_all('a')
        # print(f"Link : {url}")
        total_links.append(url)
        get_text(url, soup)
        for i,a in enumerate(links):
            if a.get('href'):
                if a.attrs["href"][0]=='#':
                    continue
                if a.attrs["href"][0]=='/':
                    try:
                        r = requests.get(url[:-1] + a.attrs["href"])
                        total_links.append(url[:-1] + a.attrs["href"])
                        soup = BeautifulSoup(r.content,'html.parser')
                        get_text(url[:-1] + a.attrs["href"], soup)
                        inner_links = soup.find_all('a')
                        for inner_a in inner_links:
                            # print(inner_a)
                            if inner_a.get('href'):
                                if inner_a.attrs["href"][0]=='#':
                                    continue
                                if inner_a.attrs["href"][0]=='/':
                                    if a.get('href')[0] == '/' :
                                        continue
                                    # print(a.get('href'))
                                    try :
                                        r = requests.get(a.get('href')[:-1] + inner_a.attrs["href"])
                                        soup = BeautifulSoup(r.content,'html.parser')
                                        get_text(a.get('href')[:-1] + inner_a.attrs["href"], soup)
                                        # print(a.get('href')[:-1] + inner_a.attrs["href"])
                                        total_links.append(a.get('href')[:-1] + inner_a.attrs["href"])
                                    except Exception as e:
                                        print(e)
                                else:
                                    try: 
                                        r = requests.get(inner_a.attrs["href"])
                                        soup = BeautifulSoup(r.content,'html.parser')
                                        total_links.append(inner_a.attrs["href"])
                                        print(inner_a.attrs["href"])
                                        get_text(inner_a.attrs["href"], soup)
                                    except Exception as e:
                                        print(e)
                                    # print(inner_a.attrs["href"])
                    except Exception as e:
                                    print(e)

                else:
                    try:
                        r = requests.get(a.attrs["href"])
                        soup = BeautifulSoup(r.content,'html.parser')
                        # print(a.attrs["href"])
                        total_links.append(a.attrs["href"])
                        get_text(a.attrs["href"], soup)


                        inner_links = soup.find_all('a')
                        for inner_a in inner_links:
                            if inner_a.get('href'):
                                if inner_a.attrs["href"][0]=='#':
                                    continue
                                if inner_a.attrs["href"][0]=='/':
                                    if a.get('href')[0] == '/' :
                                        continue
                                    try:
                                        r = requests.get(a.get('href')[:-1] + inner_a.attrs["href"])
                                        soup = BeautifulSoup(r.content,'html.parser')
                                        total_links.append(a.get('href')[:-1] + inner_a.attrs["href"])
                                        get_text(a.get('href')[:-1] + inner_a.attrs["href"], soup)
                                    except Exception as e:
                                        print(e)
                                    # print(a[:-1] + inner_a.attrs["href"])
                                else:
                                    if inner_a.get("href"):
                                        try :
                                            print(inner_a.get("href"))
                                            r = requests.get(inner_a.get("href"))
                                            soup = BeautifulSoup(r.content,'html.parser')
                                            total_links.append(inner_a.attrs["href"])
                                            get_text(inner_a.attrs["href"], soup)
                                            # print(inner_a.attrs["href"])
                                        except Exception as e:
                                            print(e)
                    except Exception as e:
                                    print(e)

    # except Exception as e:
    #     i+=1
        # print("Error" + str(e))
    #     continue

# print(len(total_links))


# my_file = open(r"./links.txt","w+" ,encoding='utf-8-sig')
# my_file.write(total_links)
# print(i)
# print(total+len(URLs))