import spotipy
from spotipy.oauth2 import SpotifyOAuth
from get_id import get_id
from playlists import get_playlist
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

        playlist_name = get_id("PLAYLIST_NAME")
        cur_user = spotify.current_user()["id"]
        print(cur_user)
        user_playlists = spotify.current_user_playlists()

        shuffled_playlist = []
        playlist_to_shuffle = get_playlist(user_playlists, playlist_name)
        print(playlist_to_shuffle)
        print("Run")
        WockaShuffle(spotify).run()

        
main()

