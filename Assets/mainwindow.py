from kivy.uix.anchorlayout import AnchorLayout
from Assets.counter import Counter


class MainWindow(AnchorLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

        self.counter = Counter()
        self.add_widget(self.counter)

    def SaveData(self):
        self.counter.save_count()
