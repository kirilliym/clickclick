import kivy
from kivy.app import App
from Assets.mainwindow import MainWindow

kivy.require("2.1.0")


class clickclickApp(App):
    def build(self):
        return MainWindow()


if __name__ == "__main__":
    clickclickApp().run()
