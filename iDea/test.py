from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.animation import Animation

class RootWidget(ScreenManager):
    pass
class Screen1(Screen):
    pass
class TestApp(App):
    def build(self):
        return RootWidget()
    def print_something(self):
        print("Hi")

    def handle_loginBtn2_press(self):
        loginBtn = self.root.screens[0].ids['log_in_button2']
        loginBtn_anim = Animation(back_color=(36/255, 120/255, 109/255, 1), color=(1, 1, 1, 1), duration=0.03)
        loginBtn_anim.start(loginBtn)      
    
    def handle_loginBtn2_release(self):
        loginBtn = self.root.screens[0].ids['log_in_button2']
        loginBtn_anim = Animation(back_color= (243/255, 246/255, 246/255, 1), color=(121/255, 124/255, 123/255, 1), duration=0.03)
        loginBtn_anim.start(loginBtn)

    def handle_signUpBtn2_press(self):
        signUpBtn2 = self.root.screens[0].ids['signUpBtn2']
        signUpBtn2_anim = Animation(back_color=(36/255, 120/255, 109/255, 1), color=(1, 1, 1, 1), duration=0.03)
        signUpBtn2_anim.start(signUpBtn2)      
    
    def handle_signUpBtn2_release(self):
        signUpBtn2 = self.root.screens[0].ids['signUpBtn2']
        signUpBtn2_anim = Animation(back_color= (243/255, 246/255, 246/255, 1), color=(121/255, 124/255, 123/255, 1), duration=0.03)
        signUpBtn2_anim.start(signUpBtn2)
        
        


if __name__ == '__main__':
    TestApp().run()