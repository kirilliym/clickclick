from kivy.app import App
from Assets.mainwindow import MainWindow


class clickclickApp(App):
    def build(self):
        return MainWindow()


if __name__ == "__main__":
    clickclickApp().run()
