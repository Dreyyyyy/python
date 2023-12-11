import tkinter as tk
from functions import register_dtb, show_query, delete_rec, edit_rec, update_rec


def gui(root):
    # Instantiate labels
    label_1st_name = tk.Label(root, text="First name:")
    label_1st_name.grid(row=0, column=0, pady=(10, 0))
    label_last_name = tk.Label(root, text="Last name:")
    label_last_name.grid(row=1, column=0)
    label_address = tk.Label(root, text="Address:")
    label_address.grid(row=2, column=0)
    label_city = tk.Label(root, text="City:")
    label_city.grid(row=3, column=0)
    label_state = tk.Label(root, text="State:")
    label_state.grid(row=4, column=0)
    label_zip_code = tk.Label(root, text="Zip code:")
    label_zip_code.grid(row=5, column=0)
    label_select = tk.Label(root, text="Select record ID:")
    label_select.grid(row=9, column=0, pady=(10, 0))

    # Instantiate fields
    field_1st_name = tk.Entry(root)
    field_1st_name.grid(row=0, column=1, pady=(10, 0), ipadx=20)
    field_last_name = tk.Entry(root)
    field_last_name.grid(row=1, column=1, ipadx=20)
    field_address = tk.Entry(root)
    field_address.grid(row=2, column=1, ipadx=20)
    field_city = tk.Entry(root)
    field_city.grid(row=3, column=1, ipadx=20)
    field_state = tk.Entry(root)
    field_state.grid(row=4, column=1, ipadx=20)
    field_zip_code = tk.Entry(root)
    field_zip_code.grid(row=5, column=1, ipadx=20)
    field_select = tk.Entry(root)
    field_select.grid(row=9, column=1, pady=(10, 0), ipadx=20)

    # Instantiate button
    btn_register = tk.Button(
        root,
        text="Register to database",
        command=lambda: register_dtb(
            field_1st_name,
            field_last_name,
            field_address,
            field_city,
            field_state,
            field_zip_code,
        ),
    )
    btn_register.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=80)
    btn_query = tk.Button(
        root, text="Show data on query", command=lambda: show_query(root)
    )
    btn_query.grid(row=7, column=0, columnspan=2, padx=10, pady=0, ipadx=82)
    btn_delete = tk.Button(
        root,
        text="Delete record from database",
        command=lambda: delete_rec(field_select),
    )
    btn_delete.grid(row=10, column=0, columnspan=2, pady=(10, 0), ipadx=58)
    btn_update = tk.Button(
        root,
        text="Update record from database",
        command=lambda: edit_rec(field_select.get()),
    )
    btn_update.grid(row=11, column=0, columnspan=2, pady=(10, 0), ipadx=56)


def second_gui(update):
    field_select = tk.IntVar()

    # Instantiate labels
    label_1st_name = tk.Label(update, text="First name:")
    label_1st_name.grid(row=0, column=0, pady=(10, 0))
    label_last_name = tk.Label(update, text="Last name:")
    label_last_name.grid(row=1, column=0)
    label_address = tk.Label(update, text="Address:")
    label_address.grid(row=2, column=0)
    label_city = tk.Label(update, text="City:")
    label_city.grid(row=3, column=0)
    label_state = tk.Label(update, text="State:")
    label_state.grid(row=4, column=0)
    label_zip_code = tk.Label(update, text="Zip code:")
    label_zip_code.grid(row=5, column=0)

    # Instantiate fields
    field_1st_name = tk.Entry(update)
    field_1st_name.grid(row=0, column=1, pady=(10, 0), ipadx=20)
    field_last_name = tk.Entry(update)
    field_last_name.grid(row=1, column=1, ipadx=20)
    field_address = tk.Entry(update)
    field_address.grid(row=2, column=1, ipadx=20)
    field_city = tk.Entry(update)
    field_city.grid(row=3, column=1, ipadx=20)
    field_state = tk.Entry(update)
    field_state.grid(row=4, column=1, ipadx=20)
    field_zip_code = tk.Entry(update)
    field_zip_code.grid(row=5, column=1, ipadx=20)

    # Instantiate button
    btn_update = tk.Button(
        update,
        text="Update record from database",
        command=lambda: update_rec(
            field_select,
            field_1st_name,
            field_last_name,
            field_address,
            field_city,
            field_state,
            field_zip_code,
            update,
        ),
    )
    btn_update.grid(row=11, column=0, columnspan=2, pady=(10, 0), ipadx=56)

    return (
        field_1st_name,
        field_last_name,
        field_address,
        field_city,
        field_state,
        field_zip_code,
        field_select,
    )
