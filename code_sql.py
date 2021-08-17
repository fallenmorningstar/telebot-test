import sqlite3
import pathlib


def check_db():
    database = pathlib.Path('mydatabase.db')
    print(database)
    if database.exists() == False:
        create_db()
        print('db has been created')
    else:
        print('db passed')
        pass


def create_db():
    connection = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE users
                      (user_id text,
                      name text,
                      surname text,
                      phone  integer)
                   """)

    connection.commit()


def my_menu():
    connection = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE my_menu
                      (monday text,
                      tuesday text,
                      wednesday text,
                      thursday text,
                      friday text,
                      saturday text,
                      sunday text)
                   """)

    connection.commit()
