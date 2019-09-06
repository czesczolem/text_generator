# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs
import time
import sys


#
# url = 'https://www.tekstowo.pl/piosenki_artysty,taco_hemingway,alfabetycznie,strona,{}.html'

# text_url = 'https://www.tekstowo.pl/piosenka,taco_hemingway,sciany_maja_uszy.html'
def is_whitelisted(link):
    crawl_blacklist = ['https://www.tekstowo.pl/piosenka,taco_hemingway,22.html']
    return not link in crawl_blacklist


def make_request(url):
    r = requests.get(url)
    soup = bs(r.content, 'lxml')
    return soup

def get_artist_page(artist, page):
    main_page = 'https://www.tekstowo.pl/piosenki_artysty,{},alfabetycznie,strona,{}.html'.format(artist, page)
    soup = make_request(main_page)
    return soup

def gen_links_from_page(soup):
    base = 'https://www.tekstowo.pl'
    data = soup.find(attrs={"class": "ranking-lista"}).findAll('a')
    links = [a['href'] for a in data if a['href'].endswith('.html')]
    links = [base + l for l in links]
    return links

def gen_artist_links(artist):
    page = 1
    link_list  = []
    while True:
        soup = get_artist_page(artist, page)
        links = gen_links_from_page(soup)
        if links:
            link_list = link_list + links
            page += 1
        else:
            break
        time.sleep(2)
    return link_list

def get_song_text(soup):
    text = soup.find(attrs={"class": "song-text"})
    return text

art = sys.argv[1]
print art
link_list = gen_artist_links(art)
for link in link_list:
    if is_whitelisted(link):
        soup = make_request(link)
        print "getting {}".format(link)
        text = get_song_text(soup).text
        with open('rapsy/{}_text.txt'.format(art), 'a') as f:
            f.write(text.encode('utf-8'))
        time.sleep(2)

