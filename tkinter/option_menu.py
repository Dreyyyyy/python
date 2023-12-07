import tkinter as tk

root = tk.Tk()
root.title("Option menu")
root.geometry("400x400")

var = tk.StringVar()

options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

menu_opt = tk.OptionMenu(root, var, *options)
menu_opt.pack()


def get_menu():
    var_value = var.get()
    menu_label = tk.Label(root, text=var_value)
    menu_label.pack()


get_menu_btn = tk.Button(root, text="Get menu option", command=get_menu)
get_menu_btn.pack()


root.mainloop()
