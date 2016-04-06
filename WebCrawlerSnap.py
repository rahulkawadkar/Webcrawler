import requests
from bs4 import BeautifulSoup


def mouthsnap_spider(max_pages):
    page = 1
    while page <= max_pages:
        #page = 1
        url = 'http://www.mouthshut.com/product-reviews/Snapdeal-com-reviews-925602969-sort-MsDate-order-d-page-' + str(page)
        print (url)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'id': 'ctl00_ctl00_ctl00_ContentPlaceHolderHeader_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl03_lnkTitle'}):
            href3 = link.get('href')
            title3 = link.string
            #print (href3)
            print (title3)
        for link in soup.findAll('a', {'id': 'ctl00_ctl00_ctl00_ContentPlaceHolderHeader_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl01_lnkTitle'}):
            href1 = link.get('href')
            title1 = link.string
            #print (href1)
            print (title1)
        for link in soup.findAll('a', {'id': 'ctl00_ctl00_ctl00_ContentPlaceHolderHeader_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl02_lnkTitle'}):
            href2 = link.get('href')
            title2 = link.string
            #print (href1)
            print (title2)
        for link in soup.findAll('a', {'id': 'ctl00_ctl00_ctl00_ContentPlaceHolderHeader_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl04_lnkTitle'}):
            href1 = link.get('href')
            title4 = link.string
            #print (href1)
            print (title4)
        for link in soup.findAll('a', {'id': 'ctl00_ctl00_ctl00_ContentPlaceHolderHeader_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl05_lnkTitle'}):
            href5 = link.get('href')
            title5 = link.string
            #print (href1)
            print (title5)
        for link in soup.findAll('a', {'id': 'ctl00_ctl00_ctl00_ContentPlaceHolderHeader_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl06_lnkTitle'}):
            href6 = link.get('href')
            title6 = link.string
            #print (href1)
            print (title6)
        for link in soup.findAll('a', {'id': 'ctl00_ctl00_ctl00_ContentPlaceHolderHeader_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl07_lnkTitle'}):
            href7 = link.get('href')
            title7 = link.string
            #print (href1)
            print (title7)
        for link in soup.findAll('a', {'id': 'ctl00_ctl00_ctl00_ContentPlaceHolderHeader_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl08_lnkTitle'}):
            href8 = link.get('href')
            title8 = link.string
            #print (href1)
            print (title8)
        for link in soup.findAll('a', {'id': 'ctl00_ctl00_ctl00_ContentPlaceHolderHeader_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl09_lnkTitle'}):
            href9 = link.get('href')
            title9 = link.string
            #print (href1)
            print (title9)
        for link in soup.findAll('a', {'id': 'ctl00_ctl00_ctl00_ContentPlaceHolderHeader_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl10_lnkTitle'}):
            href10 = link.get('href')
            title10 = link.string
            #print (href1)
            print (title10)
        page += 1



mouthsnap_spider(100)


