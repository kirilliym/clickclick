from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class Counter(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.counter = Label()
        self.counter.text = "0"
        self.counter.text_int = 0
        self.add_widget(self.counter)

        self.pluss = BoxLayout()
        self.add_widget(self.pluss)

        self.button_p_1 = Button(text="+1")
        self.button_p_1.bind(on_press=self.plus_1)
        self.pluss.add_widget(self.button_p_1)

        self.button_p_2 = Button(text="+2")
        self.button_p_2.bind(on_press=self.plus_2)
        self.pluss.add_widget(self.button_p_2)

        self.button_p_3 = Button(text="+3")
        self.button_p_3.bind(on_press=self.plus_3)
        self.pluss.add_widget(self.button_p_3)

    def update_counter(self, instance):
        self.counter.text = str(self.counter.text_int)

    def plus_1(self, instance):
        self.counter.text_int += 1
        self.update_counter(instance)

    def plus_2(self, instance):
        self.counter.text_int += 2
        self.update_counter(instance)

    def plus_3(self, instance):
        self.counter.text_int += 3
        self.update_counter(instance)
