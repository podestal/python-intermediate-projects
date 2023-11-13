# This project is about getting the 100 most played songs for a specific week and create a Spotify playlist with those songs
# 1 Scraping the Billboard Hot 100
import requests
from bs4 import BeautifulSoup
songs_date = input('Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ')
URL = 'https://www.billboard.com/charts/hot-100/' + songs_date
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.select('li h3#title-of-a-story.c-title')
with open('./python-intermediate-projects/spotify-playlist/songs.txt', mode='w') as file:
    for title in titles:
        file.write(f"{title.getText().strip()}\n")
# 2 Authentication with Spotify
# 3 Search Spotify for the songs from Step 1
# 4 Creating and adding to Spotify Playlist