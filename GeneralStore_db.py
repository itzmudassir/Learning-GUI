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




root.mainloop()
