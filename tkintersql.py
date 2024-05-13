import tkinter as tk
from tkinter import Label, Entry, Button, StringVar, IntVar, Radiobutton, Frame, messagebox
from tkcalendar import DateEntry
import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',       # Update with your MySQL username
            password='Waketech',       # Update with your MySQL password
            database='Tkintersql'  # Update with your database name
        )
        return connection
    except Error as e:
        messagebox.showerror("Connection Error", f"Error connecting to MySQL: {e}")
        return None

def insert_data():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            emp_no = txt_eno.get()
            mgr_no = txt_mgr.get()
            first_name = txt_fname.get()
            last_name = txt_lname.get()
            job = job_clicked.get()
            dept_no = dept_clicked.get()
            hire_date = cal.get_date()
            earns_commission = comm_selected.get() == "CommYes"
            commission_amount = txt_commamount.get() if earns_commission else None

            sql = "INSERT INTO employees (emp_no, mgr_no, first_name, last_name, job, dept_no, hire_date, earns_commission, commission_amount) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (emp_no, mgr_no, first_name, last_name, job, dept_no, hire_date, earns_commission, commission_amount)

            cursor.execute(sql, values)
            connection.commit()
            messagebox.showinfo("Success", "Employee details inserted successfully!")
        except Error as e:
            messagebox.showerror("Error", f"Error inserting data: {e}")
        finally:
            connection.close()

root = tk.Tk()
root.title("Employee Details")
root.geometry("700x300")

mf = Frame(root)
mf.grid()

lbl_eno = Label(mf, text="Employee #:")
lbl_eno.grid(row=0, column=0)
txt_eno = Entry(mf, width=20)
txt_eno.grid(row=0, column=1)

lbl_mgr = Label(mf, text="Manager #:")
lbl_mgr.grid(row=0, column=2)
txt_mgr = Entry(mf, width=20)
txt_mgr.grid(row=0, column=3)

lbl_fname = Label(mf, text="First Name:")
lbl_fname.grid(row=1, column=0)
txt_fname = Entry(mf, width=20)
txt_fname.grid(row=1, column=1)

lbl_lname = Label(mf, text="Last Name:")
lbl_lname.grid(row=1, column=2)
txt_lname = Entry(mf, width=20)
txt_lname.grid(row=1, column=3)

jobs = ["Clerk", "Salesman", "Manager", "Analyst", "President"]
job_clicked = StringVar()
job_clicked.set(jobs[0])

lbl_job = Label(mf, text="Job: ")
lbl_job.grid(row=2, column=0)
optmenu_job = tk.OptionMenu(mf, job_clicked, *jobs)
optmenu_job.grid(row=2, column=1)

depts = [10, 20, 30, 40]
dept_clicked = IntVar()
dept_clicked.set(depts[0])

lbl_depts = Label(mf, text="Department #: ")
lbl_depts.grid(row=2, column=2)
optmenu_depts = tk.OptionMenu(mf, dept_clicked, *depts)
optmenu_depts.grid(row=2, column=3)

lbl_hdate = Label(mf, text="Hire Date")
lbl_hdate.grid(row=2, column=4)
cal = DateEntry(mf)
cal.grid(row=2, column=5)

comm_selected = StringVar()
comm_selected.set("CommNo")  # Default value

comms = [
    ("Earns Commission?", "CommYes"),
    ("Doesn't Earn Commission", "CommNo")
]

c = 0
for text, mode in comms:
    Radiobutton(mf, text=text, variable=comm_selected, value=mode).grid(row=3, column=c)
    c += 1

lbl_commamount = Label(mf, text="Enter Commission:")
txt_commamount = Entry(mf, width=20)

def show_commission_widgets(*args):
    if comm_selected.get() == "CommYes":
        lbl_commamount.grid(row=3, column=2)
        txt_commamount.grid(row=3, column=3)
    else:
        lbl_commamount.grid_remove()
        txt_commamount.grid_remove()

comm_selected.trace('w', show_commission_widgets)

btn_insert = Button(mf, text="Insert", command=insert_data)
btn_insert.grid(row=4, column=1)

root.mainloop()
