import kivy
import spotipy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import *
from kivy.uix.floatlayout import FloatLayout
from playlists import *
from get_id import *

spotify = "temp"

class WockaShuffle(App):

    def __init__(self, new_spotify, **kwargs):
        super(WockaShuffle, self).__init__(**kwargs)
        self.spotify = new_spotify

    def build(self):
        
        def pause(instance):
            try:
                self.spotify.pause_playback()
            except spotipy.exceptions.SpotifyException as e:
                error_code = e.http_status
                if error_code == 404:
                    print("No Active Device")
                if error_code == 403:
                    print("Already Paused")

        def start(instance):
            try:
                self.spotify.start_playback()
            except spotipy.exceptions.SpotifyException as e:
                error_code = e.http_status
                if error_code == 404:
                    print("No Active Device")
                if error_code == 403:
                    print("Already Playing")

        def shuffle(instance):
            playlist_name = get_id("PLAYLIST_NAME")
            cur_user = self.spotify.current_user()["id"]
            print(cur_user)
            user_playlists = self.spotify.current_user_playlists()["items"]
            
            playlist_to_shuffle = get_playlist(user_playlists, playlist_name)
            playlist_length = playlist_to_shuffle["tracks"]["total"]
            playlist_id = playlist_to_shuffle["id"]

            # Tracks contains the outer shell of songs, 
            # it has meta data and video_thumbnail info.
            # You have to do tracks[int]["track"] to get the actual track
            tracks = get_tracks(self.spotify, playlist_id, playlist_length)
            categorized_tracks = categorize(tracks)
            shuffled_playlist = shuffle_tracks(categorized_tracks, playlist_length)
            for i in shuffled_playlist:
                print(f"{i[0]}:{i[2]}")
            
            
        layout = FloatLayout(size_hint=(1, 1))
        # Bottom Left
        pause_button = Button(text="Pause", pos_hint={"x":0, "y":0}, size_hint=(.5, .5))
        pause_button.bind(on_press=pause)
        # Bottom Right
        start_button = Button(text="Play", pos_hint={"x":0.5, "y":0}, size_hint=(.5, .5))
        start_button.bind(on_press=start)
        # Top Left
        shuffle_button = Button(text="Shuffle", pos_hint={"x":0, "y":0.5}, size_hint=(.5, .5))
        shuffle_button.bind(on_press=shuffle)

        layout.add_widget(pause_button)
        layout.add_widget(start_button)
        layout.add_widget(shuffle_button)
        return layout
    
   

