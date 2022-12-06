import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from playlists import *
from graphic import WockaShuffle  
from kivy.app import App 

def main():
    # get_ids returns: [client_id, client_secret]
    CLIENT_ID = "f59708637b0f46958f3a5ad18f926a46"
    CLIENT_SECRET = "cbfe0157f7374d4aa11d2e66176bba4a"
    REDIRECT_URI = "http://localhost:8080/callback/"
    auth = SpotifyOAuth(client_id = CLIENT_ID, 
                        client_secret = CLIENT_SECRET,
                        redirect_uri = REDIRECT_URI,
                        cache_path = "../cache.txt",
                        scope = "user-library-read, playlist-read-private, \
                            user-modify-playback-state, user-library-modify,\
                                    playlist-modify-private, playlist-read-collaborative")
    token = auth.get_cached_token()
    spotify = spotipy.Spotify(oauth_manager=auth)

    WockaShuffle(spotify).run()

        
main()

