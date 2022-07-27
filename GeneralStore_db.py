from tkinter import *
import mysql.connector

root = Tk()
root.title("General Store")
root.wm_attributes('-fullscreen', 'false')    # Screen Size
root.configure(background='white')    # Background color of Window

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



# Creating Entries and Labels *********

# Creating first Label
Label(root, text="First Name", fg="black", font="dejavu 10 bold").grid(row=2, column=0, sticky=W)
# Creating first Entry
text_entry = Entry(root, width=35, border=2)
text_entry.grid(row=2, column=1,padx=10, pady=10)
# Creating second Label
Label(root, text="Last Name",fg="black", font="dejavu 10 bold").grid(row=3, column=0,sticky=W)
# Creating second Entry
text_entry1 = Entry(root, width=35, border=2)
text_entry1.grid(row=3, column=1,padx=10, pady=10)
# Creating third Label
Label(root, text="Phone Number", font="dejavu 10 bold").grid(row=4, column=0,sticky=W)
# Creating third Entry
text_entry2 = Entry(root, width=35, border=2)
text_entry2.grid(row=4, column=1,padx=10, pady=10)
# Creating fourth Label
Label(root, text="Address", font="dejavu 10 bold").grid(row=5, column=0,sticky=W)
# Creating fourth Entry
text_entry3 = Entry(root, width=35, border=2)
text_entry3.grid(row=5, column=1,padx=10, pady=10)
# Creating fifth Label
Label(root, text="City", font="dejavu 10 bold").grid(row=6, column=0,sticky=W)
# Creating fifth Entry
text_entry4 = Entry(root, width=35, border=2)
text_entry4.grid(row=6, column=1,padx=10, pady=10)
# Creating sixth Label
Label(root, text="Zip Code", font="dejavu 10 bold").grid(row=7, column=0,sticky=W)
# Creating sixth Entry
text_entry5 = Entry(root, width=35, border=2)
text_entry5.grid(row=7, column=1,padx=10, pady=10)
# Creating Search Label
Label(root, text="Search", font="dejavu 10 bold").grid(row=0, column=0,sticky=W)
# Creating search entry
search_entry = Entry(root, width=35, border=2)
search_entry.grid(row=0, column=1,padx=10, pady=10)




root.mainloop()
