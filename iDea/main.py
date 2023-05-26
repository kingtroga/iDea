# for changing the default screen size staticly
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
from kivy.uix.label import Label
from kivytransitions.transitions import SimpleZoom
from kivy.animation import Animation
from kivy.metrics import dp
from kivymd.uix.button.button import MDIconButton
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.bottomnavigation.bottomnavigation import MDBottomNavigation
from kivy.utils import get_color_from_hex
from kivy.lang import Builder
from kivymd.uix.label.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label.label import MDFloatLayout
from kivy.properties import StringProperty, ListProperty
from PIL import Image
from kivymd.uix.list.list import TwoLineAvatarListItem, ImageLeftWidget
import asyncio
import aiohttp
import time

#for changing the default screen size dynamicly
#Window.size = (375, 812)
#Window.clearcolor = (1, 1, 1, 1)

USER_KEY = ""

class RootWidget(ScreenManager):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        Clock.schedule_once(self.screen_switch_to_screen2, 1)

    def screen_switch_to_screen2(self, dt):
        self.current = 'Screen2'

    def change_to_screen3(self):
        self.current = 'Screen3'

class LoadingItem(MDFloatLayout):
    label_pos = ListProperty()
    label_color = ListProperty()

class Screen1(Screen):
    def __init__(self, **kwargs):
        super(Screen1, self).__init__(**kwargs)
        self.name  = "Screen1"


class Screen2(Screen):
    def __init__(self, **kwargs):
        super(Screen2, self).__init__(**kwargs)
        self.name  = "Screen2"
    #pass 

class Screen3(Screen):
    pass

class Screen4(Screen):
    def __init__(self, **kwargs):
        super(Screen4, self).__init__(**kwargs)
        self.name  = "Screen4"
        self.dialog = None

    """ def on_enter(self):
        Label1 = MDLabel(
                text=f"{10}",
                pos=(100, 200 + 10),
                font_style='H1')
        self.add_widget(Label1) """
    
        
    def start_loading_screen(self):
        self.loading = MDLabel(text=f"Loading...", font_style='H1', halign='center')
        self.add_widget(self.loading)

    def handle_loginBtn2_press(self):
        self.handle_btn_anim()
        self.handle_text_extract()
        self.handle_user_auth()

    def stop_loading_screen(self):
        self.remove_widget(self.loading)
        

    def handle_btn_anim(self):
        loginBtn = self.ids['log_in_button2']
        loginBtn_anim = Animation(back_color=(243/255, 246/255, 246/255, 1), color=(121/255, 124/255, 123/255, 1), duration=0.03)
        loginBtn_anim.start(loginBtn)

    def handle_text_extract(self):
        textInput1 = self.ids['login_text_input1']
        textInput2 = self.ids['login_text_input2']
        self.userID = str(textInput1.text)
        self.password = str(textInput2.text)
        print(self.userID, self.password)

    
    def handle_user_auth(self):
        if self.userID and self.password:
            asyncio.run(self.main())
        else:
            self.parent.current="Screen6"

    async def main(self):
        task1 = asyncio.create_task(self.fetch_data())
        USER_KEY = await task1
        print(USER_KEY)
        self.show_alert_dialog()
        
       
    async def fetch_data(self):
        #session = aiohttp.ClientSession(self)
        async with aiohttp.ClientSession() as session:
            response = await session.post("http://127.0.0.1:8000/api/v1/user/login/", 
                        data={
                            'user_id':self.userID, 
                            'password': self.password})
            result = await response.json()
            return result

    def show_alert_dialog(self):
        cancelBtn = MDFlatButton(
                text="CONTINUE",
                theme_text_color="Custom",
                text_color=(36/255, 120/255, 109/255, 1),
                )
        cancelBtn.bind(on_release=self.refresh_screen)
        if not self.dialog:
            self.dialog = MDDialog(
            title="Login Successful",
            buttons= [cancelBtn]
            )
        self.dialog.open()
        #self.dialog.close()

    def refresh_screen(self, button):
        #self.sm.current = "Screen1"
        self.dialog.dismiss()
        print("I was called")
        self.parent.current="Screen6"   

    
    
    def handle_loginBtn2_release(self):
        loginBtn = self.ids['log_in_button2']
        loginBtn_anim = Animation(back_color= (36/255, 120/255, 109/255, 1), color=(1, 1, 1, 1), duration=0.03)
        loginBtn_anim.start(loginBtn)

    
        
    

