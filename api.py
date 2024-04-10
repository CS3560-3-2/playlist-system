from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
import spotipy
from pprint import pprint

def getSong(song):
  results= sp.search(q="track:" + song, type="track", limit="1")
  songInfo = (results["tracks"]["items"][0]["id"], results["tracks"]["items"][0]["name"], results["tracks"]["items"][0]["artists"][0]["name"], 
            ms_to_mins_secs(results["tracks"]["items"][0]["duration_ms"]))
  sp.start_playback(uris=["spotify:track:" + songInfo[0]])
  return songInfo

def ms_to_mins_secs(ms):
    seconds = round((ms / 1000) % 60)
    minutes = int((ms / (1000 * 60)) % 60)
    return str(minutes) + ":" + str(seconds)

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")
scope = "user-read-playback-state,user-modify-playback-state"

sp = spotipy.Spotify(
        auth_manager=spotipy.SpotifyOAuth(
          client_id=client_id,
          client_secret=client_secret,
          redirect_uri=redirect_uri,    
          scope=scope, open_browser=False))

res = sp.devices()