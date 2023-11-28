from tkinter import Tk, Button, Label
from PIL import ImageTk, Image

root = Tk()

img0 = Image.open("/home/shuruyi/Documents/git/python/tkinter/aux_files/img0.jpg")
img1 = Image.open("/home/shuruyi/Documents/git/python/tkinter/aux_files/img1.jpg")
img2 = Image.open("/home/shuruyi/Documents/git/python/tkinter/aux_files/img2.jpg")
img3 = Image.open("/home/shuruyi/Documents/git/python/tkinter/aux_files/img3.webp")
img4 = Image.open("/home/shuruyi/Documents/git/python/tkinter/aux_files/img4.webp")
img5 = Image.open("/home/shuruyi/Documents/git/python/tkinter/aux_files/img5.webp")

img_list = [ImageTk.PhotoImage(img) for img in [img0, img1, img2, img3, img4, img5]]

img_label = Label(image=img_list[0])
foward_button = Button(root, text=">>")
backward_button = Button(root, text="<<")
exit_button = Button(root, text="Quit", command=root.quit)

img_label.grid(row=0, column=0, columnspan=3)
foward_button.grid(row=1, column=2)
backward_button.grid(row=1, column=0)
exit_button.grid(row=1, column=1)

exit_button.grid()

root.mainloop()