class Screen5(Screen):
    pass


class ImageButton(MDIconButton):
    image_source = StringProperty()
    color_line = ListProperty()





class Screen6(Screen):
    appStart = True
    #############################Chat Screen#######################################
    ##############################stuff#############################################
    #######################################################################################
    user_list = {"1" : "image_1", "2" : "image_2", "3" : "image_3", 
                "4" : "image_4", "5" : "image_5", "6" : "image_6", }

    uppertext_list = {"1": "Dr. Balogun", "2": "300L Computer Sc..", 
                "3": "Abraham John", "4": "Shalom", 
                "5": "19010301024", "6":"Angel Dayna"}

    lowertext_list = {"1": "I haven't seen your assign...", "2":"There will be CSC 307 class...",
                "3": "Hey! Can you join the meeting?", "4": "How are you today?",
                "5": "Have a good day🌸", "6": "How are you today?"}

    timeline_list = {"1": "2 min ago", "2": "2 min ago", "3": "2 min ago",
                "4": "5 min ago", "5": "yesterday", "6": "2 min ago"}

    icon_list = {"1": "numeric-3-circle", "2": "numeric-4-circle", "3":"",
            "4":"", "5":"", "6":""}
    ##########################################################################################
    ##########################################################################################
    ###########################################################################################
    ###########################Group Screen###################################################
    ###########################Stuff###########################################################
    ###########################################################################################
    group_icon_list = {7, 8, 9}
    group_uppertext_list = {7: "400L Computer Science", 8: "300L CSC",
                            9: "Cyber Security" }
    group_lowertext_list = {7: "Final Year Brethren", 8: "Keep working✍🏾",
                            9: "200 L Cyber Security Students"}
    ###########################################################################################
    ############################### ANNOUNCEMENTITEM STUFF ####################################
    ###########################################################################################
    author_list = [1, 2, 3]
    author_names = {1 : "Ajibade Benjamin", 2 : "Dr. Kasali", 3 : "J. Balogun"}
    date_created = {1 : "Today, 09:30AM", 2 : "Today, 9:30AM", 3: "Today, 9:30AM"}
    anTopic = {1: "Change of Venue For Exam", 2:"CSC 409 Make-Up Test", 3:"CSC 406 Class Is Holding!"}
    anContent = {
        1: "This is a notice to all 400 level students that offer CSC 411 that the venue for the exam is no longer LTB 1, it's now BIG LT",
        2: "This is a notice to all 400 level students that offer CSC 411 that the venue for the exam is no longer LTB 1, it's now BIG LT",
        3: "Good Afternoon to all 400 level students that offer CSC 406. There will be CSC 406 class by 10pm today unfailingly. Ensure to be there because attendance will be taken"}
    #############################################################################################
    #############################################################################################
    #############################################################################################
    
    def __init__(self, **kwargs):
        super(Screen6, self).__init__(**kwargs)
        self.name  = "Screen6"
        self.dialog = None
        self.newAn = True
        self.appStart =True
        self.groupUp = True
        Clock.schedule_once(self.show_loading, 0.5)
        Clock.schedule_once(self.remove_loading, 1)
        Clock.schedule_once(self.remove_loading, 2)
        Clock.schedule_once(self.remove_loading, 3)
        Clock.schedule_once(self.remove_loading, 4)
        Clock.schedule_once(self.remove_loading, 5)
        Clock.schedule_once(self.remove_loading, 6)
        Clock.schedule_once(self.remove_loading, 7)
        Clock.schedule_once(self.remove_loading, 8)
        Clock.schedule_once(self.remove_loading, 9)
        Clock.schedule_once(self.remove_loading, 10)
        Clock.schedule_once(self.remove_loading, 11)
        Clock.schedule_once(self.remove_loading, 12)
        Clock.schedule_once(self.remove_loading, 13)
        Clock.schedule_once(self.remove_loading, 14)
        Clock.schedule_once(self.remove_loading, 15)
        Clock.schedule_once(self.remove_loading, 16)
        Clock.schedule_once(self.remove_loading, 17)
        Clock.schedule_once(self.remove_loading, 18)
        Clock.schedule_once(self.remove_loading, 19)
        Clock.schedule_once(self.remove_loading, 20)
        Clock.schedule_once(self.remove_loading, 21)
        
        
        


    def on_enter(self):
        #self.add_widget(LoadingItem())
        self.start_story()
        #time.sleep(10)
        #self.remove_widget(LoadingItem())
        pass

    def animate_loading_item(self, dt):
        while self.appStart:
            print("Haleluyah!!!")
        

    def start_story(self):
        self.show_storys_and_chats()
        self.show_groups()
        self.show_announcements()


    def get_dominant_color(self, pil_img, palette_size=16):
        # Resize image to speed up processing
        img = pil_img.copy()
        img.thumbnail((100, 100))

        # Reduce colors (uses k-means internally)
        paletted = img.convert('P', palette=Image.ADAPTIVE, colors=palette_size)

        # Find the color that occurs most often
        palette = paletted.getpalette()
        color_counts = sorted(paletted.getcolors(), reverse=True)
        palette_index = color_counts[0][1]
        dominant_color = palette[palette_index*3:palette_index*3+3]
        kivy_color = []
        for i in dominant_color:
            kivy_color.append(i/255)
        kivy_color.append(1)
        return kivy_color
    
    def show_storys_and_chats(self):
        if self.appStart:
            for i in self.user_list:
                img = Image.open(f'{i}.jpg')

                self.ids['grid'].add_widget(ImageButton(image_source=f"{i}.jpg", color_line=self.get_dominant_color(img)))

                self.ids['rv'].data.append({
                    'avatar' : f'{i}.jpg',
                    "uppertext": self.uppertext_list[i],
                    "lowertext": self.lowertext_list[i],
                    "timeline": self.timeline_list[i],
                    "icon": self.icon_list[i]
                })
            self.appStart = False

 

    def show_groups(self):
        layout = MDFloatLayout(size_hint=(1, 0.34), md_bg_color=get_color_from_hex("#FFFFFF"))
        layout.add_widget(GroupInfo())
        if self.groupUp:
            for i in self.group_icon_list:
                self.ids['groupie'].add_widget(
                    ChatItem(
                        avatar=f'{i - 2}.jpg',
                        uppertext=self.group_uppertext_list[i],
                        lowertext=self.group_lowertext_list[i],
                        timeline="",
                        icon=""
                    ))
            self.ids['groupie'].add_widget(layout)
            self.groupUp = False


    def show_announcements(self):
        if self.newAn:
            for i in self.author_list:
                self.ids['aBox'].add_widget(
                    AnnouncementItem(
                        avatar=f"{i}.jpg", 
                        author_name=self.author_names[i],
                        date_created=self.date_created[i],
                        topic=self.anTopic[i],
                        body=self.anContent[i])
                    )
            self.newAn = False


    def show_loading(self, dt):
        self.layout = self.ids['whitey']
        self.loading = LoadingItem(label_pos=[self.layout.pos[0], self.layout.height/2 + 180], )
        self.layout.add_widget(self.loading)
        
    def remove_loading(self, dt):
        if not self.appStart:
            self.layout.remove_widget(self.loading)


