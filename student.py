import tkinter as tk
from re import search
from tkinter import ttk
from tkinter import messagebox
import pymysql

from tkinter.constants import GROOVE, RIGHT

from mysql.connector.aio import MySQLConnection

win=tk.Tk()
win.geometry("1350x700+0+0")
win.title("Student management")


title_Label=tk.Label(win,text="Student Management System",font=("arial",30,"bold"),border=12,background="lightgray",relief=tk.GROOVE)
title_Label.pack(side=tk.TOP,fill=tk.X)

detail_Frame=tk.LabelFrame(win,text="Enter details",font=("arial",20),bg="lightgray",bd=12,relief=tk.GROOVE)
detail_Frame.place(x=20,y=90,width=420,height=570)

data_Frame=tk.LabelFrame(win,bd=12,relief=tk.GROOVE)
data_Frame.place(x=520,y=90,width=720,height=570)

#variables#

rollno=tk.StringVar()
name=tk.StringVar()
father=tk.StringVar()
Class_var=tk.StringVar()
section=tk.StringVar()
contact=tk.StringVar()
address=tk.StringVar()
gender=tk.StringVar()
dob=tk.StringVar()

search_by=tk.StringVar()
search_txt=tk.StringVar()

#***********#

#lables entry#

rollno_Lbl=tk.Label(detail_Frame,text="Rollno",font=("arial",17),bg="lightgray")
rollno_Lbl.grid(row=0,column=0,padx=2,pady=2)

rollno_ent=tk.Entry(detail_Frame,bd=7,font=("arial"),bg="white",textvariable=rollno)
rollno_ent.grid(row=0,column=1,padx=3,pady=3)

name_Lbl=tk.Label(detail_Frame,text="Name",font=("arial",17),bg="lightgray")
name_Lbl.grid(row=1,column=0,padx=2,pady=2)

name_ent=tk.Entry(detail_Frame,bd=7,font=("arial"),bg="white",textvariable=name)
name_ent.grid(row=1,column=1,padx=2,pady=2)

gender_Lbl=tk.Label(detail_Frame,text="Gender",font=("arial",17),bg="lightgray")
gender_Lbl.grid(row=2,column=0,padx=2,pady=2)

gender_ent=ttk.Combobox(detail_Frame,font=("arial"),state="readonly",textvariable=gender)
gender_ent['values']=("Male","Female","Other")
gender_ent.grid(row=2,column=1,padx=2,pady=2)


dob_Lbl=tk.Label(detail_Frame,text="D.O.B",font=("arial",17),bg="lightgray")
dob_Lbl.grid(row=3,column=0,padx=2,pady=2)

dob_ent=tk.Entry(detail_Frame,bd=7,font=("arial"),bg="white",textvariable=dob)
dob_ent.grid(row=3,column=1,padx=2,pady=2)

class_Lbl=tk.Label(detail_Frame,text="Class",font=("arial",17),bg="lightgray")
class_Lbl.grid(row=4,column=0,padx=2,pady=2)

class_ent=tk.Entry(detail_Frame,bd=7,font=("arial"),bg="white",textvariable=Class_var)
class_ent.grid(row=4,column=1,padx=2,pady=2)

sec_Lbl=tk.Label(detail_Frame,text="Section",font=("arial",17),bg="lightgray")
sec_Lbl.grid(row=5,column=0,padx=2,pady=2)

sec_ent=tk.Entry(detail_Frame,bd=7,font=("arial"),bg="white",textvariable=section)
sec_ent.grid(row=5,column=1,padx=2,pady=2)

contact_Lbl=tk.Label(detail_Frame,text="Contact",font=("arial",17),bg="lightgray")
contact_Lbl.grid(row=6,column=0,padx=2,pady=2)

contact_ent=tk.Entry(detail_Frame,bd=7,font=("arial"),bg="white",textvariable=contact)
contact_ent.grid(row=6,column=1,padx=2,pady=2)

father_Lbl=tk.Label(detail_Frame,text="father",font=("arial",17),bg="lightgray")
father_Lbl.grid(row=7,column=0,padx=2,pady=2)

father_ent=tk.Entry(detail_Frame,bd=7,font=("arial"),bg="white",textvariable=father)
father_ent.grid(row=7,column=1,padx=2,pady=2)

