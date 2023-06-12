import kivy
from kivy.app import App
from Assets.mainwindow import MainWindow


kivy.require("2.2.0")


class ClickClickApp(App):
    def __init__(self, **kwargs):
        super(ClickClickApp, self).__init__(**kwargs)
        self.main_window = MainWindow()


    def build(self):
        return self.main_window

    def on_pause(self):
        self.main_window.SaveData()

    def on_stop(self):
        self.main_window.SaveData()



if __name__ == "__main__":
    ClickClickApp().run()
