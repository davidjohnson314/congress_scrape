import requests
import csv
from bs4 import BeautifulSoup
from csv import writer
import re

def textFinder(href):
        return href and re.compile("/text").search(href)

searchResults = requests.get('https://www.congress.gov/bill/116th-congress/senate-resolution/316?q=%7B%22search%22%3A%5B%22air+pollution%22%5D%7D&s=1&r=1')

soup = BeautifulSoup(searchResults.text, 'html.parser')

for billTextUrl in soup.find_all("a", href=textFinder):
        print(billTextUrl)
        if billTextUrl.contents[0] == "Text":
                print("done")
        print(billTextUrl.contents)
        
        # print(billTextLink)