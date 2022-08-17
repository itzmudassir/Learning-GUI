# PROGRAMMED BY: Mudassir Nadeem

# This program is used to login to IUB website and get the access token.

from tkinter import *
from PIL import Image, ImageTk
import customtkinter
from tkinter.font import BOLD




# app CREATION
app = customtkinter.CTk()
app.title("IUB Login Page")
app.geometry("800x600+300+85")
app.configure(background='#ececec')
app.resizable(False, False)
app.iconbitmap(r'Elements\iub_logo.ico')



# FUNCTIONS FOR THE LOGIN PAGE

# LOGIN BUTTON FUNCTION
def button_event():
    if entry_email.get() == "itzmudassir07@gmail.com" and entry_password.get() == "mudassir12345.":
        app.destroy()

    else:
        Label(app, text="Invalid Email or Password", font=("DM Sans", 10), fg="red", bg="white").place(x=310, y=263)



# BACKGROUND IMAGE
user_image = ImageTk.PhotoImage(Image.open(r'Elements\Login.png'))
user_image_label = Label(app, image=user_image)
user_image_label.pack(fill = "both", expand = "yes")


# USERNAME AND PASSWORD ENTRY

# Email Entry
entry_email = customtkinter.CTkEntry(master=app,
                               placeholder_text="example@gmail.com",
                               width=270,
                               height=53,
                               fg_color = "#ececec",
                               border_color="#ececec",
                               text_color="gray",
                               border_width=0,
                               corner_radius=5)
                               
entry_email.place(x=280, y=294)

# Password Entry

entry_password = customtkinter.CTkEntry(master=app,
                                 placeholder_text="********",
                                 width=270,
                                 height=53,
                                 show = "*",
                                 fg_color = "#ececec",
                                 border_color="#ececec",
                                 text_color="gray",
                                 border_width=0,
                                 
                                 corner_radius=5)
                                 
entry_password.place(x=280, y=397)

# LOGIN BUTTON              
button = customtkinter.CTkButton(master=app,
                                 width=208,
                                 height=52,
                                 border_width=0,
                                 corner_radius=15,
                                 bg_color="white",
                                 fg_color="#2d367b",
                                 text="Login",
                                 text_color="white",
                                 text_font=("DM Sans",14, BOLD),
                                 hover_color="black",
                                 cursor="hand2",
                                 command=button_event)
button.place(x=295, y=488)








# MAINLOOP
app.mainloop()
