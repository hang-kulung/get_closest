"""Creating the base of the app, development in the dev branch"""
from kivy.app import App  
from kivy.properties import NumericProperty
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class NumberDisplay(StackLayout):
    #WHY TF did i use stacklayout? it doesn't work with grid layout? why?
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(5):
            l=Label(text="0",size_hint=(None,None),size=("20dp","20dp"),font_name= "fonts/Lcd.ttf",font_size= "30dp")
            self.add_widget(l)

class MenuScreen(BoxLayout):
    def Small(self):
        print("small button pressed")
    def Big(self):
        print("Big button pressed")
    def Clears(self):
        print("Clear button pressed")
    def Next(self):
        print("Next button pressed")

class Options(BoxLayout):
    light=NumericProperty(0)
    #my_text=StringProperty("dark")
    def on_switch(self,Switch):
        if Switch.active==False:
            print("Dark Mode")
            self.light=0
        else:
            print("Light Mode")
            self.light=1


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