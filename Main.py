'''

project name : student database system

author : pratik

'''

from os import close

import tkinter as tk

from tkinter import Message, PhotoImage, ttk, messagebox

import sqlite3

from tkinter.constants import CENTER, LEFT

from tkinter import *

from PIL import ImageTk,Image

top=tk.Tk()

top.config(bg="white")

top.geometry("1000x750")

top.title('Management System')

# Function And Operation 

# name,contact,mail,rollno,address,branch,years Add Row

con = sqlite3.connect("student.db")

con.execute("CREATE TABLE IF NOT EXISTS students(name TEXT,mail TEXT, address TEXT,branch TEXT,contact INTEGER, rollno INTEGER,  years INTEGER);")

# for Insert data in database

def insert_data(name,mail,address,branch,contact,rollno,years):

    conn = sqlite3.connect("student.db")

    conn.execute("INSERT INTO students(name,mail,address,branch,contact,rollno,years) VALUES( '" + name + "', '" + mail + "', '" + address + "', '" + branch + "', '" + contact + "', '" + rollno + "', '" + years + "' );")

    conn.commit()

    conn.close()

    messagebox.showinfo("Success", "Data Saved Successfully.")

# Add Student details

def insert():

    add_window = tk.Tk()

    add_window.title("Add Student Details")

    tk.Label(add_window).grid(row=0, column=0, columnspan=2)

    tk.Label(add_window, text="Student Name :").grid(row=1, column=0)

    name_entry = tk.Entry(add_window, width=50)

    name_entry.grid(row=1, column=1, padx=25)

    tk.Label(add_window, text="Contact :").grid(row=2, column=0)

    contact_entry = tk.Entry(add_window, width=50)

    contact_entry.grid(row=2, column=1, padx=25)

    tk.Label(add_window, text="Email id :").grid(row=3, column=0)

    email_entry = tk.Entry(add_window, width=50)

    email_entry.grid(row=3, column=1, padx=25)

    tk.Label(add_window, text="Roll Number :").grid(row=4, column=0, padx=20)

    roll_entry = tk.Entry(add_window, width=50)

    roll_entry.grid(row=4, column=1, padx=25)

    tk.Label(add_window, text="Address :").grid(row=5, column=0)

    address_entry = tk.Entry(add_window, width=50)

    address_entry.grid(row=5, column=1, padx=25)

    tk.Label(add_window, text="Branch :").grid(row=6, column=0)

    branch_entry = tk.Entry(add_window, width=50)

    branch_entry.grid(row=6, column=1, padx=25)

    tk.Label(add_window, text="Year :").grid(row=7, column=0)

    year_entry = tk.Entry(add_window, width=50)

    year_entry.grid(row=7, column=1, padx=25)

    tk.Button(add_window, text='Submit', activebackground='grey', activeforeground='white', bg='red',fg='white',command=lambda: submit()).grid(row=8, column=0, columnspan=2, pady=10)

    tk.Button(add_window, text='Close', activebackground='grey', activeforeground='white',bg='red',fg='white', command=add_window.destroy).grid(row=8, column=1, columnspan=2, pady=10)

    

    # submit button

    def submit():

        name = name_entry.get()

        contact = str(contact_entry.get())

        mail = email_entry.get()

        rollno = str(roll_entry.get())

        address = address_entry.get()

        branch = branch_entry.get()

        years = str(year_entry.get())

        insert_data(name,mail,address,branch,contact,rollno,years)

        add_window.destroy()

    add_window.mainloop()

# Display Information

