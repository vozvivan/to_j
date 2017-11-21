#!/usr/bin/python3.5m
from google import search
import urllib.request
from bs4 import BeautifulSoup

def google_scrape(url):
    thepage = urllib.request.urlopen(url)
    soup = BeautifulSoup(thepage, "html.parser")
    return soup.title.text

i = 1
query = 'заказ такси'
for url in search(query, stop=10):
    a = google_scrape(url)
    print (str(i) + ". " + a)
    print (url)
    print (" ")
    i += 1
