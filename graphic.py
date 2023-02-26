import kivy
import spotipy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import *
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.slider import Slider
from playlists import *
from get_id import *

spotify = None
playlist_name = None

class WockaShuffle(App):

    def __init__(self, new_spotify, **kwargs):
        super(WockaShuffle, self).__init__(**kwargs)
        self.spotify = new_spotify

    def build(self):
        
        def shuffle(instance):
            playlist_name = self.playlist_name
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
            shuffled_track_list = shuffle_tracks(categorized_tracks, playlist_length)
            shuffled_playlist = create_playlist(self.spotify, cur_user, shuffled_track_list, user_playlists, playlist_length, playlist_name)
            
        def button_selected(button):
            self.playlist_dropdown.select(button.text)
            self.playlist_name = button.text
            
        layout = FloatLayout(size_hint=(1, 1))
        
        self.playlist_dropdown = DropDown()
        # Loop through playlists adding to dropdown
        for i in self.spotify.current_user_playlists()["items"]:
            name = i["name"]
            self.btn = Button(text=f"{name}", height=44, size_hint_y=None)
            
            # With every new button, add a dropdown select function
            self.btn.bind(on_release=button_selected)
            self.playlist_dropdown.add_widget(self.btn)

        self.dropdown_button = Button(text="Select a playlist", pos_hint={"x":0.25, "y":0.8},size_hint=(.5, None))
        self.dropdown_button.bind(on_release=self.playlist_dropdown.open)
        self.playlist_dropdown.bind(on_select=lambda instance, x: setattr(self.dropdown_button, 'text', x))

        self.shuffle_button = Button(text="Shuffle", pos_hint={"x":0.25, "y":0}, size_hint=(.5, .5))
        self.shuffle_button.bind(on_press=shuffle)


        layout.add_widget(self.shuffle_button)
        layout.add_widget(self.dropdown_button)
        return layout
    
   

