"""Creating the base of the app, development in the dev branch"""
from kivy.app import App  
from kivy.properties import NumericProperty,ObjectProperty
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen,NoTransition

lights=0

class MenuScreen(Screen):
    light=NumericProperty(0)
    numberdisplay=[0]*5
    numberlabel='  '.join([str(x) for x in numberdisplay])
    def on_pre_enter(self, *args):
        self.light=lights
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

    def on_pre_enter(self, *args):
        self.light=lights
    #my_text=StringProperty("dark")
    def on_switch(self,Switch):
        if Switch.active==False:
            print("Dark Mode")
            global lights
            lights=0
            self.light=0
        else:
            print("Light Mode")
            lights=1
            self.light=1
    def go_home(self):
        print("Home button pressed")
        self.manager.current='home'

class HomeScreen(Screen):
    light=NumericProperty(0)
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

    def on_pre_enter(self, *args):
        if lights==1:
            self.light=1
        else:
            self.light=0

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