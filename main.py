import spotipy
from spotipy.oauth2 import SpotifyOAuth
from playlists import *
from graphic import WockaShuffle  
from kivy.app import App 

def main():
    # get_ids returns: [client_id, client_secret]
    if __name__ == "__main__":
        CLIENT_ID = "f59708637b0f46958f3a5ad18f926a46"
        CLIENT_SECRET = "068d885a0dc3448291303ffb49cbfd05"
        REDIRECT_URI = "http://localhost:8080/callback/"
        auth = SpotifyOAuth(client_id = CLIENT_ID, 
                            client_secret = CLIENT_SECRET,
                            redirect_uri = REDIRECT_URI,
                            scope = "user-library-read, playlist-read-private, \
                                user-modify-playback-state, user-library-modify,\
                                     playlist-modify-private, playlist-read-collaborative")
        spotify = spotipy.Spotify(auth_manager=auth)

        WockaShuffle(spotify).run()

        
main()

