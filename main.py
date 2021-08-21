from collect_pics import *
from create_html import *
from send_email import *
from download import *


def generate_pics(url,url_prefix):
    pic_urls = collect_pics(url,url_prefix)
    create_html(pic_urls)
    #for pic_url in pic_urls:
     #   email_send(pic_url)
    if len(pic_urls) > 0:
        send_email()

url = 'https://mythicspoiler.com/newspoilers.html'
url_prefix = 'https://mythicspoiler.com/{}'

generate_pics(url, url_prefix)


    