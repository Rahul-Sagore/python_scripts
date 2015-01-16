# Importing python library for fetching Internet resource and pattern searching
import urllib2
import re
from BeautifulSoup import BeautifulSoup

print "Welcome to Junglee.com web scrapping!\n"
usr_input = raw_input("Enter your search term : ")
print "processing ..."

inp = usr_input.split()
format_input = "+".join(inp)

url2 = "http://www.junglee.com/mn/search/junglee/ref=nb_sb_is\
s_cat_00000_3?url=search-alias%3Daps&field-keywords="+format_input+"&rush=n"


#Grabbing Html from the url
response = urllib2.urlopen(url2)
html = response.read()

#Custom function for finding particular tag with specific attribute
def get_product(tag, attr, val, soup):
    ''' Accepts 4 parameters : tag - html tag name, attr - html tag attr
        , val - value of attribute, soup - containing html response. Returns the list of matching
        patterns'''
    #fetching tag using beautifulSoup Method
    titles = soup.findAll(tag, attrs={attr : val})
    
    #Fetching content of the tag using regular expression
    match = re.findall(r'<'+tag+'[^>]*?>(.*?)</'+tag+'>', str(titles))
    
    return str(match)

#Custom function for getting price
def get_price(price_text):
    match = re.findall(r'</span[^>]*?>(.*?)</span>', str(price_text))
    return str(match)

def str_to_list(string):
    return string.split("',")

#Creating beautifulsoup object
soup = BeautifulSoup(html)

#Calling fuction for finding text in html
products= get_product('a', "class", "title", soup)

product_price = soup.findAll('span', attrs={'class':'price'})
prices = get_price(product_price) #for removing innerHTml

#Converting string into product list
product_list = str_to_list(products)
price_list = str_to_list(prices)

# Mapping of product_list and price_list into dictionary
prod_dic = dict(zip(product_list, price_list))

# Finally printing the values
for k, v in prod_dic.items():
    print "Product Name : \n", k[2:], "\nPrice : ", v[10:], "\n"

    

