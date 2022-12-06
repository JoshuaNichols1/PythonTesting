import spotipy
import requests
import json
from ytmusicapi import YTMusic
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-private"

SPOTIPY_CLIENT_ID='7f2442a7ef094bff8163f12f04db8a34'
SPOTIPY_CLIENT_SECRET='1ea0aad429944fea81d9af7ac94e5652'
spotify_access_token = "BQBRV216YYcA3X2EYILZ8-DRQEvRy4IM_7q-6m5rPb4PwpvbASBXsKAL7e49Bu-bsBWO2lZNalRRCyCH7WTEA9ETTyd62y0AwrFpRyTdjciDfi-1xdVGFgu9kg00K7nOwXYNiN31gufe4rDMhJqJqYRHkjlGP-hIEud1R9o"
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
# auth_manager=auth_manager,
yt = YTMusic()
# playlists = yt.get_library_playlists()
# print(playlists)
# playlistId = yt.create_playlist('test', 'test description')
search_results = yt.get_playlist('PLW2yev_gAPHJ99aW4kHYWo_sQkh7e0K9J', limit=953)
tracks = list(search_results["tracks"])
done = []
for i in tracks:
    artists = i["artists"]
    for person in artists:
        artist = person["name"]
        break
    # query = f'{i["title"]} {artist}'
    # result = sp.search(q=query, type='track', limit=1)
    # result = sp.search(q=f'track:"{i["title"]}"', limit=1, offset=0, type='track', market=None)
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
    # print(found_track)
    # print("")
    found_track_further = found_track["items"]
    for n in found_track_further:
        track_id = n["id"]
    # if track_id not in done:
    sp.playlist_add_items("5d8GiPsKFrWho9LxqDSZQT", [track_id], position=None)
    done.append(track_id)
    
    # %20album:"{album_name}"
# print(sp.search(q=f"track:{", limit=10, offset=0, type='track', market=None))
# print(search_results[0])
# yt.add_playlist_items(playlistId, [search_results[0]['videoId']])