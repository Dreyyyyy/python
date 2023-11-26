from tkinter import *

# instantiate ktinter
root = Tk()

# create some widgets
helloLabel = Label(root, text="Hello World")
anotherLabel = Label(root, text="Just another text")

# organizing thoses widgets using grid
helloLabel.grid(row=0, column=0)
anotherLabel.grid(row=1, column=1)

# main loop to print widgets on screen
root.mainloop()
