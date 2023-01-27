from kivy.app import App  
from kivy.properties import NumericProperty,ObjectProperty,StringProperty,BooleanProperty,ListProperty
from kivy.uix.screenmanager import ScreenManager, Screen,NoTransition
import random

class ResultScreen(Screen):
    #Instantiating necessary as the root. variable in kv was taken from the scope of the class
    light=NumericProperty(0)
    diff=NumericProperty(0)
    last_label=StringProperty('')
    background=StringProperty('')

    #runs on Screen call
    def on_pre_enter(self,light=0,diffs=0):
        self.light=light
        self.diff=diffs
        if self.light==1:
            self.background="./data/background_light.jpg"
        else:
            self.background="./data/background_dark.jpg"

        if abs(self.diff)>=10:
            self.last_label="YOU WERE " + str(self.diff)+ " OFF"
        elif abs(self.diff)==0:
            self.last_label=f"WINNER!!"
        else:
            self.last_label=f"VERY CLOSE (Diff:{self.diff})"

    def take_me_home_country_roads(self):
        global available_numbers_global
        available_numbers_global=[0]*5
        self.manager.current='home'
        self.manager.get_screen("home").on_pre_enter(self.light)
        #MY SAVIOR
        self.manager.get_screen("menu").Clear()
        self.manager.get_screen("game").Clear()

    def extrawork(self):
        self.manager.current='menu'
        self.manager.get_screen("menu").on_pre_enter(self.light)
        self.manager.get_screen("menu").Clear()
        self.manager.get_screen("game").Clear()

class GameScreen(Screen):
    light=NumericProperty(0)
    goal=NumericProperty(0)
    resulting_label=StringProperty('')
    available_numbers=ListProperty(available_numbers_global)
    background=StringProperty('')
    
    disabled_one=BooleanProperty(False)
    disabled_two=BooleanProperty(False)
    disabled_three=BooleanProperty(False)
    disabled_four=BooleanProperty(False)
    disabled_five=BooleanProperty(False)
    enable_submit=BooleanProperty(False)

    def on_pre_enter(self,light=0,available_numbers=[0]*5):
        self.light=light
        self.available_numbers=available_numbers
        self.goal=random.randint(100, 999)
        if self.light==1:
            self.background="./data/background_light.jpg"
        else:
            self.background="./data/background_dark.jpg"

    def on_leave(self):
        self.goal=random.randint(100, 999)
        GameScreen().Clear()
        
    #all numbers
    def addcalcone(self):
        self.disabled_one=True
        self.resulting_label+=str(self.available_numbers[0])
        print(self.resulting_label)
        self.enable_submit=True

    def addcaltwo(self):
        self.disabled_two=True
        self.resulting_label+=str(self.available_numbers[1])
        print(self.resulting_label)
        self.enable_submit=True

    def addcalthree(self):
        self.disabled_three=True
        self.resulting_label+=str(self.available_numbers[2])
        print(self.resulting_label)
        self.enable_submit=True

    def addcalfour(self):
        self.disabled_four=True
        self.resulting_label+=str(self.available_numbers[3])
        print(self.resulting_label)
        self.enable_submit=True

    def addcalfive(self):
        self.disabled_five=True
        self.resulting_label+=str(self.available_numbers[4])
        print(self.resulting_label)
        self.enable_submit=True

    #all symbols
    def addsymbols(self,type):
        print(f"{type} button pressed")
        self.resulting_label+=str(type)
        print(self.resulting_label)

    #all functions
    def Clear(self):
        print("clear button pressed")
        self.disabled_one=False
        self.disabled_two=False
        self.disabled_three=False
        self.disabled_four=False
        self.disabled_five=False
        self.enable_submit=False
        self.resulting_label=''
    
    def equals(self):
        try:
            self.resulting_label=str(eval(self.resulting_label))
        except SyntaxError:
            print("syntax error")
            self.resulting_label=""
        print(self.resulting_label)

    def submit(self):
        try:
            diffs=self.goal-eval(self.resulting_label)
            print(diffs)
            self.manager.current='result'
            self.manager.get_screen('result').on_pre_enter(self.light,diffs)
        except SyntaxError:
            self.resulting_label=""
            print("SyntaxError")

class MenuScreen(Screen):
    light=NumericProperty(0)
    available_numbers=ListProperty(0)
    background=StringProperty("./data/background_dark.jpg")
    counter=0
    enable=BooleanProperty(True)
    available_numbers_label=StringProperty('  '.join([str(x) for x in available_numbers_global]))
    
    def on_pre_enter(self,light=0,available_numbers=[0]*5):
        self.light=light
        self.available_numbers=available_numbers
        if self.light==1:
            self.background="./data/background_light.jpg"
        else:
            self.background="./data/background_dark.jpg"
        
    def Small(self):
        print("Small button pressed")
        #Forced to write this because it needs another instance of button click to actually have a change in the state
        if self.counter==4:
            self.enable=False
        if self.counter < len(self.available_numbers):
            self.available_numbers[self.counter] = random.randint(1,9)
            self.counter+=1
            self.available_numbers_label='  '.join([str(x) for x in self.available_numbers])

    def Big(self):
        print("Big button pressed")
        if self.counter==4:
            self.enable=False
        if self.counter < len(self.available_numbers):
            self.available_numbers[self.counter] = random.randint(10,99)
            self.counter+=1
            self.available_numbers_label='  '.join([str(x) for x in self.available_numbers])

    def Clear(self):
        print("Clear button pressed")
        self.available_numbers=[0]*5
        self.enable=True
        self.counter=0
        self.available_numbers_label='  '.join([str(x) for x in self.available_numbers])
    
    def Next(self):
        print("Next button pressed")
        self.manager.current='game' 
        self.manager.get_screen('game').on_pre_enter(self.light,self.available_numbers)

class Options(Screen):
    light=NumericProperty(0)
    background=StringProperty('')
    def on_pre_enter(self,light=0):
        self.light=light
        self.background="./data/background_dark.jpg"

    def on_switch(self,Switch):
        if Switch.active==False:
            print("Dark Mode")
            self.light=0
        else:
            print("Light Mode")
            self.light=1

    def take_me_home_country_roads(self):
        print("Home button pressed")
        self.manager.current='home'
        self.manager.get_screen('home').on_pre_enter(self.light)

class HomeScreen(Screen):
    light=NumericProperty(0)
    background=StringProperty('')

    def on_pre_enter(self,light=0):
        self.light=light
        if self.light==1:
            self.background="./data/background_light.jpg"
        else:
            self.background="./data/background_dark.jpg"

    def start(self):
        print("start button pressed")
        self.manager.current = 'menu'
        self.manager.get_screen('menu').on_pre_enter(self.light)
    def Profile(self):
        print("Profile Button Pressed")
        
    def Options(self):
        print("Options button Pressed")
        self.manager.current="options"
        self.manager.get_screen('options').on_pre_enter(self.light)
        

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