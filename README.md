# PlaylistBuilder
Scrapes the mercury music listings and makes a spotify playlist for you.

To use create a config.ini file. The format should be like:

; config.ini
[SPOTIFY]
CLIENT_ID = $YOUR_API_CLIENT_ID
CLIENT_SECRET = $YOUR_API_CLIENT_SECRET
USER_ID = $YOUR_SPOTIFY_ACCOUNT_ID


Then do a:
>pip -r requirements.txt
>python merc_scrape.py
