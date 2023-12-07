from tkinter import Button, Label, W, E, SUNKEN
from PIL import ImageTk, Image


def change_photo(img_list, opt, img_label, count_photos_label, img_num):
    global img
    print(img)

    if opt == ">>" and img < len(img_list) - 1:
        img += 1
    elif opt == "<<" and img > 0:
        img -= 1

    count_photos_label.config(
        text=f"Image {img+1} of {len(img_list)}", bd=1, relief=SUNKEN, anchor=E
    )
    img_label.config(image=img_list[img])


def show_ui(root, img_list):
    global img
    img = 0

    img_label = Label(root, image=img_list[img])
    img_label.grid(row=0, column=0, columnspan=3)

    count_photos_label = Label(
        root, text=f"Image {img+1} of {len(img_list)}", bd=1, relief=SUNKEN, anchor=E
    )
    count_photos_label.grid(row=2, column=0, columnspan=3, sticky=W + E)

    foward_button = Button(
        root,
        text=">>",
        command=lambda: change_photo(
            img_list, ">>", img_label, count_photos_label, img
        ),
    )
    backward_button = Button(
        root,
        text="<<",
        command=lambda: change_photo(
            img_list, "<<", img_label, count_photos_label, img
        ),
    )
    exit_button = Button(root, text="Quit", command=root.quit)

    foward_button.grid(row=1, column=2, pady=10)
    backward_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=1)
