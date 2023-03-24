from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.text import LabelBase
from kivy.core.window import Window, WindowBase
from kivy.clock import Clock
from kivytransitions.transitions import SimpleZoom
from kivy.animation import Animation
from kivy.metrics import dp
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

class IdeaApp(App):
    def build(self):
        self.sm = RootWidget()
        return self.sm

    def touch_down_handler(self, *args):
        if args[0].name == 'Screen1':
            print(self.root.ids)

    def start_ideaLabel2_animation(self):
        ideaLabel2 = self.root.screens[1].ids['idealabel2']
        ideaLabel2_anim = Animation(pos_hint = {'center_y':0.95, 'center_x': 0.5},font_size=dp(30))
        ideaLabel2_anim.bind(on_complete=self.change_to_screen3)
        ideaLabel2_anim.start(ideaLabel2)

    def change_to_screen3(self, instance, value):
        self.sm.current = "Screen3"


LabelBase.register(name='Montserrat',
                   fn_regular=r'C:\Users\TARI\Desktop\code\kivy\iDea\fonts\Montserrat-VariableFont_wght.ttf')

if __name__ == "__main__":
    IdeaApp().run()