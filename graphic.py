import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import *

class WockaShuffle(App):

    def build(self):
        return Button(text="Pause")

