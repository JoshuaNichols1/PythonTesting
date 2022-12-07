import spotipy
import requests
import json
from ytmusicapi import YTMusic
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-private,user-follow-modify,user-library-modify"

SPOTIPY_CLIENT_ID='7f2442a7ef094bff8163f12f04db8a34'
SPOTIPY_CLIENT_SECRET='1ea0aad429944fea81d9af7ac94e5652'
spotify_access_token = "BQBNcT2XXo2b9ZTyPugr1F34c6HYADPXWI2hBdPLcThp08vzU3SQiA4uJP7iug_GdYjtDam5P-Eyz0bjPSaYpRKNtU4kevIgklUmv8-gB240AkYrjWHngFFSzypI0Ul51qh1WP7ZAeHpF6oDVoWhAYhDPPMj_fIvkyLI4jM"
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
    sp.current_user_saved_tracks_add([track_id])
    done.append(track_id)
    result = requests.get(f"""https://api.spotify.com/v1/search?q=artist%3A{url_artist}&type=artist&limit=1&access_token={spotify_access_token}""")
    result = json.loads(result.text)
    found_artist = result["artists"]
    found_artist_further = found_artist["items"]
    for n in found_artist_further:
        artist_id = n["id"]
    sp.user_follow_artists([artist_id])