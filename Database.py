from tkinter import *   # Importing Tkinter library
import sqlite3

root = Tk()   # Creating a root window
root.title("Database")   # Title name
root.wm_attributes('-fullscreen', 'True')   # Screen Size
root.configure(background='white')    # Background color of Window

# Creating a database connection
connection = sqlite3.connect("database.db")
# Creating a cursor
cursor = connection.cursor()
# Creating a table
'''
cursor.execute("""CREATE TABLE addresses(
first_name text,
last_name text,
phone_number integer,
address text,
city text,
zip_code integer
)
""")
'''
# Creating Submit function
def submit():
    # Creating a database connection
    connection = sqlite3.connect("database.db")
    # Creating a cursor
    cursor = connection.cursor()
    # Inserting data into the table
    cursor.execute("INSERT INTO addresses VALUES (:first_name, :last_name, :phone_number, :address, :city, :zip_code)",
                        {
                            'first_name': text_entry.get(),
                            'last_name': text_entry1.get(),
                            'phone_number': text_entry2.get(),
                            'address': text_entry3.get(),
                            'city': text_entry4.get(),
                            'zip_code': text_entry5.get()
                        })

        
    # Committing changes
    connection.commit()
    # Closing the connection
    connection.close()

    # Deleting the first text entry
    text_entry.delete(0, END)
    # Deleting the second text entry
    text_entry1.delete(0, END)
    # Deleting the third text entry
    text_entry2.delete(0, END)
    # Deleting the fourth text entry
    text_entry3.delete(0, END)
    # Deleting the fifth text entry
    text_entry4.delete(0, END)
    # Deleting the sixth text entry
    text_entry5.delete(0, END)

# Creating query function
def query():
    # Creating a database connection
    connection = sqlite3.connect("database.db")
    # Creating a cursor
    cursor = connection.cursor()
    # Selecting data from the table
    cursor.execute("SELECT *, oid FROM addresses")
    # Fetching all the data
    records = cursor.fetchall()
    # Printing the data
    print_records = ""
    for record in records:
        print_records += str(record) + "\n"
    query_label = Label(root, text=print_records)
    query_label.place(x=8, y=300)

    
        

# Creating first Label
Label(root, text="First Name", fg="black", font="dejavu 10 bold").grid(row=0, column=0, sticky=W)
# Creating first Entry
text_entry = Entry(root, width=35, border=2)
text_entry.grid(row=0, column=1,padx=10, pady=10)
# Creating second Label
Label(root, text="Last Name",fg="black", font="dejavu 10 bold").grid(row=1, column=0,sticky=W)
# Creating second Entry
text_entry1 = Entry(root, width=35, border=2)
text_entry1.grid(row=1, column=1,padx=10, pady=10)
# Creating third Label
Label(root, text="Phone Number", font="dejavu 10 bold").grid(row=2, column=0,sticky=W)
# Creating third Entry
text_entry2 = Entry(root, width=35, border=2)
text_entry2.grid(row=2, column=1,padx=10, pady=10)
# Creating fourth Label
Label(root, text="Address", font="dejavu 10 bold").grid(row=3, column=0,sticky=W)
# Creating fourth Entry
text_entry3 = Entry(root, width=35, border=2)
text_entry3.grid(row=3, column=1,padx=10, pady=10)
# Creating fifth Label
Label(root, text="City", font="dejavu 10 bold").grid(row=4, column=0,sticky=W)
# Creating fifth Entry
text_entry4 = Entry(root, width=35, border=2)
text_entry4.grid(row=4, column=1,padx=10, pady=10)
# Creating sixth Label
Label(root, text="Zip Code", font="dejavu 10 bold").grid(row=5, column=0,sticky=W)
# Creating sixth Entry
text_entry5 = Entry(root, width=35, border=2)
text_entry5.grid(row=5, column=1,padx=10, pady=10)


# Creating buttons
Button(root, text="Submit",padx=5, pady=5, command=submit).grid(row=7, column=1)  # Button to submit
Button(root, text="Query",padx=5, pady=5,bg="#565446", fg="white", command=query).grid(row=7, column=0)    # Button for query
Button(root, text="Exit",padx=20, pady=5,bg="#F00D4E", command=root.destroy).grid(row=7, column=2)  # Button to exit

# Committing the changes
connection.commit()
# Closing the connection
connection.close()
        
# Creating query function
root.mainloop()