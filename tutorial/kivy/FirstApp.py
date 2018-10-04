import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.button import Label

class FirstKivyApp(App):

    def builld(self):
        return Label(text="Hello Kivy")

helloKivy = FirstKivyApp()

helloKivy.run()