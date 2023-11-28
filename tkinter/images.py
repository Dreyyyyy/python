from tkinter import Tk, Button, Label
from PIL import ImageTk, Image

# instantiate tkinter and it's title
root = Tk()
root.title("Images")
# using Pillow library to use .ico on linux, it doesn't work without it
ico = Image.open("/home/shuruyi/Documents/git/python/tkinter/aux_files/python_logo.ico")
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(True, photo)
# using Pillow library again to import newest image formats
img = ImageTk.PhotoImage(
    Image.open("/home/shuruyi/Documents/git/python/tkinter/aux_files/landscape.webp")
)
# widget with image label
image_label = Label(image=img)
image_label.pack()

# button to quit program
exit_button = Button(root, text="Exit", command=root.quit)
exit_button.pack()
# main loop to show on screen
root.mainloop()
