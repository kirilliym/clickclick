from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from Assets.counter import Counter


class MainWindow(AnchorLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

        self.inside = FloatLayout()
        self.add_widget(self.inside)

        self.counter = Counter()
        self.inside.add_widget(self.counter)
