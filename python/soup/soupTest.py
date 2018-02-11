#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
"""
#with open('/var/www/html/simple.html') as html_file:
   soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify())
#match = soup.find('div', class_='footer')
#print(match)

# Grabbing first matching element with 'find' method
article = soup.find('div', class_='article')
#print(match)

headline = article.h2.a.text
print(headline)

summary = article.p.text
print(summary)

# Getting all matches with 'find_all' method
for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()
"""
source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

article = soup.find('article')

# print(article.prettify())
headline = article.h2.a.text
#print(headline)

summary = article.find('div', class_='entry-content').p.text
#print(summary)

vid_src = article.find('iframe', class_='youtube-player')['src']
#print(vid_src)

vid_id = vid_src.split('?')[0].split('/')[-1]
print(vid_id)