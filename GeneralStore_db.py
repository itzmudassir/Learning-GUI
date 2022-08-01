# PROGRAMMED BY: Mudassir Nadeem

from tkinter import *
import mysql.connector
import csv

root = Tk()
root.title("General Store")
root.wm_attributes('-fullscreen', 'True')    # Screen Size
root.configure(background='white')    # Background color of Window

# ***DATABASE CODE START HERE***

# Creating database connection
database = mysql.connector.connect(host="localhost",user="root",passwd="mudassir12345.",database="General_Store")
#print(database)
cursor1 = database.cursor()


#cursor1.execute("CREATE DATABASE General_Store")
#cursor1.execute("SHOW DATABASES")
#print(cursor1.fetchall())

# Creating database table *****
#cursor1.execute("CREATE TABLE General(frist_name VARCHAR(255),last_name VARCHAR(255),age INT(255),zipcode INT(10),price_paid DECIMAL(10,2),user_id INT AUTO_INCREMENT PRIMARY KEY)")
#cursor1.execute("SELECT * FROM General")
#print(cursor1.description)

# Adding "FIELDS to the database"
'''cursor1.execute("ALTER TABLE General ADD  (\
    email VARCHAR(255),\
    address_1 VARCHAR(255),\
    address_2 VARCHAR(255),\
    city VARCHAR(50),\
    state VARCHAR(50),\
    country VARCHAR(255),\
    phone VARCHAR(255),\
    payment_method VARCHAR(50),\
    discount_code VARCHAR(255))")  
'''

#cursor1.execute("SELECT * FROM General")
#result=cursor1.description
#for x in result:
   #print(x)


# ***FUNCTIONS START HERE***


