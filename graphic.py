import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import *
from kivy.uix.floatlayout import FloatLayout

class WockaShuffle(App):

    def build(self):
        
        def pause(instance):
            print("I've been pressed")
        layout = FloatLayout(size=(200, 200))
        pause_button = Button(text="Pause", pos=(.5, .5), size_hint=(.5, .5))
        pause_button.bind(on_press=pause)
        layout.add_widget(pause_button)
        return layout
    
   

