from kivy.app import App  
from kivy.properties import NumericProperty,ObjectProperty,StringProperty,BooleanProperty,ListProperty
from kivy.uix.screenmanager import ScreenManager, Screen,NoTransition
import random
import os

lights=0
available_numbers_global=[0]*5
diffs=0

class ResultScreen(Screen):
    light=NumericProperty(0)
    diff=NumericProperty(0)

    def on_pre_enter(self,):
        self.light=lights
        self.diff=diffs

    def take_me_home_country_roads(self):
        global available_numbers_global
        available_numbers_global=[0]*5
        self.manager.current='home'

    def extrawork(self):
        self.manager.current='menu'

class GameScreen(Screen):
    light=NumericProperty(0)
    goal=NumericProperty(0)
    resulting_label=StringProperty('')
    available_numbers=ListProperty(available_numbers_global)
    disabled_one=BooleanProperty(False)
    disabled_two=BooleanProperty(False)
    disabled_three=BooleanProperty(False)
    disabled_four=BooleanProperty(False)
    disabled_five=BooleanProperty(False)

    def on_pre_enter(self):
        self.light=lights
        self.available_numbers=available_numbers_global
        self.goal=random.randint(100, 999)

    def on_leave(self):
        self.goal=random.randint(100, 999)
        GameScreen().clear()
        
    #all numbers
    def addcalcone(self):
        self.disabled_one=True
        self.resulting_label+=str(self.available_numbers[0])
        print(self.resulting_label)

    def addcaltwo(self):
        self.disabled_two=True
        self.resulting_label+=str(self.available_numbers[1])
        print(self.resulting_label)

    def addcalthree(self):
        self.disabled_three=True
        self.resulting_label+=str(self.available_numbers[2])
        print(self.resulting_label)

    def addcalfour(self):
        self.disabled_four=True
        self.resulting_label+=str(self.available_numbers[3])
        print(self.resulting_label)

    def addcalfive(self):
        self.disabled_five=True
        self.resulting_label+=str(self.available_numbers[4])
        print(self.resulting_label)

    #all symbols
    def addsymbols(self,type):
        print(f"{type} button pressed")
        self.resulting_label+=str(type)
        print(self.resulting_label)

    #all functions
    def clear(self):
        print("clear button pressed")
        self.disabled_one=False
        self.disabled_two=False
        self.disabled_three=False
        self.disabled_four=False
        self.disabled_five=False
        self.resulting_label=''
    
    def equals(self):
        self.resulting_label=str(eval(self.resulting_label))
        print(self.resulting_label)

    def submit(self):
        global diffs
        diffs=self.goal-eval(self.resulting_label)
        print(diffs)
        self.manager.current='result'

class MenuScreen(Screen):
    light=NumericProperty(0)
    available_numbers=ListProperty(0)
    counter=0
    temp=[]
    enable=BooleanProperty(True)
    available_numbers_label=StringProperty('  '.join([str(x) for x in available_numbers_global]))
    
    def on_pre_enter(self):
        self.light=lights
        print(f"value of temp {self.temp} and {available_numbers_global} compared")
        if self.temp==available_numbers_global:
            MenuScreen().Clears()
        else:
            self.available_numbers=available_numbers_global

    def Small(self):
        print("Small button pressed")
        if self.counter < len(self.available_numbers):
            global available_numbers_global
            self.available_numbers[self.counter] = random.randint(1,9)
            available_numbers_global=self.available_numbers
            self.counter+=1
            self.available_numbers_label='  '.join([str(x) for x in self.available_numbers])
        else:
            self.enable=False

    def Big(self):
        print("Big button pressed")
        if self.counter < len(self.available_numbers):
            global available_numbers_global
            self.available_numbers[self.counter] = random.randint(10,99)
            available_numbers_global=self.available_numbers
            self.counter+=1
            self.available_numbers_label='  '.join([str(x) for x in self.available_numbers])
        else:
            self.enable=False

    def Clears(self):
        global available_numbers_global
        print("Clear button pressed")
        self.available_numbers=[0]*5
        available_numbers_global=self.available_numbers
        self.counter=0
        self.available_numbers_label='  '.join([str(x) for x in self.available_numbers])
    
    def Next(self):
        print("Next button pressed")
        self.manager.current='game' 

class Options(Screen):
    def on_pre_enter(self):
        self.light=lights

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

    def on_pre_enter(self):
        self.light=lights

    def start(self):
        self.manager.current = 'menu'
        print("start button pressed")
    def Profile(self):
        print("Profile Button Pressed")
        
    def Options(self):
        self.manager.current="options"
        print("Options button Pressed")

class Manager(ScreenManager):  
    home = ObjectProperty(None)
    menu = ObjectProperty(None)
    options = ObjectProperty(None)
    game = ObjectProperty(None)
    result = ObjectProperty(None)

class LabsApp(App):
    def build(self):
        m = Manager(transition=NoTransition())
        return m

LabsApp().run()