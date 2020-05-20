import requests
import csv
from bs4 import BeautifulSoup
from csv import writer

response = requests.get(
#'https://www.congress.gov/bill/115th-congress/senate-bill/2760?q=%7B%22search%22%3A%22air+pollution%22%7D&s=1&r=1'
'https://www.congress.gov/bill/115th-congress/senate-joint-resolution/21?q=%7B%22search%22%3A%22air+pollution%22%7D&s=1&r=2'
#'https://www.congress.gov/quick-search/legislation?wordsPhrases=air+pollution&wordVariants=on&congresses%5B%5D=115&congresses%5B%5D=114&congresses%5B%5D=113&congresses%5B%5D=112&congresses%5B%5D=111&legislationNumbers=&legislativeAction=&sponsor=on&representative=&senator=&searchResultViewType=expanded&KWICView=false'
)
response2 = requests.get(
'https://www.congress.gov/bill/115th-congress/senate-bill/987/text?format=txt&q=%7B%22search%22%3A%22air+pollution%22%7D&r=59&s=2'
)

soup = BeautifulSoup(response.text, 'html.parser')
soup2 = BeautifulSoup(response2.text, 'html.parser')
#soup_lxml = BeautifulSoup(response.text, 'lxml')
#soup_html5 = BeautifulSoup(response.text, 'html5lib')

everything = soup.find_all('html')
   
file = open('bills.csv', 'w')
writer = csv.writer(file)

writer.writerow(['Sponsor', 'Title', 'Name', 'Tracker'])
   

for bill_search in soup.find_all("span", class_="result-heading"):
    bill_search_link = bill_search.find("a", href=True)
    #print(bill_search_link['href'])
    
#sponsor = soup.find_all("table", class_="standard01")
for sponsor in soup.find_all("table", class_="standard01"):
    sponsor_text = sponsor.find("a", target="_blank").get_text()
    #print(sponsor_text)

#title = soup.find_all("h1", class_="legDetail")    
for title in soup.find_all("h1", class_="legDetail"):
    title_text = title.get_text()
    #print(title_text)

#name = soup.find_all("h2", class_="primary")
for name in soup.find_all("h2", class_="primary"):
    name_text = name.get_text()
    #print(name_text)


#for tracker in soup.find_all("li", class_="first selected last"):
    #tracker_text = tracker.get_text()
    #print(tracker_text)

#tracker2 = soup.find_all("h3", class_="currentVersion")    
for tracker2 in soup.find_all("h3", class_="currentVersion"):
    tracker2_text = tracker2.find("span").get_text()
    print(tracker2_text)
    
writer.writerow([sponsor_text,title_text,name_text,tracker2_text])
    
file.close()


#for bill in soup2.find('pre', id='billTextContainer'):
    #print(bill)

#for bill_data in everything:
    #bill_search = bill_data.find_all("span", class_="result-heading")
    #bill_search_link = bill_search.find("a", href=True)
    #sponsor_text = sponsor.find("a", target="_blank").get_text()
    #name_text = name.get_text()
    #title_text = title.get_text()
    #tracker2_text = tracker2.find("span").get_text()
    
    #print(sponsor_text + ' ' + name_text + ' ' + tracker2_text + ' ' + tracker2_text)
    

#writer.writerow


#with open('bills.csv', 'w') as csv_file:
    #csv_writer = writer(csv_file)
    #headers = ['Title']
    #csv_writer.writerow(headers)


#csv_writer.writerow([name])
#print(name)
    #for post in name:
        #title = post.get_text()
        
 #   print(post)
    
#for post in title:
 #   name = post.find(class_="legDetail").get_text()
  #  print(name)