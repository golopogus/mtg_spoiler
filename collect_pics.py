import requests
import os
import os.path
from os import path
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from download import *
from save_pic_as_txt import *

def collect_pics(website_url, web_prefix):
    URL = website_url
    pic_location = web_prefix
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find_all("div", class_="grid-container")[0]

    results.append(soup.find_all("div", class_="grid-container")[1])

    cards = results.find_all("div", class_="grid-card")

    pic_urls = []
    for card in cards:
        pic = card.find("img")
        filename = (pic.get('src')).strip()
        full_pic_url = web_prefix.format(filename)
        file_jpeg = os.path.join("",full_pic_url.split("/")[-1])
        file = open("pics.txt") 
        if full_pic_url in file.read():
            pass
        else:
            pic_urls.append(full_pic_url)
   #     if path.exists("card_list/" + file_jpeg):
   #         pass
   #     else:
    #        download(full_pic_url)
 #           pic_urls.append(full_pic_url)
    print(pic_urls)
    save_pic_as_txt(pic_urls)

    return pic_urls




