from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from Assets.custom_buttons import TestButton
import sqlite3 as sql


class Counter(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.test_button = TestButton()
        self.add_widget(self.test_button)

        self.counter = Label()

        connection = sql.connect("database.db")
        cursor = connection.cursor()
        query = "CREATE TABLE IF NOT EXISTS baza (count INTEGER)"
        cursor.execute(query)
        connection.commit()
        
        k = 0
        query = "SELECT * FROM baza"
        cursor.execute(query)
        got = cursor.fetchone()
        
        if got == None:
            query = "INSERT INTO baza (count) VALUES (?)"
            values = (0,)
            cursor.execute(query, values)
            connection.commit()
        else:
            k = got[0]
        
        connection.close()
        

        self.counter.text = str(k)
        self.counter.text_int = k
        self.add_widget(self.counter)

        self.calc = BoxLayout()
        self.calc.orientation = "vertical"
        self.add_widget(self.calc)

        self.pluss = BoxLayout()
        self.calc.add_widget(self.pluss)

        self.button_p_1 = Button(text="+1", on_press=self.plus_1)
        self.pluss.add_widget(self.button_p_1)

    def update_counter(self, instance):
        self.counter.text = str(self.counter.text_int)

    def plus_1(self, instance):

        connection = sql.connect("database.db")
        cursor = connection.cursor()
        update = "UPDATE baza SET count = ? WHERE count = ?"
        values = (self.counter.text_int + 1, self.counter.text_int)
        cursor.execute(update, values)
        connection.commit()
        connection.close()

        self.counter.text_int += 1
        self.update_counter(instance)

