# Importing python library for fetching Internet resource
import urllib2
import re
from BeautifulSoup import BeautifulSoup

url = "http://www.junglee.com/mn/search/junglee/ref=nb_sb_is\
s_cat_00000_3?url=search-alias%3Daps&field-keywords=asus+fonepad+7&rush=n"

response = urllib2.urlopen(url)
html = response.read()

#Custom function for finding particular tag with specific attribute

def findText(tag, attr, val, soup):
    ''' Accepts 4 parameters : tag - html tag name, attr - html tag attr
        , val - value of attribute, soup - containing html response. Returns the list of matching
        patterns'''
    #fetching required tag using beautifulSoup Method
    titles = soup.findAll(tag, attrs={attr : val})
    
    #Fetching content of the tag using regular expression
    match = re.findall(r'<'+tag+'[^>]*?>(.*?)</'+tag+'>', str(titles))
    
    return str(match)

#Creating beautifulsoup object
soup = BeautifulSoup(html)

#Calling fuction for finding text in html
products= findText('a', "class", "title", soup)
product_price = find_price('span', "class", "price", soup)

#Converting string into product list
product_list = products.split("',")

for each_product in product_list:
    print "Product Name : \n", each_product[2:], "\n"




    

