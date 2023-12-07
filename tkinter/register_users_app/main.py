import tkinter as tk
import sqlite3 as sql

root = tk.Tk()
root.title("Register peoples APP")
root.geometry("330x240")


# cur.execute(
#     """CREATE TABLE peoples(
#             first_name text,
#             last_name text,
#             address text,
#             city text,
#             state text,
#             zip_code integer
#             )"""
# )


# Instantiate functions
def register_dtb():
    conn = sql.connect(
        "/home/shuruyi/Documents/git/python/tkinter/register_users_app/database.db"
    )

    cur = conn.cursor()

    cur.execute(
        "INSERT INTO peoples values (:1st_name, :last_name, :address, :city, :state, :zip_code)",
        {
            "1st_name": field_1st_name.get(),
            "last_name": field_last_name.get(),
            "address": field_address.get(),
            "city": field_city.get(),
            "state": field_state.get(),
            "zip_code": field_zip_code.get(),
        },
    )

    conn.commit()

    conn.close()

    field_1st_name.delete(0, tk.END)
    field_last_name.delete(0, tk.END)
    field_address.delete(0, tk.END)
    field_city.delete(0, tk.END)
    field_state.delete(0, tk.END)
    field_zip_code.delete(0, tk.END)


def show_query():
    conn = sql.connect(
        "/home/shuruyi/Documents/git/python/tkinter/register_users_app/database.db"
    )

    cur = conn.cursor()

    cur.execute("SELECT *, oid FROM peoples")
    records = cur.fetchall()
    # print(records)
    # Loop through records and show then all on screen
    print_records = ""
    for record in records:
        print_records += str(record) + "\n"

    label_record = tk.Label(root, text=print_records)
    label_record.grid(row=8, column=0, columnspan=2)

    conn.commit()

    conn.close()


# Instantiate labels
label_1st_name = tk.Label(root, text="First name:")
label_1st_name.grid(row=0, column=0)
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

# Instantiate fields
field_1st_name = tk.Entry(root)
field_1st_name.grid(row=0, column=1)
field_last_name = tk.Entry(root)
field_last_name.grid(row=1, column=1)
field_address = tk.Entry(root)
field_address.grid(row=2, column=1)
field_city = tk.Entry(root)
field_city.grid(row=3, column=1)
field_state = tk.Entry(root)
field_state.grid(row=4, column=1)
field_zip_code = tk.Entry(root)
field_zip_code.grid(row=5, column=1)

# Instantiate button
btn_register = tk.Button(root, text="Register to database", command=register_dtb)
btn_register.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=80)
btn_query = tk.Button(root, text="Show data on query", command=show_query)
btn_query.grid(row=7, column=0, columnspan=2, padx=10, pady=0, ipadx=82)

root.mainloop()
