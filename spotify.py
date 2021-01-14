import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import json
import time


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="",
                                               client_secret="",
                                               redirect_uri="https://kaganisildak.com",
                                               scope="user-read-currently-playing playlist-modify-public"))


def create_playlist(name):
    user_id = sp.me()['id']
    return sp.user_playlist_create(user_id,name)

def add_to_playlist(playlistid,trackid):
    tracksarray = []
    tracksarray.append("spotify:track:{}".format(trackid))
    return sp.playlist_add_items(playlistid,tracksarray)

def get_tracks(playlistid,offset=0):
    response = sp.playlist_items(playlistid,
                                offset=offset)
     
    return response                    



def track_finder(character):
    out = tuple
    results = sp.search(q=character, limit=50)
    for idx, track in enumerate(results['tracks']['items']):
        if track["name"][0] == str(character)[0]:
            out = (track["name"],track["id"])
            break
    return out


