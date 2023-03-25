from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager

class RootWidget(ScreenManager):
    pass
class Screen1(Screen):
    pass
class TestApp(App):
    def build(self):
        return RootWidget()
    def print_something(self):
        print("Hi")

if __name__ == '__main__':
    TestApp().run()