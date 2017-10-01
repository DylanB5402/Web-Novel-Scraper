# -*- coding: utf-8 -*-
from lxml import html
import requests
from bs4 import BeautifulSoup

page = requests.get('https://parahumans.wordpress.com/table-of-contents/')
webpage = html.fromstring(page.content)
links = webpage.xpath('//a/@href')
links = links[11:317]
y=300
for x in range(1, len[links]):
    current = links[y]
    worm = requests.get(current)
    arc = worm.content
    soup = BeautifulSoup(arc, "lxml")
    text = soup.get_text()
    start = text.index("Next Chapter")
    end1 = text.index("Next Chapter")
    end = text.index("Next Chapter", end1 + 1)
    chapter = text[start:end]
    chapter = chapter.encode('utf-8',errors='ignore')
    current = current.encode('utf-8',errors='ignore')
    print(y)
    file = open("Worm3.txt","a") 
    file.write(current)
    file.write(chapter)
    file.close
    y += 1