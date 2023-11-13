# This project is about getting the 100 most played songs for a specific week and create a Spotify playlist with those songs
# 1 Scraping the Billboard Hot 100
import requests
from bs4 import BeautifulSoup
songs_date = input('Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ')
URL = 'https://www.billboard.com/charts/hot-100/' + songs_date
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.select('li h3#title-of-a-story.c-title')
songs = []
# with open('./python-intermediate-projects/spotify-playlist/songs.txt', mode='w') as file:
for title in titles:
        # file.write(f"{title.getText().strip()}\n")
    songs.append(title.getText().strip())
# 2 Authentication with Spotify
import spotipy 
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = 'acf2de14c8404eb3870c747d1ca17061'
CLIENT_SECRET = '15bdeeaa008d4cc6bbce53b7e0edb210'
USERNAME = 'angulo141312'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=USERNAME,
    )
)

user_id = sp.current_user()["id"]
# 3 Search Spotify for the songs from Step 1
song_uris = []
year = songs_date.split('-')[0]

for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type='track')
    print(result)
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} does not exist in Spotify. Skipped")

# 4 Creating and adding to Spotify Playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{songs_date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)