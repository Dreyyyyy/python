from tkinter import Tk
from img_viewer import show_ui
from PIL import ImageTk, Image

root = Tk()

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
