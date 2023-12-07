import tkinter as tk
import sqlite3 as sql

root = tk.Tk()
root.title("Using a database")
root.geometry("400x400")

# Instantiate a database or connect to one
conn = sql.connect("/home/shuruyi/Documents/git/python/tkinter/using_database.db")

# Create a cursor, structure that works like a control for the database
cur = conn.cursor()

# Create a table
cur.execute(
    """ CREATE TABLE basic_database(
            text_field text,
            int_field integer,
            float_field real,
            archive_field blob
            )"""
)

# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop()