def display():

    connn = sqlite3.connect("student.db")

    display_window = tk.Tk()

    display_window.title("Students Database")

    table = ttk.Treeview(display_window)

    table["columns"] = ("one", "two", "three", "four", "five", "six", "seven")

    table.heading("one", text="Name")

    table.heading("two", text="Email")

    table.heading("three",text="Address")

    table.heading("four", text="Branch")

    table.heading("five", text="contact")

    table.heading("six", text="Roll No")

    table.heading("seven", text="Year")

    cursor = connn.execute("SELECT rowid,* FROM students;")

    i = 0

    for row in cursor:

        table.insert('', i, text="Students " + str(row[0]), values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

        i = i + 1

    table.pack()

    connn.close()

# update Information

def update():

    update_window = tk.Tk()

    update_window.title("Update Student Details")

    tk.Label(update_window, text="Select the ID of student to be Updated:").grid(row=0, column=0, sticky="W", padx=10, columnspan=2)

    s_id = tk.Entry(update_window, width=50)

    s_id.grid(row=1, column=0, sticky="W", padx=10, columnspan=2)

    tk.Label(update_window, text="\nEnter the new values:").grid(row=2, column=0, sticky="W", padx=10, pady=10, columnspan=2)

    tk.Label(update_window, text="Name :").grid(row=3, column=0, sticky="W", padx=10, pady=10)

    s_name = tk.Entry(update_window, width=50)

    s_name.grid(row=3, column=1, sticky="W", padx=10, pady=10)

    tk.Label(update_window, text="Contact :").grid(row=4, column=0, sticky="W", padx=10, pady=10)

    s_contact = tk.Entry(update_window, width=50)

    s_contact.grid(row=4, column=1, sticky="W", padx=10, pady=10)

    tk.Label(update_window, text="Email id :").grid(row=5, column=0, sticky="W", padx=10, pady=10)

    s_email = tk.Entry(update_window, width=50)

    s_email.grid(row=5, column=1, sticky="W", padx=10, pady=10)

    tk.Label(update_window, text="Roll Number :").grid(row=6, column=0, sticky="W", padx=10, pady=10)

    s_roll = tk.Entry(update_window, width=50)

    s_roll.grid(row=6, column=1, sticky="W", padx=10, pady=10)

    tk.Label(update_window, text="Address :").grid(row=7, column=0, sticky="W", padx=10, pady=10)

    s_address = tk.Entry(update_window, width=50)

    s_address.grid(row=7, column=1, sticky="W", padx=10, pady=10)

    tk.Label(update_window, text="Branch  :").grid(row=8, column=0, sticky="W", padx=10, pady=10)

    s_branch = tk.Entry(update_window, width=50)

    s_branch.grid(row=8, column=1, sticky="W", padx=10, pady=10)

    tk.Label(update_window, text="Year :").grid(row=9, column=0, sticky="W", padx=10, pady=10)

    s_year = tk.Entry(update_window, width=50)

    s_year.grid(row=9, column=1, sticky="W", padx=10, pady=10)

     

    tk.Button(update_window, text="Update", activebackground='grey', activeforeground='white',bg='red',fg='white',command=lambda: submit()).grid(row=10, column=0, padx=10, pady=10, columnspan=2)

    tk.Button(update_window, text="Close", activebackground='grey', activeforeground='white',bg='red',fg='white',command=update_window.destroy).grid(row=10, column=1, padx=10, pady=10, columnspan=2)

    def submit():

        sid = s_id.get()

        sname = s_name.get()

        scontact = s_contact.get()

        smail = s_email.get()

        sroll = s_roll.get()

        saddress = s_address.get()

        sbranch = s_branch.get()

        syears = s_year.get()        

        scon = sqlite3.connect("student.db")

        scon.execute("UPDATE students SET name = '" + sname + "', contact = '" + scontact + "', mail = '" + smail + "', rollno = '" + sroll + "', address = '" + saddress + "', branch = '" + sbranch + "' ,years = '" + syears + "' WHERE rowid = " + sid + ";")

        scon.commit()

        scon.close()

        messagebox.showinfo("Success", "Data Updated Successfully.")

        update_window.destroy()

    update_window.mainloop()

# Delete Student Data

def delete():

    delete_window = tk.Tk()

    delete_window.title("Delete Student ")

    tk.Label(delete_window, text="Enter Student Name whose details are to be removed:").grid(row=0, column=0, padx=10, pady=10)

    d_name = tk.Entry(delete_window, width=50)

    d_name.grid(row=0, column=1, padx=10, pady=10)

    tk.Button(delete_window, text="Delete Details", activebackground='grey', activeforeground='white',bg='red',fg='white', command=lambda: submit()).grid(row=1, column=0, columnspan=2)

    tk.Button(delete_window, text="Close", activebackground='grey', activeforeground='white',bg='red',fg='white', command=delete_window.destroy).grid(row=1, column=1, columnspan=2)

    tk.Label(delete_window).grid(row=2, column=0, columnspan=2)

    def submit():

        dname = d_name.get()

        dcon = sqlite3.connect("student.db")

        dcon.execute("DELETE FROM students WHERE name = '" + dname +"';")

        dcon.commit()

        dcon.execute("VACUUM;")

        dcon.commit()

        dcon.close()

        messagebox.showinfo("Success", "Deleted Successfully.")

        delete_window.destroy()

    delete_window.mainloop()

# Search Student Data 

def search():

    search_window = tk.Tk()

    search_window.title("Search Student Details")

    tk.Label(search_window, text="Enter the name of Student whose details are to be searched:").grid(row=0, column=0,padx=10, pady=10)

    f_name = tk.Entry(search_window, width=50)

    f_name.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(search_window, text="Results: ").grid(row=1, column=0, sticky="W", columnspan=2, padx=10, pady=10)

    tk.Button(search_window, text="Search", activebackground='grey', activeforeground='white',bg='red',fg='white',command=lambda: submit()).grid(row=2, column=0, columnspan=2)

    tk.Button(search_window, text="Close", activebackground='grey', activeforeground='white',bg='red',fg='white',command=search_window.destroy).grid(row=2, column=1, columnspan=2)

    tk.Label(search_window).grid(row=3, column=0, sticky="W", columnspan=2, padx=10, pady=10)

    details = ttk.Treeview(search_window)

    details["columns"] = ("one", "two", "three", "four", "five","six","seven")

    details.heading("one", text="Name")

    details.heading("two", text="Email")

    details.heading("three",text="Address")

    details.heading("four", text="Branch")

    details.heading("five", text="contact")

    details.heading("six", text="Roll No")

    details.heading("seven", text="Year")

    

    def submit():

        for row in details.get_children():

            details.delete(row)

            

        fname = f_name.get()

        fcon = sqlite3.connect("student.db")

        cursor = fcon.execute("SELECT rowid,* from students WHERE name = '" + fname + "';")

        fcon.commit()

        i = 0

        for row in cursor:

            details.insert('', i, text="Student " + str(row[0]), values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

            i = i + 1

        details.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        fcon.close()

    search_window.mainloop()

con.close()

# New First Window Student System

def openwindo():

    mainWindow = tk.Tk()

    mainWindow.title("Student System")

    mainWindow.geometry("1000x760")

    label_1 = tk.Label(mainWindow, width="300", text="\n--- STUDENT MANAGEMENT SYSTEM ---\n", bg="blue",fg="black",font=("Georgia", 30))

    label_1.pack(padx=40, pady=20)

    button_1 = tk.Button(mainWindow, text="Add Student", command=lambda: insert(), padx=275, pady=25,activebackground='grey', activeforeground='white',bg="#00FF00",fg="black",font=("Georgia", 12)) 

    button_1.pack(padx=10, pady=10)

    button_2 = tk.Button(mainWindow, text="Update Student Details", command=lambda: update(), padx=240, pady=25,activebackground='grey', activeforeground='white',bg="#00FF00",fg="black",font=("Georgia", 12)) 

    button_2.pack(padx=10, pady=10)

    button_3 = tk.Button(mainWindow, text="View Student Details", command=lambda: display(), padx=248, pady=25,activebackground='grey', activeforeground='white',bg="#00FF00",fg="black",font=("Georgia", 12)) 

    button_3.pack(padx=10, pady=10)

    button_4 = tk.Button(mainWindow, text="Delete Student", command=lambda: delete(), padx=267, pady=25,activebackground='grey', activeforeground='white',bg="#00FF00",fg="black",font=("Georgia", 12))  

    button_4.pack(padx=10, pady=10)

    button_5 = tk.Button(mainWindow, text="Search Student", command=lambda: search(), padx=267, pady=25,activebackground='grey', activeforeground='white',bg="#00FF00",fg="black",font=("Georgia", 12))  

    button_5.pack(padx=10, pady=10)

    button_6 = tk.Button(mainWindow, text="Log Out", command=lambda: exit(), padx=267, pady=25,activebackground='grey', activeforeground='white',bg="red",fg="black",font=("Georgia", 12))   

    button_6.pack(padx=10, pady=10)

    label_2 = tk.Label(mainWindow, text="\n")

    label_2.pack()

# login user function

def login():

	entry_mail=user_entry.get().lower()	entry_pwd=userpwd_entry.get().lower()

	if entry_mail =='admin' and entry_pwd=='admin':

		openwindo()

	else:

		Dis=Message(top,text=" You Don't Have Permission to Login ! ", width=500, font=('Roman',15,'bold italic'),bg="white",fg='red')

		Dis.pack(padx=10, pady=65)

# title

label_1 = tk.Label(top, width="500", text="\n--- STUDENT MANAGEMENT SYSTEM ---\n", bg="blue",fg="black",font=("Georgia", 30))

label_1.pack(padx=10, pady=20)

# image

canvas = Canvas(top, width = 1000, height = 150)

canvas.pack()

img = ImageTk.PhotoImage(Image.open("student.jpg"))

canvas.create_image(20, 20, anchor=NW, image=img)

# login

label_2 = tk.Label(top,width="500", text="Please enter details below", bg="orange",fg="white",font=("Georgia", 20))

label_2.pack(padx=20, pady=30)

# user name

label_3=tk.Label(top,text='Enter User Name :',font=("Georgia", 12)).pack()

user_entry = tk.Entry(top, width=30)

user_entry.pack(padx=10, pady=10)

# user password

label_4=tk.Label(top,text='Enter User Password :',font=("Georgia", 12)).pack()

userpwd_entry = tk.Entry(top, width=30, show='*')

userpwd_entry.pack(padx=10, pady=10)

# button User login

userloginbt=tk.Button(top, text='Log in', font=30, bg="#0000FF" ,activebackground='#C0C0C0', activeforeground='white', command=login)

userloginbt.propagate(0)

userloginbt.place(x=380,y=580,width=80,height=40)

# button User exit

userexitbt=tk.Button(top, text='Exit', font=30, bg="red" ,activebackground='#C0C0C0', activeforeground='orange', command=exit)

userexitbt.propagate(0)

userexitbt.place(x=520,y=580,width=80,height=40)

top.mainloop()
