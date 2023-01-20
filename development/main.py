"""Creating the base of the app, development in the dev branch"""
from kivy.app import App  
from kivy.properties import NumericProperty,ObjectProperty
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen,NoTransition

light=NumericProperty(0)
class NumberDisplay(StackLayout):
    #WHY TF did i use stacklayout? it doesn't work with grid layout? why?
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(5):
            l=Label(text="0",size_hint=(None,None),size=("20dp","20dp"),font_name= "fonts/Lcd.ttf",font_size= "30dp")
            self.add_widget(l)

class MenuScreen(Screen):
    def Small(self):
        print("small button pressed")
    def Big(self):
        print("Big button pressed")
    def Clears(self):
        print("Clear button pressed")
    def Next(self):
        print("Next button pressed")

class Options(Screen):
    light=NumericProperty(0)
    def __init__(self, **kwargs):
        super(Options, self).__init__(**kwargs)
    #my_text=StringProperty("dark")
    def on_switch(self,Switch):
        if Switch.active==False:
            print("Dark Mode")
            self.light=0
        else:
            print("Light Mode")
            self.light=1
    def go_home(self):
        print("Home button pressed")
        self.manager.get_screen('menu').light=NumericProperty(1)
        self.manager.current='home'
        


class HomeScreen(Screen):
    light=NumericProperty(0)
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

    def start(self):
        #Need s a jumper to page
        self.manager.current = 'menu'
        print("start button pressed")
    def Profile(self):
        #Needs a jumper to page
        print("Profile Button Pressed")
        pass
    def Options(self):
        self.manager.current="options"
        print("Options button Pressed")
        #Needs a jumper to page
        pass
class Manager(ScreenManager):  
    home = ObjectProperty(None)
    menu = ObjectProperty(None)
    options = ObjectProperty(None)

class LabsApp(App):
    def build(self):
        m = Manager(transition=NoTransition())
        return m

LabsApp().run()