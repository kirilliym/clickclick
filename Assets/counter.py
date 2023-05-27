from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from Assets.custom_buttons import TestButton
import sqlite3 as sql


class Counter(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.test_button = TestButton()
        self.add_widget(self.test_button)

        connection = sql.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS baza (count INT)")
        connection.commit()

        cursor.execute("SELECT * FROM baza")
        got = cursor.fetchone()

        if got is None:
            cursor.execute("INSERT INTO baza(count) VALUES (0)")
            connection.commit()
            self.start_count = 0
        else:
            self.start_count = got[0]

        connection.close()

        self.counter = Label()
        self.counter.text = str(self.start_count)
        self.counter.text_int = self.start_count
        self.add_widget(self.counter)

        self.calc = BoxLayout()
        self.calc.orientation = "vertical"
        self.add_widget(self.calc)

        self.pluss = BoxLayout()
        self.calc.add_widget(self.pluss)

        self.button_p_1 = Button(text="+1", on_press=self.plus_1)
        self.pluss.add_widget(self.button_p_1)

        Window.bind(on_request_close=self.save_count)

    def update_counter(self, instance):
        self.counter.text = str(self.counter.text_int)

    def plus_1(self, instance):
        self.counter.text_int += 1
        self.update_counter(instance)

    def save_count(self, instance):
        connection = sql.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE baza SET count = ? WHERE count = ?", (self.counter.text_int, self.start_count))
        connection.commit()
        connection.close()
