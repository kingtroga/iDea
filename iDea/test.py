from PIL import Image as PILImage
from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder
from kivy_gradient import Gradient
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.core.window import Window
from kivymd.uix.button import MDIconButton
Window.size = (350, 600)



class ImageButton(Image, Button):
    image_source = StringProperty()

class StoryPage(FloatLayout):
    story_background = ObjectProperty()

class UserImage(Image):
    image_source = StringProperty()


class TestApp(App):

    current = 0
    user_list = {"1": "image_1", "2": "image_2", "3": "image_3", "4": "image_4", "5": "image_5", "6": "image_6"}

    def on_start(self):
        for i in self.user_list:
            screen_manager.get_screen('home_page').ids.grid.add_widget(ImageButton(image_source=f"{i}.jpg"))

    def build(self):
        global screen_manager
        screen_manager = ScreenManager(transition = NoTransition())
        screen_manager.add_widget(Builder.load_file("home_page.kv"))
        screen_manager.add_widget(Builder.load_file("story_page.kv"))
        return screen_manager

    def story_background(self, image_color):
        im = PILImage.open(image_color)
        color = max(im.getcolors(im.size[0] * im.size[1]))[1]
        if (color[0] < 230) and (color[1] < 230) and (color[2] < 230):
            screen_manager.get_screen("story_page").ids.story.story_background = Gradient.vertical(
                (color[0]/255, color[1]/255, color[2]/255, 0.5),
                (color[0]/255, color[1]/255, color[2]/255, 1)
            )
        else:
            screen_manager.get_screen("story_page").ids.story.story_background = Gradient.vertical(
                (230/255, 230/255, 230/255, 0.5),
                (230/255, 230/255, 230/255, 1)
            )



    def show_stories(self, user):
        self.current = int(user.image_source.split(".")[0])
        self.story_background(user.image_source)
        screen_manager.get_screen("story_page").ids.story_image.source = user.image_source

if __name__ == '__main__':
    TestApp().run()