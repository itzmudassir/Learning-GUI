from tkinter import *   # Importing Tkinter library

root = Tk()   # Creating a root window
root.title("Database")   # Title name
root.wm_attributes('-fullscreen', 'True')   # Screen Size
root.configure(background='white')    # Background color of Window

# Creating Submit function
def submit():
    text_entry.delete(0, END)    # Deleting the first text entry
    text_entry1.delete(0, END)   # Deleting the second text entry
    text_entry2.delete(0, END)   # Deleting the third text entry
    text_entry3.delete(0, END)   # Deleting the fourth text entry
    text_entry4.delete(0, END)   # Deleting the fifth text entry

# Creatin query function
def query():
    return

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
Label(root, text="City", font="dejavu 10 bold").grid(row=2, column=0,sticky=W)
# Creating third Entry
text_entry2 = Entry(root, width=35, border=2)
text_entry2.grid(row=2, column=1,padx=10, pady=10)
# Creating fourth Label
Label(root, text="Address", font="dejavu 10 bold").grid(row=3, column=0,sticky=W)
# Creating fourth Entry
text_entry3 = Entry(root, width=35, border=2)
text_entry3.grid(row=3, column=1,padx=10, pady=10)
# Creating fifth Label
Label(root, text="Zip code", font="dejavu 10 bold").grid(row=4, column=0,sticky=W)
# Creating fifth Entry
text_entry4 = Entry(root, width=35, border=2)
text_entry4.grid(row=4, column=1,padx=10, pady=10)

# Creating a button
Button(root, text="Submit",padx=5, pady=5, bg="#0DF017", fg="#565446", command=submit).grid(row=5, column=1)  # Button to submit
Button(root, text="Query",padx=5, pady=5,bg="#565446", fg="white", command=query).grid(row=5, column=0)    # Button for query
Button(root, text="Exit",padx=20, pady=5,bg="#F00D4E", command=root.destroy).grid(row=5, column=2)  # Button to exit







root.mainloop()
