from kivy.app import App  
from kivy.properties import NumericProperty,ObjectProperty,StringProperty,BooleanProperty
from kivy.uix.screenmanager import ScreenManager, Screen,NoTransition
import random
import os

"""Discontinued from this version, progress to be made on the last screen and debugs on it not working on the actual phone."""
lights=0

class MenuScreen(Screen):
    light=NumericProperty(0)
    available_numbers=[0]*5
    counter=0
    enable=BooleanProperty(True)
    available_numbers_label=StringProperty('  '.join([str(x) for x in available_numbers]))
    def on_pre_enter(self, *args):
        self.light=lights
    def Small(self):
        print("Small button pressed")
        if self.counter < len(self.available_numbers):
            self.available_numbers[self.counter] = random.randint(1,9)
            self.counter+=1
            self.available_numbers_label='  '.join([str(x) for x in self.available_numbers])
        else:
            self.enable=False
    def Big(self):
        print("Big button pressed")
        if self.counter < len(self.available_numbers):
            self.available_numbers[self.counter] = random.randint(10,99)
            self.counter+=1
            self.available_numbers_label='  '.join([str(x) for x in self.available_numbers])
        else:
            self.enable=False
    def Clears(self):
        print("Clear button pressed")
        self.available_numbers=[0]*5
        self.counter=0
        self.available_numbers_label='  '.join([str(x) for x in self.available_numbers])
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
        self.light=lights

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