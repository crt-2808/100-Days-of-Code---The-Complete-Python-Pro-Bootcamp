from bs4 import BeautifulSoup
import requests
import os
import dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
dotenv.load_dotenv()

CLIENT_ID=os.getenv("Spotify_Client_ID")
SECRET_ID=os.getenv("Spotify_Client_Secret")
USER_NAME= os.getenv("Spotify_User_Name")
PLAYLIST_ID=os.getenv("Spotify_Playlist_ID")
song_urls=[]

#Create an user for spotify
sp=spotipy.Spotify(
    auth_manager=SpotifyOAuth (
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=CLIENT_ID,
        client_secret=SECRET_ID,
        show_dialog=True,
        cache_path="token.txt",
        username=USER_NAME
    )
)
user_id = sp.current_user()["id"]

#Ask for a date so you can scrap at billboard
date=input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

#Web Scrapping
link=f"https://www.billboard.com/charts/hot-100/{date}"
response=requests.get(url=f"{link}")
billboard_page=response.text
soup=BeautifulSoup(billboard_page, "html.parser")
song_titles=soup.select("li ul li h3")
song_names=[song.getText().strip() for song in song_titles]
#print(song_names)

#Look for songs at spotify
year=date.strip("-")[0]
for song in song_names:
    result=sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri=result["tracks"]["items"][0]["uri"]
        song_urls.append(uri)
    except IndexError:
        print(f"{song} does not exist in Spotify. Skipped")


playlist=sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
#print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"],items=song_urls, position=None)