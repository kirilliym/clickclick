from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from Assets.db import CounterDataBase


Builder.load_file("Assets/kv/Counter.kv")


class Counter(FloatLayout):
    def __init__(self, **kwargs):
        super(Counter, self).__init__(**kwargs)

        self.start_count = CounterDataBase.db_create()

        self.texture_background = Image(source="data/background.png").texture
        self.texture_background.wrap = "repeat"
        self.texture_background.uvsize = (
            Window.width / self.texture_background.width,
            Window.height / self.texture_background.height,
        )

    def plus_1(self):
        self.count += 1

    def save_count(self):
        CounterDataBase.db_update(self.count, self.start_count)
