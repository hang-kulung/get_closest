"""Creating the base of the app, development in the dev branch"""
from kivy.app import App  
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class NumberDisplay(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(5):
            l=Label(text="0",size_hint=(None,None),size=("20dp","20dp"),font_name= "fonts/Lcd.ttf",font_size= "30dp")
            self.add_widget(l)

class MenuButtons(GridLayout):
    def Small(self):
        print("small button pressed")
    def Big(self):
        print("Big button pressed")
    def Clears(self):
        print("Clear button pressed")
    def Next(self):
        print("Next button pressed")
class HomeScreen(GridLayout):
    def start(self):
        #Need s a jumper to page
        print("start button pressed")
    def Profile(self):
        #Needs a jumper to page
        print("Profile Button Pressed")
        pass
    def Options(self):
        print("Options button Pressed")
        #Needs a jumper to page
        pass
class LabsApp(App):
    pass

LabsApp().run()