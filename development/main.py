"""Creating the base of the app, development in the dev branch"""
from kivy.app import App  
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label

class NumberDisplay(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(5):
            l=Label(text="0",size_hint=(None,None),size=("20dp","20dp"))
            self.add_widget(l)
class LabsApp(App):
    pass

LabsApp().run()