import spotipy
import requests
import json
from ytmusicapi import YTMusic
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

scope = "user-follow-read,user-follow-modify"

SPOTIPY_CLIENT_ID='7f2442a7ef094bff8163f12f04db8a34'
SPOTIPY_CLIENT_SECRET='1ea0aad429944fea81d9af7ac94e5652'
spotify_access_token = "BQCFa2vKFYJ4Vb8GTWzP0A8KcjmASrRz6axGU3p6o7lN66EPD-vA5kstC5q_O3NhoXSmRo_TBeB1CM_l0jgPfCxDVhvh6C4cEzeAjyLMp6o1b4KGXsnIQe8Fk0n8AE2-GC1HnkWDBLVGOwoFKK9qMpPJVHQbko6TyjM8dRM"
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
yt = YTMusic("headers_auth.json")
subs = yt.get_library_artists()
for i in subs:
    result = requests.get(f"""https://api.spotify.com/v1/search?q=artist%3A{i["artist"]}&type=artist&limit=1&access_token={spotify_access_token}""")
    result = json.loads(result.text)
    found_artist = result["artists"]
    found_artist_further = found_artist["items"]
    for n in found_artist_further:
        artist_id = n["id"]
    print(artist_id)
    sp.user_follow_artists(artist_id)