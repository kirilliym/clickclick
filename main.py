import kivy
from kivy.app import App
from Assets.mainwindow import MainWindow

kivy.require("2.1.0")


class clickclickApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_window = MainWindow()

    def build(self):
        return self.main_window

    def on_stop(self):
        self.main_window.counter.save_count()


if __name__ == "__main__":
    clickclickApp().run()
