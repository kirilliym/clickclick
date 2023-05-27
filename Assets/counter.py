from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.lang import Builder
from Assets.custom_buttons import ClickButton
from Assets.db import CounterDataBase


Builder.load_file("Assets/kv/Counter.kv")


class Counter(FloatLayout):
    def __init__(self, **kwargs):
        super(Counter, self).__init__(**kwargs)

        self.start_count = CounterDataBase.db_create()

        self.click_button = ClickButton(on_press=self.plus_1)
        self.add_widget(self.click_button)

        self.texture = Image(source="data/background.png").texture
        self.texture.wrap = "repeat"
        self.texture.uvsize = (
            Window.width / self.texture.width,
            Window.height / self.texture.height,
        )

    def plus_1(self, instance):
        self.count += 1

    def save_count(self):
        CounterDataBase.db_update(self.count, self.start_count)
