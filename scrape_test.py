import requests
import csv
from bs4 import BeautifulSoup
from csv import writer


searchResults = requests.get('https://www.congress.gov/bill/116th-congress/senate-resolution/316?q=%7B%22search%22%3A%5B%22air+pollution%22%5D%7D&s=1&r=1')

soup = BeautifulSoup(searchResults.text, 'html.parser')

for billTextUrl in soup.find_all("h2"):
        print(billTextUrl)
        
        # print(billTextLink)