import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog

root = tk.Tk()
root.title("Open File")


def open_file():
    global img

    root.filename = filedialog.askopenfilename(
        initialdir="/home/shuruyi/Documents/git/python/tkinter/aux_files",
        title="Select a file",
        filetypes=[
            ("jpg files", "*.jpg"),
            ("webp files", "*.webp"),
            ("all files", "*.*"),
        ],
    )

    dir_label = tk.Label(root, text=f"{root.filename}")
    dir_label.pack()

    img = ImageTk.PhotoImage(Image.open(root.filename))
    img_label = tk.Label(root, image=img)
    img_label.pack()


open_button = tk.Button(root, text="Open file", command=open_file)
open_button.pack()

root.mainloop()
