from tkinter import Tk, Button, Label
from PIL import ImageTk, Image


def change_photo(img_list, opt, img_label):
    global i

    if opt == ">>" and i < len(img_list) - 1:
        i += 1
    elif opt == "<<" and i > 0:
        i -= 1

    img_label.config(image=img_list[i])


def show_ui(root, img_list):
    img_label = Label(root, image=img_list[i])
    img_label.grid(row=0, column=0, columnspan=3)

    foward_button = Button(
        root,
        text=">>",
        command=lambda: change_photo(img_list, ">>", img_label),
    )
    backward_button = Button(
        root,
        text="<<",
        command=lambda: change_photo(img_list, "<<", img_label),
    )
    exit_button = Button(root, text="Quit", command=root.quit)

    foward_button.grid(row=1, column=2)
    backward_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=1)


root = Tk()

i = 0

img_paths = [
    "/home/shuruyi/Documents/git/python/tkinter/aux_files/img0.jpg",
    "/home/shuruyi/Documents/git/python/tkinter/aux_files/img1.jpg",
    "/home/shuruyi/Documents/git/python/tkinter/aux_files/img2.jpg",
    "/home/shuruyi/Documents/git/python/tkinter/aux_files/img3.webp",
    "/home/shuruyi/Documents/git/python/tkinter/aux_files/img4.webp",
    "/home/shuruyi/Documents/git/python/tkinter/aux_files/img5.webp",
]

# Resize images to a uniform size
target_size = (800, 600)
img_list = [
    ImageTk.PhotoImage(Image.open(path).resize(target_size)) for path in img_paths
]

show_ui(root, img_list)
root.mainloop()
