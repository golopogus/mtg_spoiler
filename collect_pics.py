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

    counter = 0
    found = False
    results = []
    pic_urls = []

    #print(len(soup.find_all("div", class_="grid-container")))
    while found == False:# and counter <= len(soup.find_all("div", class_="grid-container"))-1:


        results = soup.find_all("div", class_="grid-container")[counter]
        
        #results.append(soup.find_all("div", class_="grid-container")[1])

        cards = results.find_all("div", class_="grid-card")

        
        for card in cards:
            pic = card.find("img")
            filename = (pic.get('src')).strip()
            full_pic_url = web_prefix.format(filename)
            file_jpeg = os.path.join("",full_pic_url.split("/")[-1])
            file = open("pics.txt") 
            #print(full_pic_url)
            if full_pic_url in file.read():
                found = True
            else:
                pic_urls.append(full_pic_url)
        
        #print(found)
        counter += 1
        if counter > len(soup.find_all("div", class_="grid-container"))-1:
            found = True
   #     if path.exists("card_list/" + file_jpeg):
   #         pass
   #     else:
    #        download(full_pic_url)
 #           pic_urls.append(full_pic_url)
    
    save_pic_as_txt(pic_urls)

    return pic_urls




