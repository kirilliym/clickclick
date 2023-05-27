from kivy.uix.button import Button
from kivy.lang import Builder


Builder.load_file("Assets/kv/ClickButton.kv")


class ClickButton(Button):
    def __init__(self, **kwargs):
        super(ClickButton, self).__init__(**kwargs)
        self.default_size_hint = self.size_hint[0]

    def on_press(self):
        self.color_shadow = (0 / 255, 0 / 255, 0 / 255, 0.55)
        self.shadow_slip = (1.06, 0.94)
        self.size_hint = (self.size_hint[0] * 0.99, None)

    def on_touch_up(self, touch):
        self.color_shadow = (0 / 255, 0 / 255, 0 / 255, 0.5)
        self.shadow_slip = (1.07, 0.93)
        self.size_hint = (self.default_size_hint, None)