# Creating function to "Export Data"
def export_csv():
    cursor1.execute("SELECT * FROM General")
    result = cursor1.fetchall()
    with open('General.csv', 'w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in result:
            writer.writerow(row)
    csvfile.close()
    print("The data has been exported to the csv file")

# Creating Submit function
def clear_fields():
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
    # Deleting the seventh text entry
    text_entry6.delete(0, END)
    # Deleting the eighth text entry
    text_entry7.delete(0, END)
    # Deleting the ninth text entry
    text_entry8.delete(0, END)
    # Deleting the tenth text entry
    text_entry9.delete(0, END)



# Creating FUNCTIONS to remove text from the text entry
def temp_text(e):
   text_entry.delete(0,"end")
def temp_text1(e):
   text_entry1.delete(0,"end")
def temp_text2(e):
    text_entry2.delete(0,"end")
def temp_text3(e):
    text_entry3.delete(0,"end")
def temp_text4(e):
    text_entry4.delete(0,"end")
def temp_text5(e):
    text_entry5.delete(0,"end")
def temp_text6(e):
    text_entry6.delete(0,"end")
def temp_text7(e):
    text_entry7.delete(0,"end")
def temp_text8(e):
    text_entry8.delete(0,"end")
def temp_text9(e):
    text_entry9.delete(0,"end")

# Creating function to insert data into the database
def add_customer():
        sql_command = "INSERT INTO General(frist_name,last_name,phone,email,address_1,city,state,zipcode,price_paid,user_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (text_entry.get(),text_entry1.get(),text_entry2.get(),text_entry3.get(),text_entry4.get(),text_entry5.get(),text_entry6.get(),text_entry7.get(),text_entry8.get(),text_entry9.get())
        cursor1.execute(sql_command,values)
        database.commit()
        clear_fields()
        print("Data Inserted")

# Creating function to "Show Data"
def show_customer():
    top=Toplevel()
    top.title("Customer Info")
    top.geometry("500x500") 

    cursor1.execute("SELECT * FROM General")
    result = cursor1.fetchall()
    
    for index, x in enumerate(result):
        num=0
        for y in x:
            Label(top,text=y).grid(row=index,column=num)
            num+=1
    
    
    Button(top,text="Export", font=("Helvetica", "12", "bold"), bg="black", fg="white", command=export_csv).grid(row=index+1,column=0)


# Creating function to "Search Data" from the database
def search_customer():
    top=Toplevel()
    top.title("Search Customer")
    top.geometry("500x500") 
    cursor1.execute("SELECT * FROM General")
    result = cursor1.fetchall()

# Creating a "Title" Label
title = Label(root, text="General ", font=("Helvetica", 40), bg="black", fg="orange").place(x=5, y=5)
title_e = Label(root, text=" Store", font=("Helvetica", 40), bg="black", fg="white").place(x=190, y=5)

# Creating "First Name" Label
first_name = Label(root, text="First Name", font=("Helvetica", "12", "bold"), bg="white").place(x=5, y=100)
# Creating a "First Name" Text Entry
global text_entry
text_entry = Entry(root, width=30, bg="white", border = 2)
text_entry.insert(0, "Jack")
text_entry.place(x=180, y=102)
text_entry.bind("<FocusIn>", temp_text)
# Creating "Last Name" Label
last_name = Label(root, text="Last Name", font=("Helvetica", "12", "bold"), bg="white").place(x=5, y=150)
# Creating a "Last Name" Text Entry
global text_entry1
text_entry1 = Entry(root, width=30, bg="white", border = 2)
text_entry1.insert(0, "Smith")
text_entry1.bind("<FocusIn>", temp_text1)
text_entry1.place(x=180, y=152)
# Creating "Phone Number" Label
phone_number = Label(root, text="Phone Number", font=("Helvetica", "12", "bold"), bg="white").place(x=5, y=200)
# Creating a "Phone Number" Text Entry
global text_entry2
text_entry2 = Entry(root, width=30, bg="white", border = 2)
text_entry2.insert(0, "1234567890")
text_entry2.bind("<FocusIn>", temp_text2)
text_entry2.place(x=180, y=202)
# Creating "Email" Label
email = Label(root, text="Email", font=("Helvetica", "12", "bold"), bg="white").place(x=5, y=250)
# Creating a "Email" Text Entry
global text_entry3
text_entry3 = Entry(root, width=30, bg="white", border = 2)
text_entry3.insert(0, "@example.com")
text_entry3.bind("<FocusIn>", temp_text3)
text_entry3.place(x=180, y=252)
# Creating "Address" Label
address = Label(root, text="Address", font=("Helvetica", "12", "bold"), bg="white").place(x=5, y=300)
# Creating a "Address" Text Entry
global text_entry4
text_entry4 = Entry(root, width=30, bg="white", border = 2)
text_entry4.insert(0, "123 Main St")
text_entry4.bind("<FocusIn>", temp_text4)
text_entry4.place(x=180, y=302)
# Creating "City" Label
city = Label(root, text="City", font=("Helvetica", "12", "bold"), bg="white").place(x=5, y=350)
# Creating a "City" Text Entry
global text_entry5
text_entry5 = Entry(root, width=30, bg="white", border = 2)
text_entry5.insert(0, "New York")
text_entry5.bind("<FocusIn>", temp_text5)
text_entry5.place(x=180, y=352)
# Creating "State" Label
state = Label(root, text="State", font=("Helvetica", "12", "bold"), bg="white").place(x=5, y=400)
# Creating a "State" Text Entry
global text_entry6
text_entry6 = Entry(root, width=30, bg="white", border = 2)
text_entry6.insert(0, "NY")
text_entry6.bind("<FocusIn>", temp_text6)
text_entry6.place(x=180, y=402)
# Creating "Zip Code" Label
zip_code = Label(root, text="Zi Code", font=("Helvetica", "12", "bold"), bg="white").place(x=5, y=450)
# Creating a "Zip Code" Text Entry
global text_entry7
text_entry7 = Entry(root, width=30, bg="white", border = 2)
text_entry7.insert(0, "10001")
text_entry7.bind("<FocusIn>", temp_text7)
text_entry7.place(x=180, y=452)
# Creating "Price Paid" Label
price_paid = Label(root, text="Price Paid", font=("Helvetica", "12", "bold"), bg="white").place(x=5, y=500)
# Creating a "Price Paid" Text Entry
global text_entry8
text_entry8 = Entry(root, width=30, bg="white", border = 2)
text_entry8.insert(0, "100.00")
text_entry8.bind("<FocusIn>", temp_text8)
text_entry8.place(x=180, y=502)
# Creating "User ID" Label
user_id = Label(root, text="User ID", font=("Helvetica", "12", "bold"), bg="white").place(x=5, y=550)
# Creating a "User ID" Text Entry
global text_entry9
text_entry9 = Entry(root, width=30, bg="white", border = 2)
text_entry9.insert(0, "1")
text_entry9.bind("<FocusIn>", temp_text9)
text_entry9.place(x=180, y=552)




# CREATING BUTTONS
exit_button = Button(root, text="X",padx=10, bg="#F00D4E", command=root.destroy).place(x=1330, y=0)  # Button to exit
# Creating "Clear Fields" Button
clear_field = Button(root, text="Clear", font=("Helvetica", "12", "bold"), bg="black", fg="white", command=clear_fields).place(x=100, y=600)
# Creating "Add Customer" Button
add_customer_e = Button(root, text="Add Customer", font=("Helvetica", "12", "bold"), bg="black", fg="white", command=add_customer).place(x=300, y=600)
# Creating "Show Customers" Button
show_customers_e = Button(root, text="Show Customers", font=("Helvetica", "12", "bold"), bg="black", fg="white", command=show_customer).place(x=500, y=600)
# Creating "Search Customer" Button
search_customer_e = Button(root, text="Search Customer", font=("Helvetica", "12", "bold"), bg="black", fg="white", command=search_customer).place(x=700, y=600)
root.mainloop()
