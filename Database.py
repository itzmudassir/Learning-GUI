from tkinter import *   # Importing Tkinter library
import sqlite3
from tkinter import messagebox  # Importing Messagebox library
import time

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

    messagebox.showinfo("Info", "The Information has been saved")  # Creating a message box

# Creating query function
def query():
    global record
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
        print_records += str(record[6]) + " " + str(record[0]) + "" + str(record[1]) + "\n"
    query_label = Label(root, text=print_records)
    query_label.place(x=8, y=330)

# Creating a function to delete data
def delete():
    # Creating a database connection
    connection = sqlite3.connect("database.db")
    # Creating a cursor
    cursor = connection.cursor()
    # Deleting data from the table
    cursor.execute("DELETE FROM addresses WHERE oid= " + search_entry.get())
    # Committing changes
    connection.commit()
    # Closing the connection
    connection.close()
    search_entry.delete(0, END)
    query()
    messagebox.showinfo("Info", "The Information has been deleted")  # Creating a message box

# Creating a function to save data
def update_data():
    # Creating a database connection
    connection = sqlite3.connect("database.db")
    # Creating a cursor
    cursor = connection.cursor()
    # Updating data in the table-
    cursor.execute("UPDATE addresses SET first_name=:first_name, last_name=:last_name, phone_number=:phone_number, address=:address, city=:city, zip_code=:zip_code WHERE oid=:oid",
                        {
                            'first_name': first_name_e.get(),
                            'last_name': last_name_e.get(),
                            'phone_number': phone_number_e.get(),
                            'address': address_e.get(),
                            'city': city_e.get(),
                            'zip_code': zip_code_e.get(),
                            'oid': search_entry.get()
                        })
    # Committing changes
    connection.commit() 
    # Closing the connection
    connection.close()
    messagebox.showinfo("Info", "The Information has been updated")  # Creating a message box


# Creating a function to update data
def update():
    up=Tk()
    up.title("we are learning Tkinter")
    up.geometry("500x500")
    connection=sqlite3.connect("database.db")
    cursor=connection.cursor()
    record_id=search_entry.get()
    cursor.execute("SELECT * FROM addresses WHERE oid="+record_id)
    data=cursor.fetchall()
    print(data)
    print_record=''
    for record in data:
        print_record += str( record ) +"\n"
    global first_name_e
    global last_name_e
    global phone_number_e
    global address_e
    global city_e
    global zip_code_e

    first_name_label=Label(up,text="First Name:")
    first_name_label.grid(row=0,column=0,sticky=W)
    first_name_e=Entry(up,width=30)
    first_name_e.grid(row=0,column=1)

    #create a label for the last name
    last_name_label=Label(up,text="Last Name:")
    last_name_label.grid(row=1,column=0,sticky=W)
    last_name_e=Entry(up,width=30)
    last_name_e.grid(row=1,column=1)

    #create a label for the phone number
    phone_number_label=Label(up,text="Phone Number:")
    phone_number_label.grid(row=2,column=0,sticky=W)
    phone_number_e=Entry(up,width=30)
    phone_number_e.grid(row=2,column=1)

    #create a label for the address
    address_label=Label(up,text="Address:")
    address_label.grid(row=3,column=0,sticky=W)
    address_e=Entry(up,width=30)
    address_e.grid(row=3,column=1)

    #create a label for the city
    city_label=Label(up,text="City:")
    city_label.grid(row=4,column=0,sticky=W)
    city_e=Entry(up,width=30)
    city_e.grid(row=4,column=1)

    #create a label for the zip code
    zip_code_label=Label(up,text="Zip Code:")
    zip_code_label.grid(row=5,column=0,sticky=W)
    zip_code_e=Entry(up,width=30)
    zip_code_e.grid(row=5,column=1)
    
    
    for record in data:
        
        first_name_e.insert(0,record[0])
        last_name_e.insert(0,record[1])
        phone_number_e.insert(0,record[2])
        address_e.insert(0,record[3])
        city_e.insert(0,record[4])
        zip_code_e.insert(0,record[5])
    
    
    # Creating a button to update the data
    Button(up, text="Save", command=update_data).place(x=180, y=125)
    
    

        

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
# Creating Search Label
Label(root, text="Search", font="dejavu 10 bold").grid(row=6, column=0,sticky=W)
# Creating search entry
search_entry = Entry(root, width=35, border=2)
search_entry.grid(row=6, column=1,padx=10, pady=10)


# Creating buttons
Button(root, text="Submit",padx=5, pady=5, command=submit).grid(row=7, column=1)  # Button to submit
Button(root, text="Show Record",padx=5, pady=5,bg="#565446", fg="white", command=query).grid(row=7, column=0)    # Button for query
Button(root, text="X",padx=10, bg="#F00D4E", command=root.destroy).place(x=1330, y=0)  # Button to exit

# Creating delete button
Button(root, text="Delete",padx=5, pady=5, command=delete).grid(row=7, column=2)
# Creating update button
Button(root, text="Update",padx=5, pady=5, command=update).grid(row=7, column=3)

# Committing the changes
connection.commit()
# Closing the connection
connection.close()
        
# Creating query function
root.mainloop()
