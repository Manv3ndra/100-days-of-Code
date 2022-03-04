from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find("div", class_="chart-results-list // lrv-u-padding-t-150 lrv-u-padding-t-050@mobile-max")
tag = song_names_spans.find_all("div", class_="o-chart-results-list-row-container")

song_names = []

top = soup.find("a", class_="c-title__link lrv-a-unstyle-link").get_text().strip()

for name in tag:
    try:
        song = name.find("h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only").get_text().strip()
        song_names.append(song)
    except AttributeError:
        song_names.append(top)

#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id="a65fc64a342142b7b65b2e96fa99a9b5",
        client_secret="e2487f42d8d1449e849cc36530a110c7",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
# print(user_id)

#Searching Spotify for songs by title
song_uris = []
# year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=song, type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"Billboard Top 100 {date}", public=False)
# print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print("Created and Added Songs to Playlist")