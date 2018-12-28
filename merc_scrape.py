from bs4 import BeautifulSoup
from datetime import datetime
import urllib.request
import requests
from html.parser import HTMLParser
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials


def scrape_listing(requestDate = datetime.today(), pageNum = None, artists = []):
    date = requestDate.strftime('%Y-%m-%d')
    site = "https://www.portlandmercury.com/events/music/"+date
    if pageNum is not None: 
        site += '?page={pageNum}&view_id=events'.format(pageNum=pageNum)   # it works if page=1 but it's slow, leave it off 
    else:
        pageNum=1     # set it to 1 so we can increment it
    print ("scraping ", site)
    page = urllib.request.urlopen(site)
    soup = BeautifulSoup(page, 'html.parser')
    # rows = soup.find_all('div', class_='calendar-post row')
    # artists = []
    rows = soup.find_all('h3', class_="calendar-post-title")
    for row in rows:
        # print(row.find('a').text.lstrip().rstrip())
        text = row.find('a').text.lstrip().rstrip()
        # print (text.split(','))
        for artist in text.split(','):
            print(artist)
            artists.append(artist.rstrip().lstrip())
    # print (artists)
    # print (len(artists))   

    nextButtons = soup.find_all('li', class_="next")
    for nextButton in nextButtons:      # there should only be one, but whatever
        print ("Date: ", date)
        print("next:", nextButton.next)
        link = nextButton.find("a")
        print ("---------link--------------")
        print (link)
        if link is not None:
            linkText = link.attrs["href"]
            print ("link text")
            print (linkText)
            if date in linkText:
                print ('there is another page')
                pageNum+=1
                scrape_listing(requestDate, pageNum, artists)
        # if nextButton.next.attrs is not None:
        #     if date in nextButton.next.attrs["href"]:
        #         print ('there is another page')
        #         moreData = True
        #         # scrape_listing(requestDate, pageNum)
        # else:
        #     print ('that is all for this day')    
    return artists      # ,moreData  


# moreData = True
# pageNum = 0
# friday = datetime(2018,12,14)
# allArtists = scrape_listing(friday)
# print (allArtists)

    
 