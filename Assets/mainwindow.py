from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from Assets.counter import Counter


class MainWindow(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.inside = BoxLayout()
        self.inside.orientation = "vertical"
        self.inside.size_hint = (0.4, 0.4)
        self.add_widget(self.inside)

        self.inside.add_widget(Counter())
