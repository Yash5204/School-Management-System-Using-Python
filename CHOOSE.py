def assembly():
    res = messagebox.askyesnocancel("Notifications", "If you want to open Assembly Management Part ?")
    if (res == True):
        os.system("python PROJECT1.py")
    else:
        return

def timetable():
    res = messagebox.askyesnocancel("Notifications", "If you want to open Time Table (Schedule) Management Part ?")
    if (res == True):
        os.system("python PROJECT2.py")
    else:
        return

def event():
    res = messagebox.askyesnocancel("Notifications", "If you want to open Special Event Management Part ?")
    if (res == True):
        os.system("python PROJECT3.py")
    else:
        return

def attendance():
    res = messagebox.askyesnocancel("Notifications", "If you want to open Attendance Management Part ?")
    if (res == True):
        os.system("python PROJECT4.py")
    else:
        return

import os
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

root = Tk()
root.title("Choose the work to do")
root.geometry("1350x700+0+0")
# ...................................................................................................................ALL IMAGES
bg_icon = ImageTk.PhotoImage(file="C:/Users/yashdeep1/Pictures/colorful-background-1.jpg")
# ...................................................................................................................VARIABLES
bg_lbl = Label(root, image=bg_icon)
bg_lbl.pack(fill=BOTH)

chooseframe = Frame(root, bg="yellow", relief=GROOVE, bd=7)
chooseframe.place(x=275, y=275, width=770, height=200)

title = Label(root, text="CHOOSE THE PART OF SYSTEM", font=("times new roman", 40, "bold"), bg="blue",fg="white", relief=GROOVE, borderwidth=4)
title.place(x=0, y=0, relwidth=1)

assemblybutton = Button(chooseframe, bd=5, text="ASSEMBLY", font=("times new roman", 20, "bold"), width=20,
                       bg="firebrick1", fg="black", activeforeground="white", activebackground="blue",command=assembly)
assemblybutton.place(x=20, y=20)

ttbutton = Button(chooseframe, bd=5, text="TIME TABLE", font=("times new roman", 20, "bold"), width=20,
                  bg="firebrick1", fg="black", activeforeground="white", activebackground="blue",command=timetable)
ttbutton.place(x=400, y=20)

eventbutton = Button(chooseframe, bd=5, text="SPECIAL EVENTS", font=("times new roman", 20, "bold"), width=20,
                  bg="firebrick1", fg="black", activeforeground="white", activebackground="blue",command=event)
eventbutton.place(x=20, y=100)

attendancebutton = Button(chooseframe, bd=5, text="ATTENDANCE", font=("times new roman", 20, "bold"), width=20,
                  bg="firebrick1", fg="black", activeforeground="white", activebackground="blue",command=attendance)
attendancebutton.place(x=400, y=100)

root.mainloop()