address_Lbl=tk.Label(detail_Frame,text="Address",font=("arial",17),bg="lightgray")
address_Lbl.grid(row=8,column=0,padx=2,pady=2)

address_ent=tk.Entry(detail_Frame,bd=7,font=("arial"),bg="white",textvariable=address)
address_ent.grid(row=8,column=1,padx=2,pady=2)
#*********************************#
#insertion#

def insert_data():
    try:
        conn = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='student',
            user='root',
            password='prince143'
        )
        cursor = conn.cursor()
        query = '''
            INSERT INTO students (rollno, name, gender, dob, class, father, section, contact, address)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        values = (
            rollno.get(),
            name.get(),
            gender.get(),
            dob.get(),
            Class_var.get(),
            father.get(),
            section.get(),
            contact.get(),
            address.get()
        )
        cursor.execute(query, values)
        conn.commit()
        messagebox.showinfo("Success", "Record inserted successfully!")
        conn.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Something went wrong: {err}")
        load_data()
        clear()


#*****************#
#*update data#



def update_data():




    rollno_val= rollno_ent.get()
    name_val = name_ent.get()
    gender_val =gender_ent.get()
    dob_val = dob_ent.get()
    Class_val = class_ent.get()
    father_val =father_ent.get()
    section_val = sec_ent.get()
    contact_val = contact_ent.get()
    address_val = address_ent.get()

    if rollno_val and name_val and gender_val and dob_val and Class_val and father_val and section_val and contact_val and address_val:
        try:
            conn = mysql.connector.connect(
                host='127.0.0.1',
                port=3306,
                database='student',
                user='root',
                password='prince143'
            )
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE students
                SET name = %s, gender = %s, dob = %s, Class = %s, father = %s, section = %s, contact = %s, address = %s
                WHERE rollno =%s
            """, (name_val, gender_val, dob_val, Class_val, father_val, section_val, contact_val, address_val, rollno_val))  # Added rollno_val here
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Record updated successfully.")
            load_data()  # Refresh the table after update
        except Exception as e:
            messagebox.showerror("Error", f"Update failed: {e}")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        load_data()
        clear()

#***************#
##load data#
def load_data():
    try:
        conn = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='student',
            user='root',
            password='prince143'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()

        # Clear old data
        student_table.delete(*student_table.get_children())

        # Insert new data
        for row in rows:
            student_table.insert("", tk.END, values=row)

        conn.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Failed to load data: {err}")

#######
#delete data#
def delete_data():
    rollno_val = rollno_ent.get()

    if not rollno_val:
        messagebox.showwarning("Input Error", "Please enter the Roll Number to delete.")
        return

    try:
        conn = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='student',
            user='root',
            password='prince143'
        )
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE rollno = %s", (rollno_val,))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Record deleted successfully.")
        load_data()  # Refresh the table
    except Exception as e:
        messagebox.showerror("Error", f"Delete failed: {e}")
        load_data()
        clear()

#*****************#
##searcb element##
def search_data():
    try:
        conn = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='student',
            user='root',
            password='prince143'
        )
        cursor = conn.cursor()

        field = search_by.get()  # e.g., 'name' or 'rollno'
        search_term = search_txt.get()  # e.g., the text entered by user

        # Validate inputs
        if not field or not search_term:
            messagebox.showwarning("Input Error", "Please select a field and enter search text.")
            return

        # Ensure field is safe (to prevent SQL injection)
        if field not in ['name', 'rollno']:
            messagebox.showerror("Invalid Field", "Invalid search field selected.")
            return

        # Prepare and execute query
        query = f"SELECT * FROM students WHERE {field} LIKE %s"
        value = ("%" + search_term + "%",)
        cursor.execute(query, value)
        rows = cursor.fetchall()

        # Clear table
        student_table.delete(*student_table.get_children())

        # Insert rows into table
        for row in rows:
            student_table.insert('', tk.END, values=row)

        conn.close()
    except Exception as e:
        messagebox.showerror("Error", f"Search failed: {e}")

############
#clear data#
def clear():
    rollno.set("")
    name.set("")
    father.set("")
    Class_var.set("")
    section.set("")
    contact.set("")
    address.set("")
    gender.set("")
    dob.set("")

##########

#button section#


btn_Frame=tk.Frame(detail_Frame,bd=10,relief=tk.GROOVE)
btn_Frame.place(x=19,y=400,width=295,height=90)

add_btn = tk.Button(btn_Frame, text="Add", font=("arial", 13), width=14, command=insert_data)
add_btn.grid(row=0,column=0)

dlt_btn=tk.Button(btn_Frame,text="Delete",font=("arial",13),width=14,command=delete_data)
dlt_btn.grid(row=0,column=1)

update_btn=tk.Button(btn_Frame,text="Update",font=("arial",13),width=14,command=update_data)
update_btn.grid(row=1,column=0)

clr_btn=tk.Button(btn_Frame,text="Clear",font=("arial",13),width=14,command=clear)
clr_btn.grid(row=1,column=1)

#*************************************#

#search#


search_Frame=tk.Frame(data_Frame,bd=5,relief=tk.GROOVE)
search_Frame.pack(side=tk.TOP,fill=tk.X)

search_lbl=tk.Label(search_Frame,text="Search",font=("arail,15"))
search_lbl.grid(row=0,column=0,pady=2,padx=2)

search_combo = ttk.Combobox(search_Frame, textvariable=search_by, font=("times new roman", 13), width=10,
                            state='readonly')
search_combo['values']=("name","rollno",)
search_combo.grid(row=0,column=1,padx=5,pady=2)

search_entry = tk.Entry(search_Frame, textvariable=search_txt, font=("times new roman", 13), width=8)
search_entry.grid(row=0, column=2, padx=10, pady=5)



search_btn = tk.Button(search_Frame, text="Search", font=("arial", 15), width=8,command=lambda :search_data())
search_btn.grid(row=0, column=6, pady=2, padx=2)


show_btn = tk.Button(search_Frame, text="Show all", font=("arial", 15), width=8, command=load_data)
show_btn.grid(row=0,column=9,pady=2,padx=2)

#********#
#**database#

database_Frame=tk.Frame(data_Frame,bd=11,relief=GROOVE)
database_Frame.pack(fill=tk.BOTH,expand=True)

y_scroll=tk.Scrollbar(database_Frame,orient=tk.VERTICAL)
x_scroll=tk.Scrollbar(database_Frame,orient=tk.HORIZONTAL)
#name,rollno,gender,dob,fathername,class,section,address,contact#
student_table=ttk.Treeview(database_Frame,columns=("Rollno","Name","Gender","Dob","Class","Fathername","section","contact","Address"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

student_table.heading("Rollno",text="Rollno")
student_table.heading("Name",text="Name")
student_table.heading("Gender",text="Gender")
student_table.heading("Dob",text="D.O.B")
student_table.heading("Class",text="Class")
student_table.heading("Fathername",text="Father's name")
student_table.heading("section",text="Section")
student_table.heading("contact",text="Contact")
student_table.heading("Address",text="Address")

student_table['show']='headings'

student_table.column("Rollno",width=120)
student_table.column("Name",width=120)
student_table.column("Gender",width=120)
student_table.column("Dob",width=120)
student_table.column("Class",width=120)
student_table.column("Fathername",width=120)
student_table.column("section",width=120)
student_table.column("contact",width=120)
student_table.column("Address",width=190)








student_table.pack(fill=tk.BOTH,expand=True)
#**********#
#connection code#
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
    # or your database host
        database="student",
        user='root',
        password='prince143'
    )

    if connection.is_connected():
        print("Successfully connected to the database")

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")

#************#
import tkinter as tk
from tkinter import ttk
import mysql.connector

# Connect to MySQL database
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    # or your database host
    database="student",
    user='root',
    password='prince143'
)
cursor = connection.cursor()

# Fetch data from the database
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

columns = [desc[0] for desc in cursor.description]  # Get column names

# Create main Tkinter window
root = tk.Tk()
root.title("Database Viewer")

# Create Treeview
tree = ttk.Treeview(root, columns=columns, show='headings')

# Define columns
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor=tk.CENTER)

# Insert data into Treeview
for row in rows:
    tree.insert('', tk.END, values=row)

tree.pack(expand=True, fill='both')

# Run the Tkinter loop
root.mainloop()

# Close the database connection
cursor.close()
connection.close()

#**********#





#****************#
win.mainloop()