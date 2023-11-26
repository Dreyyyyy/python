from tkinter import *


# simple function that print when the button is clicked
def click_func():
    clickLabel = Label(root, text="You've clicked!")
    clickLabel.pack()


# instantiate the tkinter
root = Tk()
# create and pack a helloLabel
helloLabel = Label(root, text="Hello World!")
helloLabel.pack()
# create and pack a button, that will activate the function when clicked
clickButton = Button(root, text="Click here", command=click_func)
clickButton.pack()
# main loop to print the widgets
root.mainloop()
