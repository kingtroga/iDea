# for changing the default screen size staticily
from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '812')
Config.write()

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition, WipeTransition
from kivy.core.text import LabelBase
from kivy.core.window import Window, WindowBase
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.uix.button import Button
from kivytransitions.transitions import SimpleZoom
from kivy.animation import Animation
from kivy.metrics import dp
from kivymd.uix.button.button import MDIconButton
from kivymd.uix.bottomnavigation.bottomnavigation import MDBottomNavigation
from kivy.utils import get_color_from_hex
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

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

class Screen5(Screen):
    pass



class Screen6(Screen):
    current = 0
    user_list = {"1" : "image_1", "2" : "image_2", "3" : "image_3", 
                "4" : "image_4", "5" : "image_5", "6" : "image_6", }

    def __init__(self, **kwargs):
        super(Screen6, self).__init__(**kwargs)
        self.name  = "Screen6"

    def start_story(self):
        for i in self.user_list:
           self.ids['grid'].add_widget(ImageButton(image_source=f"{i}.jpg"))
           self.ids['grid2'].add_widget(ChatItem(
               avatar = '1.jpg',
               uppertext = "Dr. Balogun",
               lowertext = "I haven't seen your assin...",
               timeline="2 min ago",
               icon = "numeric-5-circle"
           ))

class Screen7(Screen):
    pass   
    

class ChatItem(BoxLayout):
    avatar = StringProperty()
    uppertext = StringProperty()
    lowertext = StringProperty()
    timeline = StringProperty()
    icon = StringProperty()

class ImageButton(MDIconButton):
    image_source = StringProperty()


class IdeaApp(MDApp):

    current = 0
    user_list = {"1" : "image_1", "2" : "image_2", "3" : "image_3", 
                "4" : "image_4", "5" : "image_5", "6" : "image_6", }

    def start_story(self):
        for i in self.user_list:
           self.root.screens[5].ids['grid'].add_widget(ImageButton(image_source=f"{i}.jpg"))
           self.root.screens[5].ids['rv'].data.append({
               'avatar' : '1.jpg',
               "uppertext": "Dr. Balogun",
               "lowertext": "I haven't seen your assin...",
               "timeline":"2 min ago",
               "icon": "numeric-5-circle"
           })


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

    def handle_login2(self, *args):
        loginBtn2 = self.root.screens[3].ids['log_in_button2']
        loginBtn2.bind(on_press=self.change_to_screen6)

    def handle_signUp(self, *args):
        signUpBtn = self.root.screens[2].ids['sign_up_button']
        print(signUpBtn.color)
        signUpBtn.bind(on_press=self.change_to_screen5)

    def change_to_screen4(self, dt):
        self.sm.transition = WipeTransition()
        self.sm.current = "Screen4"

    def change_to_screen5(self, button):
        self.sm.transition = WipeTransition()
        #print("What the fuck?")
        self.sm.current = "Screen5"
    
    def change_to_screen6(self, button):
        self.sm.transition = WipeTransition()
        self.sm.current="Screen6"
        

    def handle_loginBtn2_press(self):
        loginBtn = self.root.screens[3].ids['log_in_button2']
        loginBtn_anim = Animation(back_color=(36/255, 120/255, 109/255, 1), color=(1, 1, 1, 1), duration=0.03)
        loginBtn_anim.start(loginBtn)      
    
    def handle_loginBtn2_release(self):
        loginBtn = self.root.screens[3].ids['log_in_button2']
        loginBtn_anim = Animation(back_color= (243/255, 246/255, 246/255, 1), color=(121/255, 124/255, 123/255, 1), duration=0.03)
        loginBtn_anim.start(loginBtn)

    def handle_signUpBtn_release(self):
        self.back_color=(1, 1, 1, 1)
        self.change_to_screen5()

    def handle_signUpBtn2_press(self):
        signUpBtn2 = self.root.screens[4].ids['signUpBtn2']
        signUpBtn2_anim = Animation(back_color=(36/255, 120/255, 109/255, 1), color=(1, 1, 1, 1), duration=0.03)
        signUpBtn2_anim.start(signUpBtn2)      
    
    def handle_signUpBtn2_release(self):
        signUpBtn2 = self.root.screens[4].ids['signUpBtn2']
        signUpBtn2_anim = Animation(back_color= (243/255, 246/255, 246/255, 1), color=(121/255, 124/255, 123/255, 1), duration=0.03)
        signUpBtn2_anim.start(signUpBtn2)
    



    #def handle_press(self, widget):
    #   widget.color=(0.5, 0.5, 0.5, 1)
    #   self.sm.transition = WipeTransition()
    #   self.sm.current = "Screen4"

        






#LabelBase.register(name='Montserrat',
#                   fn_regular=r'C:\Users\TARI\Desktop\code\kivy\iDea\fonts\Montserrat-VariableFont_wght.ttf')

if __name__ == "__main__":
    IdeaApp().run()