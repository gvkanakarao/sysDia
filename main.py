from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty

# List of images
image_list = ['images\\1_0.jpg','images\\1_1.jpg','images\\1_2.jpg','images\\1_3.jpg','images\\1_4.jpg','images\\1_5.jpg']


class HomeScreen(Screen):
    def go_to_images(self):
        self.manager.current = "image_screen"
        self.manager.get_screen("image_screen").show_image(0)

class ImageScreen(Screen):
    image_source = StringProperty("")
    image_index = NumericProperty(0)

    def show_image(self, index):
        if 0 <= index < len(image_list):
            self.image_index = index
            self.image_source = image_list[index]

    def next_image(self):
        if self.image_index < len(image_list) - 1:
            self.show_image(self.image_index + 1)

    def prev_image(self):
        if self.image_index > 0:
            self.show_image(self.image_index - 1)

# ✅ Now load the KV file after defining classes
Builder.load_file("image.kv")

class ImageApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(ImageScreen(name="image_screen"))
        return sm

if __name__ == "__main__":
    ImageApp().run()
