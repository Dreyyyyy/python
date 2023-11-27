from tkinter import *

# instantiate main function of tkinter
root = Tk()


# defines a function to print the name caught from field
def clickButton():
    nameLabel = Label(root, text=f"Hello! {entry.get()}")
    nameLabel.pack()


# widget of input
entry = Entry(root, text="Please, type your name: ")
entry.pack()
# widget of button that calls the clickButton fuction when clicked
button = Button(root, text="Click me", command=clickButton)
button.pack()
# main loop to print on screen
root.mainloop()
