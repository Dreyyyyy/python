from tkinter import *

# instantiate ktinter
root = Tk()

# creating a "Hello World" widget
helloLabel = Label(root, text="Hello World!")
# shoving it into the screen(via root widget)
helloLabel.pack()

# main loop to print widgets on screen
root.mainloop()
