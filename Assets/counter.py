from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from Assets.custom_buttons import ClickButton

Builder.load_file("Assets/kv/Counter.kv")


class Counter(FloatLayout):
    def __init__(self, **kwargs):
        super(Counter, self).__init__(**kwargs)

        self.counter = Label()
        self.counter.text = "0"
        self.counter.font_size = 72
        self.counter.text_int = 0
        self.counter.pos_hint = {"center_x": 0.5, "center_y": 0.8}
        self.add_widget(self.counter)

        self.test_button = ClickButton(on_press=self.plus_1)
        self.add_widget(self.test_button)

    def update_counter(self, instance):
        self.counter.text = str(self.counter.text_int)

    def plus_1(self, instance):
        self.counter.text_int += 1
        self.update_counter(instance)
