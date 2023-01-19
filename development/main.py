"""Creating the base of the app, development in the dev branch"""
from kivy.app import App  
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

class MainScreen(BoxLayout):
    pass

class LabsApp(App):
    pass

LabsApp().run()