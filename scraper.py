#import libraries
import pandas as pd #The pandas library allows for data analysis and manipulation
import requests as requests # Requests is for making network connections
from bs4 import BeautifulSoup # BueatifulSoup is for extracting extracting data from HTML
from bs4 import NavigableString
from PIL import Image
from io import BytesIO


#Add a url and perform a fetch request
web_url = "https://www.ikea.com/us/en/cat/armoires-wardrobes-19053/" #the target website
fetched_page = requests.get(web_url) # Here we are fetching the page


models=[]
prices=[]
descriptions=[]
dimensions=[]
newDimensions=[]

beautifulSoup=BeautifulSoup(fetched_page.text, "html.parser") #using pythons default library html.parser alongside beautifulsoup to parse text
for item in beautifulSoup.find_all('div', attrs={'class': 'pip-product-compact'}):
    
    model = item.find('span', attrs={'pip-header-section__title--small notranslate'})
    whole_dollar = item.find('span', attrs={'pip-price__integer'})
    decimal_dollar= item.find('span', attrs={'pip-price__decimals'})
    description = item.find('span', attrs={'pip-header-section__description-text'})
    dimension = item.find('span',attrs={'pip-header-section__description-measurement'})

    models.append(model.text)
    prices.append("$ "+whole_dollar.text+decimal_dollar.text)
    descriptions.append(description.text)
   
df = pd.DataFrame({'Product Name': models, 'Price':prices, 'Description':descriptions})
df.to_csv('Armoires_&_Wardrobes.csv', index=False, encoding='utf-8')



