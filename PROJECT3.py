from tkinter import *
from tkinter import messagebox,ttk,Tk
import pymysql
import time
def add_event():
    condition = Date_var.get ( )
    if (len ( condition ) != 0):
        con = pymysql.connect(host="localhost", user="root", password="yashdeep1", database="schoolmanagementsystem3")
        mycursor = con.cursor()
        mycursor.execute("insert into eventdata values(%s,%s,%s,%s,%s)", (Date_var.get(),Day_var.get(),txt_occupation.get('1.0', END),From_var.get(),To_var.get()))
        con.commit()
        fetch_data()
        clear()
        con.close()
        messagebox.showinfo("Notification", "Record has been inserted")

def fetch_data():
        con = pymysql.connect(host="localhost", user="root", password="yashdeep1", database="schoolmanagementsystem3")
        mycursor = con.cursor()
        mycursor.execute("select * from eventdata")
        rows = mycursor.fetchall()
        if len(rows) != 0:
            event_table.delete(*event_table.get_children())
            for row in rows:
                event_table.insert('', END, values=row)
            con.commit()
        con.close()

def clear():
    Date_var.set("")
    Day_var.set("")
    txt_occupation.delete ( '1.0' , END )
    From_var.set("")
    To_var.set("")

def get_cursor(ev):
        cursor_row = event_table.focus()
        content = event_table.item(cursor_row)
        row = content['values']
        if (len(row)!=0):
            Date_var.set (row[0])
            Day_var.set (row[1])
            txt_occupation.delete ( '1.0' , END )
            txt_occupation.insert ( END , row[2] )
            From_var.set (row[3])
            To_var.set (row[4])

def update_data():
        con = pymysql.connect(host="localhost", user="root", password="yashdeep1", database="schoolmanagementsystem3")
        mycursor = con.cursor()
        mycursor.execute("update eventdata set Day=%s,Occupation=%s,From_=%s,To_=%s where Date=%s",
                         (Day_var.get(),
                          txt_occupation.get ( '1.0' , END ),
                          From_var.get(),
                          To_var.get(),
                          Date_var.get()))
        con.commit()
        fetch_data()
        clear()
        messagebox.showinfo ( "Notifications" ,"Data have been updated" )
        con.close()

def delete_data():
        con = pymysql.connect(host="localhost", user="root", password="yashdeep1", database="schoolmanagementsystem3")
        mycursor = con.cursor()
        mycursor.execute("delete from eventdata where Date=%s", Date_var.get())
        con.commit()
        fetch_data()
        clear()
        con.close()
        messagebox.showinfo("Notification","The selected data have been deleted")

def search_data():
        con = pymysql.connect(host="localhost", user="root", password="yashdeep1", database="schoolmanagementsystem3")
        mycursor = con.cursor()

        mycursor.execute(
            "select * from eventdata where " + str(search_by.get()) + " LIKE '%" + str(search_txt.get()) + "%'")
        rows = mycursor.fetchall()
        if len(rows) != 0:
            event_table.delete(*event_table.get_children())
            for row in rows:
                event_table.insert('', END, values=row)
            con.commit()
        con.close()

#..................................................................................................................................................EXIT BUTTON
def exit_():
        res = messagebox.askyesnocancel("Notification", "Do you want to exit?")
        if (res == True):
            root.destroy()

root = Tk()
root.title("School Management System")
root.geometry("1350x700+0+0")
root.config(bg="blue")
# .....................................................................................
title = Label(root, text="School Management System", font=("times new roman", 40, "bold"), relief=GROOVE, bd=10,bg="yellow", fg="red")
title.place(x=0, y=0, relwidth=1)
#..................................................................................................................
Date_var = StringVar()
Day_var = StringVar()
From_var = StringVar()
To_var = StringVar()
search_by = StringVar()
search_txt = StringVar()
#..........................................................................................................................................................................TIME AND DATE
def tick( ):
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%y")
    clock.config(text='Date :'+date_string+ "\n"+ 'Time :'+time_string)
    clock.after(500,tick)
#.............................................................................................................................................................CLOCK CONFIGURATION
clock = Label(root,relief=RIDGE,borderwidth=4,font=("times",19,"bold"),width=20,bg="#21ff00",bd=10)
clock.place(x=0,y=0)
tick()
# ......................................................................................................................................................MANAGE FRAME
Manage_Frame = Frame(root, bd=4, relief=RIDGE, bg="red")
Manage_Frame.place(x=20, y=100, width=520, height=570)

m_title = Label(Manage_Frame, text="Manage Assemblies", bg="red", fg="white", font=("times new roman", 30, "bold"))
m_title.grid(row=0, columnspan=2, pady=20)

lbl_date = Label(Manage_Frame, text="Date:", bg="red", fg="white", font=("times new roman", 27, "bold"))
lbl_date.grid(row=1, column=0, padx=10, pady=10, sticky="w")

