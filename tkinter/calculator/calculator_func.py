from tkinter import END, Entry


def sum_nums(entry):
    global first_num
    global math

    first_num = int(entry.get())
    math = "+"

    entry.delete(0, END)


def calc_nums(entry):
    second_num = entry.get()

    entry.delete(0, END)

    if math == "+":
        entry.insert(0, first_num + int(second_num))
    elif math == "-":
        entry.insert(0, first_num - int(second_num))


def sub_nums(entry):
    global first_num
    global math

    first_num = int(entry.get())
    math = "-"

    entry.delete(0, END)


def clear_nums(entry):
    entry.delete(0, END)
