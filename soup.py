import requests
import csv
from bs4 import BeautifulSoup
from csv import writer

#bill scraping loop
    # csv writer
    # bill txt writer
def billScrape(soup,writer,billPage):
    

    for sponsor in soup.find_all("table", class_="standard01"):
        sponsor_text = sponsor.find("a", target="_blank").get_text()
        #print(sponsor_text)

    
    for title in soup.find_all("h1", class_="legDetail"):
        title_text = title.get_text()
        #print(title_text)

    
    for name in soup.find_all("h2", class_="primary"):
        # name_text = name.get_text()
        name_text = name.contents[1]
        print(name_text)


    #for tracker in soup.find_all("li", class_="first selected last"):
        #tracker_text = tracker.get_text()
        #print(tracker_text)


    for tracker2 in soup.find_all("h3", class_="currentVersion"):
        tracker2_text = tracker2.find("span").get_text()
        # print(tracker2_text)


    index = billPage.find('?')
    print(billPage[0:index-1]+'/text?format=txt')
    billTextUrl = billPage[0:index-1]+'/text?format=txt'


    billTextGet = requests.get(billTextUrl)
    soupBillText = BeautifulSoup(billTextGet.text, 'html.parser')


    # billTextLink = [0]
    # for billTextUrl in soup.find_all("ul", _class="cdg-summary-wrapper-list"):
    #     billTextUrl2 = billTextUrl.find("a", href=True)
    #     billTextLink = billTextUrl2['href']
    #     print(billTextLink)
    # billTextSearch = requests.get(billTextLink)

    # soupBillText = BeautifulSoup(billTextSearch.text, 'html.parser')


    billText = soupBillText.find('pre', id='billTextContainer')
    billText2 = billText.get_text()


    BillTxt = open(name_text + ".txt", "a")
    BillTxt.write(billText2)
    BillTxt.close()


    writer.writerow([name_text,sponsor_text,title_text,tracker2_text])



def main():
    #csv writer
    file = open('bills.csv', 'a')
    writer = csv.writer(file)
    writer.writerow(['Name', 'Sponsor', 'Title', 'Tracker'])

    #link search
    userSearchTerms = input("type search terms:")
    userSearchFormatted = userSearchTerms.replace(" ", "+")
    queryString = 'https://www.congress.gov/quick-search/legislation?wordsPhrases=' + userSearchFormatted + '&wordVariants=on&congresses%5B%5D=115&congresses%5B%5D=114&congresses%5B%5D=113&congresses%5B%5D=112&congresses%5B%5D=111&legislationNumbers=&legislativeAction=&sponsor=on&representative=&senator=&searchResultViewType=expanded&KWICView=false'
    #print(queryString)
    searchResults = requests.get(queryString)

    soupSearch = BeautifulSoup(searchResults.text, 'html.parser')



    billUrlList = []
    for billSearch in soupSearch.find_all("li", class_="expanded"):
        billUrls1 = billSearch.find("span", class_="result-heading")
        billUrls2 = billUrls1.find("a", href=True)
        billUrlList.append(billUrls2['href'])
        
        # billUrlList2 = [billUrls]
        # getLinks = bill_search_links.get('href')
        # print(billUrlList)


    for link in billUrlList:
        print(link)
        
        billPage = requests.get(link)
        
        soupBillPage = BeautifulSoup(billPage.text, 'html.parser')

        billScrape(soupBillPage,writer,link)


    file.close()

if __name__ == '__main__':
    main()

