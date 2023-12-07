import tkinter as tk

root = tk.Tk()
root.title("Radio buttons")

pizzas = [
    ("Pepperoni", "Pepperoni"),
    ("Mozzarella", "Mozzarella"),
    ("Bacon", "Bacon"),
    ("Hawaian", "Hawaian"),
]

radio = tk.StringVar()
radio.set("None")

for text, mode in pizzas:
    radio_button = tk.Radiobutton(root, text=text, variable=radio, value=mode)
    radio_button.pack()

# radio_button = tk.Radiobutton(root, text="Radio Button", variable=radio, value=1)
# radio_button.pack()

click_button = tk.Button(root, text="Get Radio Value", command=lambda: get_radio(radio))
click_button.pack()


def get_radio(radio):
    value = radio.get()
    label = tk.Label(root, text=f"{value}")
    label.pack()


root.mainloop()
