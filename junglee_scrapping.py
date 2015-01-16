# Importing python library for fetching Internet resource
import urllib2
# Importing beautifulsoup for pattern searching
from BeautifulSoup import BeautifulSoup

url = "http://www.junglee.com/mn/search/junglee/ref=nb_sb_is\
s_cat_00000_3?url=search-alias%3Daps&field-keywords=asus+fonepad+7&rush=n"

response = urllib2.urlopen(url)
html = response.read()

#Creating beautifulsoup object
soup = BeautifulSoup(html)

product_title = str(soup.find('a',attrs={"class":"title"}))
product_title = str(soup.find('span',attrs={"class":"list"}))

print product_title.split('">')[1]


    

