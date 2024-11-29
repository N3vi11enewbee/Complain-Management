from tkinter import *
import tkinter.messagebox as MessageBox
import sqlite3
from complaintlisting import ComplaintListing

def submit_complaint():
    description = desc_entry.get()
    if description == "":
        MessageBox.showinfo("Insert Status", "All fields are required")
    else:
        insert_complaint(description)

def insert_complaint(description):
    conn = sqlite3.connect('complaintDB.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO complaints(description, status) VALUES(?, ?)", (description, "Pending"))
    conn.commit()
    conn.close()
    MessageBox.showinfo("Insert Status", "Complaint Submitted Successfully")
    desc_entry.delete(0, END)

def view_complaints():
    ComplaintListing()

def delete_complaint():
    conn = sqlite3.connect('complaintDB.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM complaints WHERE id = ?", (complaint_id_entry.get(),))
    conn.commit()
    conn.close()
    MessageBox.showinfo("Delete Status", "Complaint Deleted Successfully")
    complaint_id_entry.delete(0, END)

root = Tk()
root.title("Complaint Management System")

# Complaint Description
Label(root, text='Complaint Description').grid(row=0, column=0)
desc_entry = Entry(root)
desc_entry.grid(row=0, column=1)

# Submit Button
submit_btn = Button(root, text='Submit Complaint', command=submit_complaint)
submit_btn.grid(row=1, column=1)

# View Complaints Button
view_btn = Button(root, text='View Complaints', command=view_complaints)
view_btn.grid(row=2, column=1)

# Complaint ID for deletion
Label(root, text="Complaint ID to delete").grid(row=3, column=0)
complaint_id_entry = Entry(root)
complaint_id_entry.grid(row=3, column=1)

# Delete Button
delete_btn = Button(root, text='Delete Complaint', command=delete_complaint)
delete_btn.grid(row=4, column=1)

root.mainloop()
