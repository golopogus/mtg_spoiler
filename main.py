from collect_pics import *
from create_html import *
from send_email_ses import *
from download import *
from save_pic_as_txt import *


def generate_pics(url,url_prefix):
    pic_urls = collect_pics(url,url_prefix)
    create_html(pic_urls)
    if len(pic_urls) > 0:
        send_email()

url = 'https://mythicspoiler.com/newspoilers.html'
url_prefix = 'https://mythicspoiler.com/{}'

generate_pics(url, url_prefix)


    