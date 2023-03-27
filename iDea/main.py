# for changing the default screen size staticily
from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '812')
Config.write()

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition, WipeTransition
from kivy.core.text import LabelBase
from kivy.core.window import Window, WindowBase
from kivy.clock import Clock
from kivytransitions.transitions import SimpleZoom
from kivy.animation import Animation
from kivy.metrics import dp

#for changing the default screen size dynamicly
#Window.size = (375, 812)
#Window.clearcolor = (1, 1, 1, 1)

class RootWidget(ScreenManager):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        Clock.schedule_once(self.screen_switch_to_screen2, 1)

    def screen_switch_to_screen2(self, dt):
        self.current = 'Screen2'

    def change_to_screen3(self):
        self.current = 'Screen3'




class Screen1(Screen):
    pass

class Screen2(Screen):
    pass 

class Screen3(Screen):
    pass

class Screen4(Screen):
    pass

class IdeaApp(App):
    def build(self):
        self.sm = RootWidget()
        return self.sm

    def touch_down_handler(self, *args):
        if args[0].name == 'Screen1':
            print(self.root.ids)

    def start_ideaLabel2_animation(self):
        ideaLabel2 = self.root.screens[1].ids['idealabel2']
        ideaLabel2_anim = Animation(pos_hint = {'center_y':0.97, 'center_x': 0.5},font_size=dp(30), duration=0.5)
        ideaLabel2_anim.bind(on_complete=self.change_to_screen3)
        ideaLabel2_anim.start(ideaLabel2)

    def change_to_screen3(self, instance, value):
        self.sm.transition = NoTransition()
        self.sm.current = "Screen3"
        self.sm.transition = WipeTransition()

    def handle_login(self, *args):
        loginBtn = self.root.screens[2].ids['log_in']
        print(loginBtn.color)
        loginBtn.bind(on_press=self.change_to_screen4)
        #Clock.schedule_once(self.change_to_screen4, 0.2)

    def change_to_screen4(self, dt):
        self.sm.transition = WipeTransition()
        self.sm.current = "Screen4"

    def handle_loginBtn2_press(self):
        loginBtn = self.root.screens[3].ids['log_in_button2']
        loginBtn_anim = Animation(back_color=(36/255, 120/255, 109/255, 1), color=(1, 1, 1, 1), duration=0.03)
        loginBtn_anim.start(loginBtn)      
    
    def handle_loginBtn2_release(self):
        loginBtn = self.root.screens[3].ids['log_in_button2']
        loginBtn_anim = Animation(back_color= (243/255, 246/255, 246/255, 1), color=(121/255, 124/255, 123/255, 1), duration=0.03)
        loginBtn_anim.start(loginBtn)

    #def handle_press(self, widget):
    #   widget.color=(0.5, 0.5, 0.5, 1)
    #   self.sm.transition = WipeTransition()
    #   self.sm.current = "Screen4"

        






LabelBase.register(name='Montserrat',
                   fn_regular=r'C:\Users\TARI\Desktop\code\kivy\iDea\fonts\Montserrat-VariableFont_wght.ttf')

if __name__ == "__main__":
    IdeaApp().run()