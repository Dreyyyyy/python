import tkinter as tk
import sqlite3 as sql
from gui import gui

root = tk.Tk()
root.title("Register peoples APP")
root.geometry("330x480")

# Start the GUI
gui(root)

root.mainloop()
