import requests
import os
import os.path
from os import path
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from download import *

def collect_pics(website_url, web_prefix):
    URL = website_url#"https://mythicspoiler.com/newspoilers.html"
    pic_location = web_prefix#'https://mythicspoiler.com/{}'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find_all("div", class_="grid-container")[0]

    cards = results.find_all("div", class_="grid-card")

    pic_urls = []
    for card in cards:
        pic = card.find("img")
        filename = (pic.get('src')).strip()
        full_pic_url = web_prefix.format(filename)
        #pic_urls.append(full_pic_url)
        klsd = os.path.join("",full_pic_url.split("/")[-1])
        #print(path.exists("card_list/" + klsd))
        if path.exists("card_list/" + klsd):
            pass
        else:
            download(full_pic_url)
            pic_urls.append(full_pic_url)

    return pic_urls




