import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Message Box")


def pop_up():
    # showinfo, showwarning, showerror, askquestion, askokquestion, askyesno
    message_box = messagebox.askquestion("Info Box", "Info Box!")
    message_label = tk.Label(text=message_box)
    message_label.pack()
    message_label.pack()


click_button = tk.Button(root, text="Open Message Box", command=pop_up)
click_button.pack()

root.mainloop()
