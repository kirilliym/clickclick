from kivy.uix.button import Button
from kivy.vector import Vector
from kivy.lang import Builder


Builder.load_file("Assets/kv/TestButton.kv")


class TestButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_press(self):
        self.color_button = 1, 0, 0, 1

    def on_release(self):
        self.color_button = 0.8, 0, 0.8, 1

    def collide_point(self, x, y):
        return Vector(x, y).distance(self.center) <= self.width / 2
