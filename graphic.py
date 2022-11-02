import kivy
import spotipy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import *
from kivy.uix.floatlayout import FloatLayout

spotify = "temp"

class WockaShuffle(App):

    def __init__(self, new_spotify, **kwargs):
        super(WockaShuffle, self).__init__(**kwargs)
        self.spotify = new_spotify

    def build(self):
        
        def pause(instance):
            try:
                self.spotify.pause_playback()
            except spotipy.exceptions.SpotifyException:
                print("No Active Device")
        layout = FloatLayout(size=(200, 200))
        pause_button = Button(text="Pause", pos=(.5, .5), size_hint=(.5, .5))
        pause_button.bind(on_press=pause)
        layout.add_widget(pause_button)
        return layout
    
   

