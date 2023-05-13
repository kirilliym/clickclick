from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from Assets.custom_buttons import TestButton


class Counter(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.test_button = TestButton()
        self.add_widget(self.test_button)

        self.counter = Label()
        self.counter.text = "0"
        self.counter.text_int = 0
        self.add_widget(self.counter)

        self.calc = BoxLayout()
        self.calc.orientation = "vertical"
        self.add_widget(self.calc)

        self.pluss = BoxLayout()
        self.calc.add_widget(self.pluss)

        self.button_p_1 = Button(text="+1", on_press=self.plus_1)
        self.pluss.add_widget(self.button_p_1)

        self.button_p_2 = Button(text="+2", on_press=self.plus_2)
        self.pluss.add_widget(self.button_p_2)

        self.button_p_3 = Button(text="+3", on_press=self.plus_3)
        self.pluss.add_widget(self.button_p_3)

        self.reset = BoxLayout()
        self.button_del = Button(text="reset", on_press=self.to_reset)
        self.reset.add_widget(self.button_del)
        self.calc.add_widget(self.reset)

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

    def to_reset(self, instance):
        self.counter.text_int = 0
        self.update_counter(instance)
