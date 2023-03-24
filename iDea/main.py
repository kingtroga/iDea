from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.text import LabelBase
from kivy.core.window import Window, WindowBase
from kivy.clock import Clock
from kivytransitions.transitions import SimpleZoom
from kivy.animation import Animation
from kivy.metrics import dp
#Window.clearcolor = (1, 1, 1, 1)

class Screen1(Screen):
    pass

class Screen2(Screen):
    pass 

class Screen3(Screen):
    pass

class IdeaApp(App):
    def build(self):
        x = WindowBase.width
        y = WindowBase.height
        print(x, y)
        pass

    def touch_down_handler(self, *args):
        if args[0].name == 'Screen1':
            print(self.root.ids)

    def start_ideaLabel_animation(self):
        ideaLabel = self.root.screens[1].ids['anim_ideaLabel']
        ideaLabel_anim = Animation(size_hint_y=1.85, duration=0.35) 
        ideaLabel_anim.bind(on_start=self.start_ideaLabelFont_animationI)
        ideaLabel_anim.start(ideaLabel)
    
    
    def start_ideaLabelFont_animationI(self, instance, value):
        ideaLabel2 = self.root.screens[1].ids['i']
        ideaLabel2_anim = Animation(font_size=dp(30))
        ideaLabel2_anim.bind(on_start=self.start_ideaLabelFont_animationD)
        ideaLabel2_anim.start(ideaLabel2)
    
    def start_ideaLabelFont_animationD(self, instance, value):
        ideaLabel2 = self.root.screens[1].ids['d']
        ideaLabel2_anim = Animation(font_size=dp(30), )
        ideaLabel2_anim.bind(on_start=self.start_ideaLabelFont_animationE)
        ideaLabel2_anim.start(ideaLabel2)
    
    def start_ideaLabelFont_animationE(self, instance, value):
        ideaLabel2 = self.root.screens[1].ids['e']
        ideaLabel2_anim = Animation(font_size=dp(30))
        ideaLabel2_anim.bind(on_start=self.start_ideaLabelFont_animationA)
        ideaLabel2_anim.start(ideaLabel2)

    def start_ideaLabelFont_animationA(self, instance, value):
        ideaLabel2 = self.root.screens[1].ids['a']
        ideaLabel2_anim = Animation(font_size=dp(30))
        ideaLabel2_anim.start(ideaLabel2)


LabelBase.register(name='Montserrat',
                   fn_regular=r'C:\Users\TARI\Desktop\code\kivy\iDea\fonts\Montserrat-VariableFont_wght.ttf')

if __name__ == "__main__":
    IdeaApp().run()