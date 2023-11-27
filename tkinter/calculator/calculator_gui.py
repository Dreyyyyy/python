from tkinter import Tk, Entry, Button, END
from calculator_func import sum_nums, sub_nums, clear_nums, calc_nums


def start_gui():
    root = Tk()
    root.title("Simple Calculator")
    start_widgets(root)
    root.mainloop()
    return root


def start_widgets(root):
    input_entry = Entry(root, width=50, borderwidth=5)
    input_entry.grid(row=0, column=0, columnspan=4, ipady=10, padx=10, pady=10)

    button1 = Button(
        root, text="1", padx=39, pady=20, command=lambda: button_clicked(1, input_entry)
    )
    button2 = Button(
        root, text="2", padx=39, pady=20, command=lambda: button_clicked(2, input_entry)
    )
    button3 = Button(
        root, text="3", padx=39, pady=20, command=lambda: button_clicked(3, input_entry)
    )

    button4 = Button(
        root, text="4", padx=39, pady=20, command=lambda: button_clicked(4, input_entry)
    )
    button5 = Button(
        root, text="5", padx=39, pady=20, command=lambda: button_clicked(5, input_entry)
    )
    button6 = Button(
        root, text="6", padx=39, pady=20, command=lambda: button_clicked(6, input_entry)
    )

    button7 = Button(
        root, text="7", padx=39, pady=20, command=lambda: button_clicked(7, input_entry)
    )
    button8 = Button(
        root, text="8", padx=39, pady=20, command=lambda: button_clicked(8, input_entry)
    )
    button9 = Button(
        root, text="9", padx=39, pady=20, command=lambda: button_clicked(9, input_entry)
    )

    button0 = Button(
        root, text="0", padx=88, pady=20, command=lambda: button_clicked(0, input_entry)
    )
    button_clear = Button(
        root,
        text="C",
        padx=38,
        pady=20,
        command=lambda: button_functions("C", input_entry),
    )
    button_equal = Button(
        root,
        text="=",
        padx=20,
        pady=55,
        command=lambda: button_functions("=", input_entry),
    )
    button_add = Button(
        root,
        text="+",
        padx=20,
        pady=19,
        command=lambda: button_functions("+", input_entry),
    )
    button_min = Button(
        root,
        text="-",
        padx=21,
        pady=19,
        command=lambda: button_functions("-", input_entry),
    )

    button1.grid(row=3, column=0, padx=4, pady=4)
    button2.grid(row=3, column=1, padx=4, pady=4)
    button3.grid(row=3, column=2, padx=4, pady=4)

    button4.grid(row=2, column=0, padx=4, pady=4)
    button5.grid(row=2, column=1, padx=4, pady=4)
    button6.grid(row=2, column=2, padx=4, pady=4)

    button7.grid(row=1, column=0, padx=4, pady=4)
    button8.grid(row=1, column=1, padx=4, pady=4)
    button9.grid(row=1, column=2, padx=4, pady=4)

    button0.grid(row=4, column=0, columnspan=2, padx=4, pady=4)
    button_clear.grid(row=4, column=2, padx=4, pady=4)
    button_equal.grid(row=3, column=3, padx=4, pady=4, rowspan=2)
    button_add.grid(row=2, column=3, padx=4, pady=4, rowspan=1)
    button_min.grid(row=1, column=3, padx=4, pady=4, rowspan=1)

    # Additional padding for symmetry
    root.grid_columnconfigure(0, minsize=90)
    root.grid_columnconfigure(1, minsize=90)
    root.grid_columnconfigure(2, minsize=90)
    root.grid_columnconfigure(3, minsize=90)


def button_clicked(num, entry):
    global current
    current = entry.get()

    entry.delete(0, END)
    entry.insert(0, str(current) + str(num))


def button_functions(opt, entry):
    if opt == "C":
        clear_nums(entry)
    if opt == "+":
        sum_nums(entry)
    if opt == "-":
        sub_nums(entry)
    if opt == "=":
        calc_nums(entry)
