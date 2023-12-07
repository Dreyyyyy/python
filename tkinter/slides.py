import tkinter as tk

root = tk.Tk()
root.title("Slides")
root.geometry("400x400")

vertical = tk.Scale(root, from_=0, to=200)
vertical.pack()

horizontal = tk.Scale(root, from_=0, to=200, orient="horizontal")
horizontal.pack()

hor_val_label = tk.Label(root, text=horizontal.get())
hor_val_label.pack()


def slide():
    hor_val_label = tk.Label(root, text=horizontal.get())
    hor_val_label.pack()

    hor = str(horizontal.get())
    ver = str(vertical.get())

    root.geometry(f"{hor}x{ver}")


get_hor_btn = tk.Button(root, text="Get horizontal value", command=slide)
get_hor_btn.pack()

root.mainloop()
