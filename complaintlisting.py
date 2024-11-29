from tkinter import *
import sqlite3
from tkinter import ttk

def ComplaintListing():
    listing_window = Tk()
    listing_window.title("Complaint Listing")

    # Create Treeview to display complaints
    tree = ttk.Treeview(listing_window, columns=('ID', 'Description', 'Status'), show='headings')
    tree.heading('ID', text='ID')
    tree.heading('Description', text='Description')
    tree.heading('Status', text='Status')
    tree.pack(fill=BOTH, expand=1)

    conn = sqlite3.connect('complaintDB.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM complaints")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", END, values=row)
    conn.close()

    # Mark as Resolved Button
    def mark_as_resolved():
        selected_item = tree.selection()
        if selected_item:
            complaint_id = tree.item(selected_item, 'values')[0]
            conn = sqlite3.connect('complaintDB.db')
            cursor = conn.cursor()
            cursor.execute("UPDATE complaints SET status = ? WHERE id = ?", ('Resolved', complaint_id))
            conn.commit()
            conn.close()
            ComplaintListing()  # Refresh the listing
            listing_window.destroy()

    update_btn = Button(listing_window, text='Mark as Resolved', command=mark_as_resolved)
    update_btn.pack()

    listing_window.mainloop()
