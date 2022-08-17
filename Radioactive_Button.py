from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Pazhong Automation")
r=  IntVar()
#r.set("3")

def click(r):
    global radio1
    global radio2
    global radio3
    global radio4

    #Label(root,text=r.get()).pack()
    #button = Button(root, text="click me!", command=lambda: click(r.get())).pack()
    if   r == 1:

        respose = messagebox.askyesnocancel("this is my popup", "would you like to prcessed!!")
        if respose == 1:
            radio1= Radiobutton(root, text="option 1",bg="red", variable=r, value=1, ).place(x= 20 ,y= 10)
        else:
            radio1 = Radiobutton(root, text="option 1", bg="green", variable=r, value=1, ).place(x=20, y=10)



    elif r == 2:
         Label(root, text="R have value 2").pack()
    else:
        Label(root,text="okay okay").pack()


radio1= Radiobutton(root,text="option 1",variable=r,value=1,command=lambda:click(r.get())).place(x= 20 ,y= 10)
radio2= Radiobutton(root,text="option 2",variable=r,value=2,command=lambda :click(r.get())).place(x= 20 ,y= 40)
radio3= Radiobutton(root,text="option 3",variable=r,value=3,command=lambda :click(r.get())).place(x= 20 ,y= 70)
radio4= Radiobutton(root,text="option 4",variable=r,value=4,command=lambda :click(r.get())).place(x= 20 ,y= 100)

#button=Button(root,text="click me!",command=lambda :click(r.get())).pack()
#lable1=Label(root,text=r.get()).pack()

root.mainloop()
