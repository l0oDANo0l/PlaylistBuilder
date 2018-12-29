import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from merc_scrape import scrape_listing
import datetime
import configparser

# loads the config file
config = configparser.ConfigParser()
config.read('config.ini')

clientId = config['SPOTIFY']['CLIENT_ID']
clientSecret = config['SPOTIFY']['CLIENT_SECRET']

artists = scrape_listing()
print (artists)

username = config['SPOTIFY']['USER_ID']
scope = 'playlist-modify-private'
#https://open.spotify.com/user/126154079?si=kZOLviYwRBGgExs34FTIeA

client_credentials_manager = SpotifyClientCredentials(clientId, clientSecret)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
token = util.prompt_for_user_token(username, scope, clientId, clientSecret, 'https://example.com/callback/') #, scope, redirect_uri = 'https://example.com/callback/')
if not token:
    print ("Can't get token for", username)
    quit()

sp = spotipy.Spotify(auth=token)
playlist_name='local shows'
playlist_description='testing creating local shows playlist'
sp.trace_out = True
playlists = sp.user_playlist_create(username, playlist_name, public=False)  
print (playlists)
playlist_id = playlists["id"]
for artist in artists:  
    result = sp.search(artist, type='artist', market='us')
    # print (result)

    if len(result["artists"]["items"])==0:
        print ("could not find artist", artist)

    if len(result["artists"]["items"])==1:
        print ("found exact match for artist", artist)  
        artist_id = result["artists"]["items"][0]["id"]
        print (artist_id)
        tracks_list = sp.artist_top_tracks(artist_id)
        track_ids = [x["id"] for x in tracks_list["tracks"]]
        results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
        
    if len(result["artists"]["items"])>1:
        print ("found multiple matches for artist", artist)  
        for item in result["artists"]["items"]:
            print (item["name"])   


    # for item in result["artists"]["items"]:
    #     tracks_list = sp.artist_top_tracks(item["id"])
    #     track_ids = [x["id"] for x in tracks_list["tracks"]]
    #     results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)

