#Canaan 2017

import urllib2
from bs4 import BeautifulSoup

import csv

from datetime import datetime


#Variable URL
SP_quote = 'https://www.bloomberg.com/quote/SPX:IND'

#BloombergQuotes
quote_page = ['https://www.bloomberg.com/quote/INDU:IND',
'https://www.bloomberg.com/quote/SPX:IND']

data = []
for pg in quote_page:
	page = urllib2.urlopen(pg)
	soup2 = BeautifulSoup(page,'html.parser')
	name_box2 = soup2.find('h1',attrs={'class':'name'})
	name2 = name_box2.text.strip()
	price_box2 = soup2.find('div',attrs={'class':'price'})
	price2 = price_box2.text.strip()
	time_box2 = soup2.find('div',attrs={'class':'price-datetime'})
	time2 = time_box2.text
	data.append((name2,price2,time2))


with open('Aggregate_Index.csv','a') as csv_file:
	writer2 = csv.writer(csv_file)
	for name2, price2, time2 in data:
		writer2.writerow([name2,price2,time2,datetime.now()])



#page HTML
page = urllib2.urlopen(SP_quote)



soup = BeautifulSoup(page,'html.parser')


#SP500Values
name_box = soup.find('h1',attrs={'class':'name'})
name = name_box.text.strip()

price_box = soup.find('div',attrs={'class':'price'})
price = price_box.text.strip()

time_box = soup.find('div',attrs={'class':'price-datetime'})
time = time_box.text.strip()

print name + " : $" + price + " " + time

with open('index.csv','a') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow([name,price,time,datetime.now()])
