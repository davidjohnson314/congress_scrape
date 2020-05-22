import requests
import csv
from bs4 import BeautifulSoup
from csv import writer

#bill scraping loop
def billScrape(soup,writer):
    

    for sponsor in soup.find_all("table", class_="standard01"):
        sponsor_text = sponsor.find("a", target="_blank").get_text()
        #print(sponsor_text)

    
    for title in soup.find_all("h1", class_="legDetail"):
        title_text = title.get_text()
        #print(title_text)

    
    for name in soup.find_all("h2", class_="primary"):
        name_text = name.get_text()
        #print(name_text)


    #for tracker in soup.find_all("li", class_="first selected last"):
        #tracker_text = tracker.get_text()
        #print(tracker_text)

    # for tracker2 in soup.find_all("h3", class_="currentVersion"):
    #     tracker2_text = tracker2.find("span").get_text()
        # print(tracker2_text)


    writer.writerow([sponsor_text,title_text,name_text])

#csv writer
file = open('bills.csv', 'a')
writer = csv.writer(file)
writer.writerow(['Sponsor', 'Title', 'Name', 'Tracker'])

#link search
# userSearchTerms = input("type search terms:")
# userSearchFormatted = userSearchTerms.replace(" ", "+")
queryString = 'https://www.congress.gov/quick-search/legislation?wordsPhrases=' + "air+pollution" + '&wordVariants=on&congresses%5B%5D=115&congresses%5B%5D=114&congresses%5B%5D=113&congresses%5B%5D=112&congresses%5B%5D=111&legislationNumbers=&legislativeAction=&sponsor=on&representative=&senator=&searchResultViewType=expanded&KWICView=false'
#print(queryString)
searchResults = requests.get(queryString)

soupSearch = BeautifulSoup(searchResults.text, 'html.parser')

billUrlList = []
for billSearch in soupSearch.find_all("span", class_="result-heading"):
    billUrls = billSearch.find("a", href=True)
    billUrlList.append(billUrls['href'])
    
    # billUrlList2 = [billUrls]
    # getLinks = bill_search_links.get('href')
    # print(billUrlList)


for link in billUrlList:
    print(link)
    
    billPage = requests.get(link)
    
    soupBillPage = BeautifulSoup(billPage.text, 'html.parser')

    billScrape(soupBillPage,writer)


file.close()





# for line in file:
    # if 'Sponsor' not in line:
        # writer.writerow(['Sponsor', 'Title', 'Name', 'Tracker'])
    # break

# def add_to_csv(row):
    # with open('output.csv', 'a') as f:


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