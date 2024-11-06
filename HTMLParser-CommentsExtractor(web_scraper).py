
##########################################################
##
## Auth: Ziv7
##
## Desc: Web Scraping Tool.
##       Extract & parse the comments in the web page by given a URL.
##       Can be use to reveal private comment of developer as credentials, used tools etc (information security wise). 
##
## Files: HTMLParser-CommentsExtractor(web_scraper).py
###########################################################


from bs4 import BeautifulSoup as BS
from bs4 import Comment

from urllib.request import urlopen

response = urlopen('https://data.gov/')
html = response.read()


soup=BS(html,'html.parser')
comments=soup.find_all(string=lambda text:isinstance(text,Comment))
for c in comments:
    print (c)
    print ("===========")

