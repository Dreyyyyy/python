import tkinter as tk
import sqlite3 as sql


# Instantiate functions
def register_dtb(
    field_1st_name,
    field_last_name,
    field_address,
    field_city,
    field_state,
    field_zip_code,
):
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


def show_query(root):
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
        print_records += (
            str(record[0]) + " " + str(record[1]) + " " + str(record[6]) + "\n"
        )

    label_record = tk.Label(root, text=print_records)
    label_record.grid(row=12, column=0, columnspan=2, pady=(20, 0))

    conn.commit()

    conn.close()


def delete_rec(field_delete):
    conn = sql.connect(
        "/home/shuruyi/Documents/git/python/tkinter/register_users_app/database.db"
    )

    cur = conn.cursor()

    cur.execute("DELETE from peoples WHERE oid = " + field_delete.get())
    field_delete.delete(0, tk.END)

    conn.commit()

    conn.close()


def edit_rec(field_select):
    from gui import second_gui

    field_1st_name = ""
    field_last_name = ""
    field_address = ""
    field_city = ""
    field_state = ""
    field_zip_code = ""
    field_select_id = tk.IntVar()

    update = tk.Tk()
    update.title("Update a record")
    update.geometry("330x480")

    (
        field_1st_name,
        field_last_name,
        field_address,
        field_city,
        field_state,
        field_zip_code,
        field_select_id,
    ) = second_gui(update)

    conn = sql.connect(
        "/home/shuruyi/Documents/git/python/tkinter/register_users_app/database.db"
    )

    cur = conn.cursor()

    cur.execute("SELECT *, oid FROM peoples WHERE oid = " + field_select)
    records = cur.fetchall()

    for record in records:
        field_1st_name.insert(0, record[0])
        field_last_name.insert(0, record[1])
        field_address.insert(0, record[2])
        field_city.insert(0, record[3])
        field_state.insert(0, record[4])
        field_zip_code.insert(0, record[5])
        # Set the field_select value to the IntVar received from second_gui
        field_select_id.set(int(record[6]))

    conn.commit()

    conn.close()

    update.mainloop()


def update_rec(
    field_select,
    field_1st_name,
    field_last_name,
    field_address,
    field_city,
    field_state,
    field_zip_code,
    update,
):
    conn = sql.connect(
        "/home/shuruyi/Documents/git/python/tkinter/register_users_app/database.db"
    )

    cur = conn.cursor()

    sql_query = """UPDATE peoples SET
                    first_name = ?,
                    last_name = ?,
                    address = ?,
                    city = ?,
                    state = ?,
                    zip_code = ?
                    WHERE oid = ?"""

    try:
        print("SQL Query:", sql_query)
        cur.execute(
            sql_query,
            (
                str(field_1st_name.get()),
                str(field_last_name.get()),
                str(field_address.get()),
                str(field_city.get()),
                str(field_state.get()),
                int(field_zip_code.get()),
                field_select.get(),
            ),
        )
        conn.commit()
        conn.close()
        update.destroy()
    except sql.Error as e:
        print("SQL Error:", e)
