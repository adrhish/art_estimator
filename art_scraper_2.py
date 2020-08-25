import time
import random

sleep = 0.1
 
#Looping over the artists on page letter_page of letter: 
for letter in ['A']: #add all the letters
    print(f'now starting letter {letter}')
    time.sleep( sleep )

    page_soup = BeautifulSoup(requests.get(f'http://www.findartinfo.com/english/{letter}/browse-by-artist.html').content,
                                       'html.parser')
    max_pages_for_letter = int(page_soup.find_all('a')[-15]['href'][-8:-5])
    
    for letter_page in range(21,max_pages_for_letter): 
        print(f'Total number of observations for far: {len(paintings)}')
        print(f'now starting page {letter_page} of letter {letter}... ...')
        
         
        #looping over all artists for the page:
        for j in range(49,49+60):
            
            try:
                artists_html = BeautifulSoup(requests.get(f'http://www.findartinfo.com/english/{letter}/browse-by-artist/page/{letter_page}.html').content,
                                           'html.parser')

                #fetches the link to access the artist_page
                URL_extend = artists_html.find_all('a', href=True)[j]['href']

                artist_html = BeautifulSoup(requests.get(f'http://www.findartinfo.com{URL_extend}').content,
                                           'html.parser')

                max_pages_artist = int(artist_html.find_all('h2')[0].text.strip(' \r\n ').split(' ')[19])

            except Exception as exception:
                print('Error for max artist pages:',exception)
                print(f'setting max_pages_artist manuallay to 5')
                max_pages_artist = 5
                time.sleep(2)
                
            for artist_page in range(1,max_pages_artist+1):
                
                time.sleep(sleep)
                
                try:
                    artists_paintings = int(artist_html.find_all('h2')[0].text.strip(' \r\n ').split(' ')[7])
                    if  artists_paintings < 5:
                        print(f'{j} has too few paintings ({artists_paintings}).')
                        continue
                    else:
                        #print('this artist has more than 5 paintings.')
                        max_paintings_per_page = min(int(soup_extended.find_all('h2')[0].text.strip(' \r\n ').split(' ')[7]),30)
                except: 
                    print('could not fetch number of paintings for artist.')
                    artists_paintings = 'Unknown'
                    max_paintings_per_page = 30
                    
                print(f'scraping artist {j} {artist_page}/{max_pages_artist} on page {letter_page} of letter {letter} ({artists_paintings} paintings)')
                artist_soup = BeautifulSoup(requests.get(f'http://www.findartinfo.com{URL_extend[:-5]}/page/{artist_page}.html', 
                                                   headers=headers, cookies=cookies).content, 'html.parser')
                for image_number in range(0,max_paintings_per_page): 
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
                        
                        
                        '''try:  
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
                            _dict['img available'] = 'n' '''
                            
                    except Exception as error:
                        print(error, f': painting has not been appended')
                        continue
            images_df = pd.DataFrame(paintings)
            print()
            
        
    print(f'Letter {letter} completed')
    images_df.to_csv(f'{letter}paintings_df.csv', index=False)
print('All letters completed.')
pd.images_df
    print(f'Letter {letter} completed')
    images_df.to_csv(f'{letter}paintings_df.csv', index=False)
print('All letters completed.')
images_df
