import kivy
kivy.require('1.0.0')

from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text='Hello World')

if __name__ in ('__android__', '__main__'):
    MyApp().run()