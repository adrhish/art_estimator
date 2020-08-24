'''
Username : palifa1229@ermailo.com

Password : BvEDAmYRtd3psV8

'''

import requests
import pandas as pd
from bs4 import BeautifulSoup
from requests import Session
import shutil
import re

cookies = {
    'LANGAUGE': 'english',
    '__RequestVerificationToken': 'P-XoVem8zlsPZsfy5tdKoq2YFNteg3Hnq0QD0A4OWI0T65ikEajMChQ9seYoC6iQzrltbIpjhNlemYRhhabhQuiC2gRHRnGD8qGPlwPYq8rkUk5cuEqLIA6SIviILSF2fl207IPjkEzmP6szgPh_-A2',
    'ASP.NET_SessionId': 'zovc0cio2yuw2pvkfrvpz5ny',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:79.0) Gecko/20100101 Firefox/79.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'http://www.findartinfo.com/english/list-prices-by-artist/119744/herman-hgg.html',
    'Upgrade-Insecure-Requests': '1',
}

response = requests.get('http://www.findartinfo.com/english/price-info/3871826/main.html', headers=headers, cookies=cookies)
soup = BeautifulSoup(response.content,'html.parser')


#TODO 
paintings = [] 

import time
import random

sleep = 0.2

time.sleep( sleep )
 
#Looping over the artists on page letter_page of letter: 
for letter in ['A']: #add all the letters
    print(f'now starting letter {letter}')
    time.sleep( sleep )

    page_soup = BeautifulSoup(requests.get(f'http://www.findartinfo.com/english/{letter}/browse-by-artist.html').content,
                                       'html.parser')
    max_pages_for_letter = int(page_soup.find_all('a')[-15]['href'][-8:-5])
    
    for letter_page in range(1,max_pages_for_letter): 
        print(f'now starting page {letter_page} of letter {letter}... ...')
            
        for j in range(49,49+61):
            print(f'scraping artist {j} on page {letter_page} of letter {letter}')

            #max_pages_for_artist = 
            try:
                soup = BeautifulSoup(requests.get(f'http://www.findartinfo.com/english/{letter}/browse-by-artist/page/{letter_page}.html').content,
                                           'html.parser')
                URL_extend = soup.find_all('a', href=True)[j]['href']
                #max_pages_artist = int(soup.find_all('h2')[0].text.strip(' \r\n ')[22:26])
                print(f'URL_extend: {URL_extend}')
            except Exception as exception:
                print('max pages',exception)
                continue
            for artist_page in range(1,4):
                #print(f'scraping page{artist_page} of artist {j} on page {letter_page} of letter {letter}')
                time.sleep(sleep)
                
                artist_soup = BeautifulSoup(requests.get(f'http://www.findartinfo.com{URL_extend[:-5]}/page/{artist_page}.html', 
                                                   headers=headers, cookies=cookies).content, 'html.parser')
                for image_number in range(0,31): 
                    try:
                        URL_pic = artist_soup.find_all('span', class_='linkgoogle')[image_number].find('a', href=True)['href']
                        response = requests.get(f'http://www.findartinfo.com{URL_pic}', headers=headers, cookies=cookies)
                        soup = BeautifulSoup(response.content,'html.parser')
                    except: 
                        continue
                    
                    _dict = {} 
                    #fetching the title of the picture
                    try:
                        title = soup.find_all('td')[35].string
                        _dict['title'] = title 
                        
                    #fetching the date of sale as string
                        date_sold = soup.find_all('td')[51].string
                        _dict['date_sold'] = date_sold
                        
                    #fetching the size of picture
                        size = soup.find_all('span')[1].contents[0]
                        _dict['size'] = size

                    #fetching the kind of the picture
                        kind =  soup.find_all('td')[37].string
                        _dict['kind'] = kind
                
                    #fetching the name of the artist
                        artist = soup.find_all('td')[33].string
                        _dict['artist'] = artist
                        
                    #signed
                        signed = soup.find_all('td')[41].string
                        _dict['signed'] = signed
                        
                    #stamped
                        stamped = soup.find_all('td')[43].string
                        _dict['stamped'] = stamped
                        
                    #inscribed
                        inscribed = soup.find_all('td')[45].string
                        _dict['inscribed'] = inscribed
                        
                    #dating 
                        dating = soup.find_all('td')[47].string
                        _dict['dating'] = dating
                        
                    #lot number
                        lot = soup.find_all('td')[49].string
                        _dict['lot_number'] = lot
                        
                    #auction house
                        auction_house = soup.find_all('td')[53].string
                        _dict['auction_house'] = auction_house
                        
                    #price_estimated
                        price_estimated = soup.find_all('td')[55].string
                        _dict['price_estimated'] = price_estimated
                    
                    #fetching the price as a string 
                        auction_result = soup.find_all('td')[57].string
                        _dict['auction_result'] = auction_result
                    
                    #premium
                        with_premium = soup.find_all('td')[59].string
                        _dict['with_premium'] = with_premium
                        
                        #counter += 1 
                        #print(f'{title} by {artist} appended')
                        paintings.append(_dict)
                        
                        try:  
                            # Open the url image, set stream to True, this will return the stream content.
                            r = requests.get(soup.find_all('img')[4].get('src'), stream = True)

                            # Check if the image was retrieved successfully
                            if r.status_code == 200:

                                # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
                                r.raw.decode_content = True
                                filename = f"{soup.find_all('td')[35].string} by {soup.find_all('td')[33].string}.jpg"

                                # Open a local file with wb ( write binary ) permission.
                                with open(filename,'wb') as f:
                                    shutil.copyfileobj(r.raw, f)
                                    #print('Image sucessfully Downloaded: ',filename)
                                    _dict['img available'] = 'y'
                            else:
                                #print(f'Failed to download image: {title} by {artist}')
                                _dict['img available'] = 'n'
                        except:
                            #print(f'Exception: Image unavailable: {title} by {artist}')
                            _dict['img available'] = 'n'
                            
                    except Exception as error:
                        print(error, f': painting has not been appended')
                        continue
            images_df = pd.DataFrame(paintings)
            
            print()
    print(f'Letter {letter} completed')
    
print('All letters completed.')