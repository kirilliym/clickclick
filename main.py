from kivy.app import App
from Assets.mainscreen import MainScreen


class clickclickApp(App):
    def build(self):
        return MainScreen()


if __name__ == "__main__":
    clickclickApp().run()
