from tkinter import Tk, LabelFrame, Button

root = Tk()

frame = LabelFrame(root, text="Main Frame", padx=5, pady=5)
frame.pack(padx=10, pady=10)

click_button = Button(root, text="Button")
click_button.pack()

root.mainloop()
