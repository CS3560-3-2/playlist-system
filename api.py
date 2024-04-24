from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
import spotipy
from pprint import pprint

def getSong(song):
  #search for the top 10 result of the given input
  results = sp.search(q="track:" + song, type="track", limit="10")
  songs = []

  #each row in tracks is the id, track name, artist name, and duration of each of the top 10 tracks
  for tracks in range(len(results["tracks"]["items"])):
    songs.append((results["tracks"]["items"][tracks]["id"], results["tracks"]["items"][tracks]["name"], results["tracks"]["items"][tracks]["artists"][0]["name"], 
            results["tracks"]["items"][tracks]["duration_ms"]))
  return songs

def playSong(num):
   #plays the song corresponding to the id
   sp.start_playback(uris=["spotify:track:" + str(num)])

def pauseSong():
   sp.pause_playback()

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