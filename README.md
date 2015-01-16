# python_scripts
Contains scripts written in python. (For automation, web scrapping)


###Script 1# : Junglee_scrapping

The aim of making this script is to find the product list and their corresponding prices from www.junglee.com. After running this script user will be prompted to enter the search term, then the script will search the product on junglee.com and will output all the products with their prices. I have used Python2.7.6 for web scrapping, 're' python libray for pattern searching and beautifulsoup Python package for parsing HTML documents.


####Directory structure

python_scripts
<pre><br/>
|<br/>
|---junglee_scrapping/<br/>
|	|<br/>
|	|---junglee_scrapping.py<br/>
|<br/>
|---README.md<br/><pre>


####Instructions
	
- To make this script run properly, you must install BeautifulSoup library first:

		`sudo pip install beautifulsoup`
		
- Now after cloning or downloading this script, locate the junglee_scrapping.py on terminal: 
		`cd /path/to/the/clone/repo/script`

- Now run the script using `python junglee_scrapping.py`

####Task completed : 
  - Fetched product list successfully
  - Fetched product price successfully
  - Integrated product list and price list into dictionary
  - Taking user input as a search term

####Need to be done :
  - Suggesting cheap product
