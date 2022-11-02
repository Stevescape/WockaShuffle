import spotipy
from spotipy.oauth2 import SpotifyOAuth
from get_id import get_id
from playlists import *
from graphic import WockaShuffle  
from kivy.app import App 

def main():
    # get_ids returns: [client_id, client_secret]
    if __name__ == "__main__":
        CLIENT_ID = get_id("CLIENT_ID")
        CLIENT_SECRET = get_id("CLIENT_SECRET") 
        REDIRECT_URI = get_id("REDIRECT_URI")
        auth = SpotifyOAuth(client_id = CLIENT_ID, 
                            client_secret = CLIENT_SECRET,
                            redirect_uri = REDIRECT_URI,
                            scope = "user-library-read, playlist-read-private, user-modify-playback-state")
        spotify = spotipy.Spotify(auth_manager=auth)

        WockaShuffle(spotify).run()

        
main()

