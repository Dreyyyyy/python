import tkinter as tk

root = tk.Tk()
root.title("Check Boxes")
root.geometry("400x400")

check_box_var = tk.BooleanVar()

check_box = tk.Checkbutton(
    root, text="Check here", onvalue=True, offvalue=False, variable=check_box_var
)
check_box.pack()


def get_check_box():
    check_box_value = check_box_var.get()
    check_box_label = tk.Label(root, text=check_box_value)
    check_box_label.pack()


check_btn = tk.Button(root, text="Get check box value", command=get_check_box)
check_btn.pack()

root.mainloop()
