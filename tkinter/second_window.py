import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Main Window")


def open_window():
    global img

    top = tk.Toplevel()
    top.title("Second Window")

    img = ImageTk.PhotoImage(
        Image.open("/home/shuruyi/Documents/git/python/tkinter/aux_files/img0.jpg")
    )
    img_label = tk.Label(
        top,
        image=img,
    )
    img_label.pack()

    close_button = tk.Button(top, text="Close window", command=top.destroy)
    close_button.pack()


click_button = tk.Button(root, text="Open second window", command=open_window)
click_button.pack()

root.mainloop()