class Screen7(Screen):
    pass   
    

class ChatItem(BoxLayout):
    avatar = StringProperty()
    uppertext = StringProperty()
    lowertext = StringProperty()
    timeline = StringProperty()
    icon = StringProperty()


class AnnouncementItem(MDFloatLayout):
    avatar = StringProperty()
    author_name = StringProperty()
    date_created = StringProperty()
    topic = StringProperty()
    body = StringProperty()

class GroupInfo(MDLabel):
    text = "Create more groups provided it meets the terms conditions of this app and the school(MTU)"
    halign="center"
    valign="center"
    theme_text_color="Custom"
    text_color = [121/255, 124/255, 123/255, 1]
    font_name = "fonts/Montserrat-Light.ttf"






class IdeaApp(MDApp):

    current = 0
    newAn = True
    appStart =True
    groupUp = True
    dialog = False

    #############################Chat Screen#######################################
    ##############################stuff#############################################
    #######################################################################################
    user_list = {"1" : "image_1", "2" : "image_2", "3" : "image_3", 
                "4" : "image_4", "5" : "image_5", "6" : "image_6", }

    uppertext_list = {"1": "Dr. Balogun", "2": "300L Computer Sc..", 
                "3": "Abraham John", "4": "Shalom", 
                "5": "19010301024", "6":"Angel Dayna"}

    lowertext_list = {"1": "I haven't seen your assign...", "2":"There will be CSC 307 class...",
                "3": "Hey! Can you join the meeting?", "4": "How are you today?",
                "5": "Have a good day🌸", "6": "How are you today?"}

    timeline_list = {"1": "2 min ago", "2": "2 min ago", "3": "2 min ago",
                "4": "5 min ago", "5": "yesterday", "6": "2 min ago"}

    icon_list = {"1": "numeric-3-circle", "2": "numeric-4-circle", "3":"",
            "4":"", "5":"", "6":""}
    ###########################Group Screen###################################################
    ###########################Stuff###########################################################
    ###########################################################################################
    group_icon_list = {7, 8, 9}
    group_uppertext_list = {7: "400L Computer Science", 8: "300L CSC",
                            9: "Cyber Security" }
    group_lowertext_list = {7: "Final Year Brethren", 8: "Keep working✍🏾",
                            9: "200 L Cyber Security Students"}
    ###########################################################################################
    ############################### ANNOUNCEMENTITEM STUFF ####################################
    ###########################################################################################
    author_list = [1, 2, 3]
    author_names = {1 : "Ajibade Benjamin", 2 : "Dr. Kasali", 3 : "J. Balogun"}
    date_created = {1 : "Today, 09:30AM", 2 : "Today, 9:30AM", 3: "Today, 9:30AM"}
    anTopic = {1: "Change of Venue For Exam", 2:"CSC 409 Make-Up Test", 3:"CSC 406 Class Is Holding!"}
    anContent = {
        1: "This is a notice to all 400 level students that offer CSC 411 that the venue for the exam is no longer LTB 1, it's now BIG LT",
        2: "This is a notice to all 400 level students that offer CSC 411 that the venue for the exam is no longer LTB 1, it's now BIG LT",
        3: "Good Afternoon to all 400 level students that offer CSC 406. There will be CSC 406 class by 10pm today unfailingly. Ensure to be there because attendance will be taken"}
    

    def start_story(self):
        self.show_storys_and_chats()
        self.show_groups()
        self.show_announcements()

    def show_storys_and_chats(self):
        if self.appStart:
            for i in self.user_list:
                img = Image.open(f'{i}.jpg')

                self.root.screens[5].ids['grid'].add_widget(ImageButton(image_source=f"{i}.jpg", color_line=self.get_dominant_color(img)))

                self.root.screens[5].ids['rv'].data.append({
                    'avatar' : f'{i}.jpg',
                    "uppertext": self.uppertext_list[i],
                    "lowertext": self.lowertext_list[i],
                    "timeline": self.timeline_list[i],
                    "icon": self.icon_list[i]
                })
            self.appStart = False

 

    def show_groups(self):
        layout = MDFloatLayout(size_hint=(1, 0.34), md_bg_color=get_color_from_hex("#FFFFFF"))
        layout.add_widget(GroupInfo())
        if self.groupUp:
            for i in self.group_icon_list:
                self.root.screens[5].ids['groupie'].add_widget(
                    ChatItem(
                        avatar=f'{i - 2}.jpg',
                        uppertext=self.group_uppertext_list[i],
                        lowertext=self.group_lowertext_list[i],
                        timeline="",
                        icon=""
                    ))
            self.root.screens[5].ids['groupie'].add_widget(layout)
            self.groupUp = False


    def show_announcements(self):
        if self.newAn:
            for i in self.author_list:
                self.root.screens[5].ids['aBox'].add_widget(
                    AnnouncementItem(
                        avatar=f"{i}.jpg", 
                        author_name=self.author_names[i],
                        date_created=self.date_created[i],
                        topic=self.anTopic[i],
                        body=self.anContent[i])
                    )
            self.newAn = False

    


        

    def get_dominant_color(self, pil_img, palette_size=16):
        # Resize image to speed up processing
        img = pil_img.copy()
        img.thumbnail((100, 100))

        # Reduce colors (uses k-means internally)
        paletted = img.convert('P', palette=Image.ADAPTIVE, colors=palette_size)

        # Find the color that occurs most often
        palette = paletted.getpalette()
        color_counts = sorted(paletted.getcolors(), reverse=True)
        palette_index = color_counts[0][1]
        dominant_color = palette[palette_index*3:palette_index*3+3]
        kivy_color = []
        for i in dominant_color:
            kivy_color.append(i/255)
        kivy_color.append(1)
        return kivy_color

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Teal"
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
        #loginBtn2.bind(on_press=self.change_to_screen6)

    def check_for_textinput(self, *args):
        loginBtn2 = self.root.screens[3].ids['log_in_button2']
        textInput1 = self.root.screens[3].ids['login_text_input1']
        textInput2 = self.root.screens[3].ids['login_text_input2']

        if textInput2.text != "" or textInput1.text != "":
            loginBtn2.back_color = (36/255, 120/255, 109/255, 1)
            loginBtn2.color = (1, 1, 1, 1)
        

    

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
        self.handle_btn_anim()
        self.handle_text_extract()
        

    def handle_btn_anim(self):
        loginBtn = self.root.screens[3].ids['log_in_button2']
        loginBtn_anim = Animation(back_color=(243/255, 246/255, 246/255, 1), color=(121/255, 124/255, 123/255, 1), duration=0.03)
        loginBtn_anim.start(loginBtn)

    def handle_text_extract(self):
        textInput1 = self.root.screens[3].ids['login_text_input1']
        textInput2 = self.root.screens[3].ids['login_text_input2']
        self.userID = str(textInput1.text)
        self.password = str(textInput2.text)
        #print(self.userID, self.password)

            
    
    def handle_loginBtn2_release(self):
        loginBtn = self.root.screens[3].ids['log_in_button2']
        loginBtn_anim = Animation(back_color= (36/255, 120/255, 109/255, 1), color=(1, 1, 1, 1), duration=0.03)
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

    def do_something(self):
        if self.newAn:
            for i in self.author_list:
                self.root.screens[5].ids['aBox'].add_widget(
                    AnnouncementItem(
                        avatar=f"{i}.jpg", 
                        author_name=self.author_names[i],
                        date_created=self.date_created[i],
                        topic=self.anTopic[i],
                        body=self.anContent[i])
                    )
            self.newAn = False



    



    #def handle_press(self, widget):
    #   widget.color=(0.5, 0.5, 0.5, 1)
    #   self.sm.transition = WipeTransition()
    #   self.sm.current = "Screen4"

        






#LabelBase.register(name='Montserrat',
#                   fn_regular=r'C:\Users\TARI\Desktop\code\kivy\iDea\fonts\Montserrat-VariableFont_wght.ttf')

if __name__ == "__main__":
    IdeaApp().run()