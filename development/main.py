"""Creating the base of the app, development in the dev branch"""
from kivy.app import App  
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

class MainScreen(Widget):
    pass

class MainScreenUI(Widget):
    pass

class LabsApp(App):
    def build(self):
        return MainScreenUI()

LabsApp().run()