txt_date = Entry(Manage_Frame, textvariable=Date_var, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
txt_date.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lbl_day = Label(Manage_Frame, text="Day:", bg="red", fg="white", font=("times new roman", 25, "bold"))
lbl_day.grid(row=2, column=0, padx=10, pady=10, sticky="w")

combo_day = ttk.Combobox(Manage_Frame, textvariable=Day_var, font=("times new roman", 19, "bold"), state="readonly")
combo_day["values"] = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
combo_day.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lbl_occupation = Label(Manage_Frame, text="Occupation:", bg="red", fg="white", font=("times new roman", 25, "bold"))
lbl_occupation.grid(row=3, column=0, padx=10, pady=10, sticky="w")

txt_occupation = Text(Manage_Frame, width=25, height=4, font=("", 15))
txt_occupation.grid(row=3, column=1, padx=10, pady=10, sticky="w")

lbl_timing = Label(Manage_Frame, text="Timings:-", bg="red", fg="white", font=("times new roman", 25, "bold"))
lbl_timing.grid(row=4, column=0, padx=10, pady=10, sticky="w")

lbl_from = Label(Manage_Frame, text="From:", bg="red", fg="white", font=("times new roman", 25, "bold"))
lbl_from.place(x=210, y=350, width=100)

txt_from = Entry(Manage_Frame, textvariable=From_var, font=("times new roman", 20, "bold"), bd=5,relief=GROOVE)
txt_from.place(x=340, y=350, width=140)

lbl_to = Label(Manage_Frame, text="To:", bg="red", fg="white", font=("times new roman", 25, "bold"))
lbl_to.place(x=210, y=410, width=80)

txt_to = Entry(Manage_Frame, textvariable=To_var, font=("times new roman", 20, "bold"), bd=5,relief=GROOVE)
txt_to.place(x=340, y=410, width=140)

# ....................................................................................................................................BUTTON FRAME
btn_frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="red")
btn_frame.place(x=20, y=485, width=470)

addbtn = Button(btn_frame, text="ADD", width=10, command=add_event).grid(row=0, column=0, padx=5, pady=10)
updatebtn = Button(btn_frame, text="UPDATE", width=10, command=update_data).grid(row=0, column=1, padx=5, pady=10)
deletebtn = Button(btn_frame, text="DELETE", width=10, command=delete_data).grid(row=0, column=2, padx=5, pady=10)
clearbtn = Button(btn_frame, text="CLEAR", width=10, command=clear).grid(row=0, column=3, padx=5, pady=10)
exitbtn = Button(btn_frame, text="EXIT", width=10, command=exit_).grid(row=0, column=4, padx=5, pady=10)
# ....................................................................................................................................DETAIL FRAME
Detail_Frame = Frame(root, bd=4, relief=RIDGE, bg="red")
Detail_Frame.place(x=590, y=100, width=750, height=570)

lbl_search = Label(Detail_Frame, text="Search By", bg="red", fg="white", font=("times new roman", 25, "bold"))
lbl_search.grid(row=0, column=0, padx=20, pady=10, sticky="w")

combo_search = ttk.Combobox(Detail_Frame, textvariable=search_by, width=10, font=("times new roman", 19, "bold"),state="readonly")
combo_search["values"] = ("Date", "Day")
combo_search.grid(row=0, column=1, padx=20, pady=10)

txt_search = Entry(Detail_Frame, textvariable=search_txt, width=15, font=("times new roman", 12, "bold"), bd=5,
                   relief=GROOVE)
txt_search.grid(row=0, column=2, padx=15, pady=10, sticky="w")

searchbtn = Button(Detail_Frame, text="SEARCH", width=10, command=search_data).grid(row=0, column=3, padx=10,
                                                                                    pady=10)
showallbtn = Button(Detail_Frame, text="SHOWALL", width=10, command=fetch_data).grid(row=0, column=4, padx=10,
                                                                                     pady=10)

# ......................................................................................................................Table Frame
table_frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="red")
table_frame.place(x=10, y=70, width=720, height=485)

scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
scroll_y = Scrollbar(table_frame, orient=VERTICAL)
event_table = ttk.Treeview(table_frame, columns=("date", "day", "occupation", "from", "to"),
                              xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
style = ttk.Style()
style.configure("Treeview.Heading", font=("times", 15, "bold"), foreground="blue")
style.configure("Treeview", font=("times", 12, "bold"), foreground="black")

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=event_table.xview)
scroll_y.config(command=event_table.yview)
event_table.heading("date", text="Date")
event_table.heading("day", text="Day")
event_table.heading("occupation", text="Occupation")
event_table.heading("from", text="From")
event_table.heading("to", text="To")
event_table["show"] = "headings"
event_table.column("date", width=100)
event_table.column("day", width=100)
event_table.column("occupation", width=400)
event_table.column("from", width=80)
event_table.column("to", width=80)
event_table.pack(fill=BOTH, expand=1)
fetch_data()
event_table.bind("<ButtonRelease-1>", get_cursor)

root.mainloop()
