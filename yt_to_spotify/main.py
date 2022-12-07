import spotipy
import requests
import json
from ytmusicapi import YTMusic
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-private"

SPOTIPY_CLIENT_ID='7f2442a7ef094bff8163f12f04db8a34'
SPOTIPY_CLIENT_SECRET='1ea0aad429944fea81d9af7ac94e5652'
spotify_access_token = "BQCFa2vKFYJ4Vb8GTWzP0A8KcjmASrRz6axGU3p6o7lN66EPD-vA5kstC5q_O3NhoXSmRo_TBeB1CM_l0jgPfCxDVhvh6C4cEzeAjyLMp6o1b4KGXsnIQe8Fk0n8AE2-GC1HnkWDBLVGOwoFKK9qMpPJVHQbko6TyjM8dRM"
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
yt = YTMusic()
search_results = yt.get_playlist('PLW2yev_gAPHJ99aW4kHYWo_sQkh7e0K9J', limit=953)
tracks = list(search_results["tracks"])
done = []
for i in tracks:
    artists = i["artists"]
    for person in artists:
        artist = person["name"]
        break
    url_artist = []
    title = i["title"]
    for word in artist.split():
        url_artist.append(word)
    url_artist = '+'.join(url_artist)
    url_word = []
    for word in title.split():
        url_word.append(word)
    cont = True
    iterator = 0
    title_arr = []
    while cont == True and iterator < len(url_word):
        if str.__contains__(url_word[iterator], "feat.") == False:
            title_arr.append(url_word[iterator])
        else:
            cont = False
        iterator += 1
    url_word = '+'.join(title_arr)
    result = requests.get(f"""https://api.spotify.com/v1/search?q=track%3A{url_word}%20artist%3A{url_artist}&type=track,artist&limit=1&access_token={spotify_access_token}""")
    result = json.loads(result.text)
    found_track = result["tracks"]
    if found_track["total"] == 0:
        result = requests.get(f"""https://api.spotify.com/v1/search?q=track%3A{url_word}&type=track,artist&limit=1&access_token={spotify_access_token}""")
        data = json.loads(result.text)
        found_track = data["tracks"]
    found_track_further = found_track["items"]
    for n in found_track_further:
        track_id = n["id"]
    sp.playlist_add_items("5d8GiPsKFrWho9LxqDSZQT", [track_id], position=None)
    done.append(track_id)