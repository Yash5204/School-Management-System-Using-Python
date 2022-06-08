import os
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        # ...................................................................................................................ALL IMAGES
        self.bg_icon = ImageTk.PhotoImage(file="C:/Users/yashdeep1/Pictures/bg.jpg")
        self.user_icon = PhotoImage(file="C:/Users/yashdeep1/Pictures/user.png")
        self.logo_icon = ImageTk.PhotoImage(file="C:/Users/yashdeep1/Pictures/user2.jpg")
        self.pass_icon = PhotoImage(file="C:/Users/yashdeep1/Pictures/pass.png")
        # ...................................................................................................................VARIABLES
        global uname, pass_
        uname = StringVar()
        pass_ = StringVar()

        bg_lbl = Label(self.root, image=self.bg_icon)
        bg_lbl.pack()

        title = Label(self.root, text="Login System", font=("times new roman", 40, "bold"), bg="yellow", fg="red",
                      relief=GROOVE, borderwidth=4)
        title.place(x=0, y=0, relwidth=1)

        loginframe = Frame(self.root, bg="white")
        loginframe.place(x=400, y=150)

        logolbl = Label(loginframe, image=self.logo_icon, bd=0)
        logolbl.grid(row=0, columnspan=2, pady=20)

        lbluser = Label(loginframe, text="USERNAME", image=self.user_icon, compound=LEFT,
                        font=("times new roman", 20, "bold"), bg="white")
        lbluser.grid(row=1, column=0, padx=20, pady=10)

        lblpass = Label(loginframe, text="PASSWORD", image=self.pass_icon, compound=LEFT,
                        font=("times new roman", 20, "bold"), bg="white")
        lblpass.grid(row=2, column=0, padx=20, pady=10)

        userentry = Entry(loginframe, bd=5, relief=GROOVE, font=("times", 15), textvariable=uname)
        userentry.grid(row=1, column=1, padx=20, pady=10)

        passentry = Entry(loginframe, bd=5, relief=GROOVE, font=("times", 15), textvariable=pass_)
        passentry.grid(row=2, column=1, padx=20, pady=10)
        # ..................................................................................................................
        loginbutton = Button(loginframe, bd=5, text="Login", width=15, font=("times new roman", 14, "bold"),
                             bg="yellow", fg="red", command=self.login, activeforeground="white",
                             activebackground="blue")
        loginbutton.grid(row=3, column=1, pady=10)

    def login(self):
        if uname.get() == "" or pass_.get() == "":
            messagebox.showerror("Error", "All fields are mandatory")
        elif uname.get() == "Admin" and pass_.get() == "soekhichripur":
            messagebox.showinfo("Logged In", f"Welcome {uname.get()}")
            os.system("python 7.py")
            root.destroy()
        else:
            messagebox.showerror("Error", "Please enter valid username and password")
            return


root = Tk()
obj = Login_System(root)
root.mainloop()
