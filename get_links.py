from bs4 import BeautifulSoup
import requests

URLs = ['https://nypost.com/news/' ,
        'https://www.usatoday.com/news/', 'https://www.msn.com/en-us/news/',
        'https://news.yahoo.com/?fr=sycsrp_catchall/','https://www.nbcnews.com/',
        'https://www.nfl.com/','https://www.foxnews.com/',
        'https://www.britannica.com/sports/football-soccer/', 
        'https://edition.cnn.com/','https://edition.cnn.com/' , 
        'https://www.nytimes.com/' , 'https://www.reuters.com/' , 
        'https://www.bbc.com/news/', 'https://en.wikipedia.org/wiki/CNN/' , 
        'https://en.wikipedia.org/wiki/BBC/' , 'https://en.wikipedia.org/wiki/The_Guardian/' , 
        'https://en.wikipedia.org/wiki/The_Sun_(United_Kingdom)/' ,'https://en.wikipedia.org/wiki/The_Times/' , 
        'https://en.wikipedia.org/wiki/The_Washington_Post/']



def get_links(main_link , links , total_links):
    
    for a in links :
        if a.get('href') and main_link:
            if a.get('href')[0] == "/" and main_link:
                if main_link[:-1] + a.get("href") in total_links:
                    continue
                total_links.append(main_link[:-1] + a.get("href"))
            elif a.get('href')[0] == '#':
                continue
            else :
                if a.get("href") in total_links:
                    continue
                total_links.append(a.get("href"))
    total_links.append(f"###")

def fetch(URLs):
    total_links = []
    for index, url in enumerate(URLs):
        try:
            r = requests.get(url.strip())
            soup = BeautifulSoup(r.content,'html.parser')
            total_links.append(url)
            links = soup.find_all('a')
            get_links(url , links , total_links)
        except :
            continue
    return total_links


all_links = fetch(fetch(URLs))
links = "" 
for a in all_links:
    if a:
        print(a)
        links+=a
        links+=f'\n'


my_file = open(r"./links"+'.txt',"w+" ,encoding='utf-8-sig')
my_file.write(links)
print(len(all_links))