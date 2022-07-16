from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()

root.title("Practice")  # Title name
root.wm_attributes('-fullscreen', 'True')    # Screen Size
root.configure(background='white')    # Background color of Window
var = IntVar()    # Declaring variable "var" datatype
r = IntVar()      # Declaring variable "r" datatype


def click():    # Creating "Click" Function
    global var  # Declaring "var" variable as global

    var.get()   # Getting the value of "var"
    r.get()     # Getting the value of "r"
    if var.get() == 0:   # Applying first condition
        top = Toplevel()  # Creating Multi Window
        top.title("this is second window")   # Multi window title
        top.wm_attributes('-fullscreen', 'True')   # Multi window size

        Label(top, text="COMING SOON", font="Arial 28 bold").pack()   # Creating a label of "Coming Soon"
        Radiobutton(top, text="Radio 1", variable=r, value=1).pack()   # Creating a first radio button
        Radiobutton(top, text="Radio 2", variable=r, value=2).pack()   # creating a second radio button

        Button(top, text="Back", command=top.destroy).pack()     # Creating a back button

        def click1():   # Creating a function(click1) within a function
            if r.get() == 1:   # Applying first condition
                top = Toplevel()   # Creating Multi window
                top.title("this is second window")   # Multi Window size
                top.wm_attributes('-fullscreen', 'True')  # Multi Window size

                Label(top, text="COMING SOON", font="Arial 28 bold").pack()   # Creating a label of "Coming soon"
                Button(top, text="Back", command=top.destroy).pack()   # Creating a back button
            if r.get() == 2:   # Applying 2nd condition
                top = Toplevel()  # Creating Multi window
                top.title("this is second window")  # Multi window title
                top.wm_attributes('-fullscreen', 'True')  # Multi window size
                Label(top, image=my_img1).place(x=20, y=20)  # Adding an image to the Multi Window
                Button(top, text="Back", command=top.destroy).pack()  # Creating a back button
            
            if r.get() == 0:   # Applying 3rd condition
                top = Toplevel()  # Creating Multi window
                top.title("this is second window")  # Multi window title
                top.wm_attributes('-fullscreen', 'True')  # Multi window size
                messagebox.showinfo("Error", "Please select a radio button")  # Creating a message box

            if r.get == 0:
                top = Toplevel()  # Creating Multi window
                top.title("this is second window")  # Multi Window size
                top.wm_attributes('-fullscreen', 'True')  # Multi Window size
                Label(top, text="COMING", font="Arial 28 bold").pack()

        Button(top, text="Click", command=click1).pack()  # Button for the radio buttons

    if var.get() == 1:   # Applying 2nd condition
        top = Toplevel()  # Creating Multi Window
        top.title("this is second window")  # Multi window title
        top.wm_attributes('-fullscreen', 'True')  # Multi window size
        Label(top, image=my_img1).place(x=20, y=20)  # Adding an image
        Button(top, text="Back", command=top.destroy).pack()   # Creating a back button


Checkbutton(root, text="Please check the box", variable=var).pack()   # Creating a Checkbox button
Button(root, text="Button 1", bg='#ff0000', fg='#ffffff', command=click).pack()  # Button for Checkbox button
Button(root, text="Back", command=root.destroy).pack()  # Creating a back button


my_img1 = ImageTk.PhotoImage(Image.open("C:\Mudassir\Pictures\pic.png"))  # Image location

# Mainloop
root.mainloop()
