import sqlite3 as sql


class CounterDataBase:
    def db_create():
        connection = sql.connect("data/count.db")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Counter (count INT)")
        connection.commit()
        cursor.execute("SELECT * FROM Counter")
        got = cursor.fetchone()

        if got is None:
            cursor.execute("INSERT INTO Counter(count) VALUES (0)")
            connection.commit()
            connection.close()
            return 0
        else:
            connection.close()
            return got[0]

    def db_update(value, key):
        connection = sql.connect("data/count.db")
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE Counter SET count = ? WHERE count = ?",
            (value, key),
        )
        connection.commit()
        connection.close()
