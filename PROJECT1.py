from tkinter import *
from tkinter import messagebox , ttk , Tk
import pymysql
import time

def add_assembly():
    condition = Date_var.get ( )
    if (len ( condition ) != 0):
        con = pymysql.connect(host="localhost", user="root", password="yashdeep1", database="schoolmanagementsystem")
        mycursor = con.cursor()
        mycursor.execute("insert into assemblydata values(%s,%s,%s,%s,%s)", (
        Date_var.get(), Class_var.get(), Section_var.get(), Teacher_var.get(), txt_theme.get('1.0', END)))
        con.commit()
        fetch_data()
        clear()
        con.close()
        messagebox.showinfo("Notification", "Record has been inserted")

def fetch_data():
        con = pymysql.connect(host="localhost", user="root", password="yashdeep1", database="schoolmanagementsystem")
        mycursor = con.cursor()
        mycursor.execute("select * from assemblydata")
        rows = mycursor.fetchall()
        if len(rows) != 0:
            assembly_table.delete(*assembly_table.get_children())
            for row in rows:
                assembly_table.insert('', END, values=row)
            con.commit()
        con.close()

def clear():
    Date_var.set("")
    Class_var.set("")
    Section_var.set("")
    Teacher_var.set("")
    txt_theme.delete('1.0', END)

def get_cursor(ev):
        cursor_row = assembly_table.focus()
        content = assembly_table.item(cursor_row)
        row = content['values']
        if (len(row)!=0):
            Date_var.set(row[0])
            Class_var.set(row[1])
            Section_var.set(row[2])
            Teacher_var.set(row[3])
            txt_theme.delete('1.0', END)
            txt_theme.insert(END, row[4])

def update_data():
        con = pymysql.connect(host="localhost", user="root", password="yashdeep1", database="schoolmanagementsystem")
        mycursor = con.cursor()
        mycursor.execute("update assemblydata set Class=%s,Section=%s,Teacher=%s,Theme=%s where Date=%s",
                         (Class_var.get(),
                          Section_var.get(),
                          Teacher_var.get(),
                          txt_theme.get('1.0', END),
                          Date_var.get()))
        con.commit()
        fetch_data()
        clear()
        messagebox.showinfo ( "Notifications" , "Data have been updated" )
        con.close()

def delete_data():
        con = pymysql.connect(host="localhost", user="root", password="yashdeep1", database="schoolmanagementsystem")
        mycursor = con.cursor()
        mycursor.execute("delete from assemblydata where Date=%s", Date_var.get())
        con.commit()
        fetch_data()
        clear()
        con.close()
        messagebox.showinfo("Notification","The selected data have been deleted")

def search_data():
        con = pymysql.connect(host="localhost", user="root", password="yashdeep1", database="schoolmanagementsystem")
        mycursor = con.cursor()

        mycursor.execute(
            "select * from assemblydata where " + str(search_by.get()) + " LIKE '%" + str(search_txt.get()) + "%'")
        rows = mycursor.fetchall()
        if len(rows) != 0:
            assembly_table.delete(*assembly_table.get_children())
            for row in rows:
                assembly_table.insert('', END, values=row)
            con.commit()
        con.close()

        # ..................................................................................................................................................EXIT BUTTON

def exit_():
        res = messagebox.askyesnocancel("Notification", "Do you want to exit?")
        if (res == True):
            root.destroy()

root = Tk()
root.title("School Management System")
root.geometry("1350x700+0+0")
root.config(bg="blue")
# .....................................................................................
title = Label(root, text="School Management System", font=("times new roman", 40, "bold"), relief=GROOVE, bd=10,
                  bg="yellow", fg="red")
title.place(x=0, y=0, relwidth=1)
#..................................................................................................................
Date_var = StringVar()
Class_var = StringVar()
Section_var = StringVar()
Teacher_var = StringVar()
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
Manage_Frame.place(x=20, y=100, width=500, height=570)

m_title = Label(Manage_Frame, text="Manage Assemblies", bg="red", fg="white", font=("times new roman", 30, "bold"))
m_title.grid(row=0, columnspan=2, pady=20)

lbl_date = Label(Manage_Frame, text="Date:", bg="red", fg="white", font=("times new roman", 25, "bold"))
lbl_date.grid(row=1, column=0, padx=20, pady=10, sticky="w")

txt_date = Entry(Manage_Frame, textvariable=Date_var, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
txt_date.grid(row=1, column=1, padx=15, pady=10, sticky="w")

lbl_class = Label(Manage_Frame, text="Class:", bg="red", fg="white", font=("times new roman", 25, "bold"))
lbl_class.grid(row=2, column=0, padx=19, pady=10, sticky="w")

combo_class = ttk.Combobox(Manage_Frame, textvariable=Class_var, font=("times new roman", 19, "bold"),
                           state="readonly")
combo_class["values"] = (
"Nursery", "Primary", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th")
combo_class.grid(row=2, column=1, padx=22, pady=10)

lbl_sec = Label(Manage_Frame, text="Section:", bg="red", fg="white", font=("times new roman", 25, "bold"))
lbl_sec.grid(row=3, column=0, padx=19, pady=10, sticky="w")

combo_Section = ttk.Combobox(Manage_Frame, textvariable=Section_var, font=("times new roman", 19, "bold"),
                             state="readonly")
combo_Section["values"] = ("A", "B", "C", "D")
combo_Section.grid(row=3, column=1, padx=22, pady=10)

lbl_teacher = Label(Manage_Frame, text="Teacher:", bg="red", fg="white", font=("times new roman", 25, "bold"))
lbl_teacher.grid(row=4, column=0, padx=20, pady=10, sticky="w")

txt_teacher = Entry(Manage_Frame, textvariable=Teacher_var, font=("times new roman", 20, "bold"), bd=5,
                    relief=GROOVE)
txt_teacher.grid(row=4, column=1, padx=15, pady=10, sticky="w")

lbl_theme = Label(Manage_Frame, text="Theme:", bg="red", fg="white", font=("times new roman", 25, "bold"))
lbl_theme.grid(row=5, column=0, padx=20, pady=10, sticky="w")

txt_theme = Text(Manage_Frame, width=25, height=4, font=("", 15))
txt_theme.grid(row=5, column=1, padx=20, pady=10, sticky="w")
# ....................................................................................................................................BUTTON FRAME
btn_frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="red")
btn_frame.place(x=10, y=475, width=470)

addbtn = Button(btn_frame, text="ADD", width=10, command=add_assembly).grid(row=0, column=0, padx=5, pady=10)
updatebtn = Button(btn_frame, text="UPDATE", width=10, command=update_data).grid(row=0, column=1, padx=5, pady=10)
deletebtn = Button(btn_frame, text="DELETE", width=10, command=delete_data).grid(row=0, column=2, padx=5, pady=10)
clearbtn = Button(btn_frame, text="CLEAR", width=10, command=clear).grid(row=0, column=3, padx=5, pady=10)
exitbtn = Button(btn_frame, text="EXIT", width=10, command=exit_).grid(row=0, column=4, padx=5, pady=10)
# ....................................................................................................................................DETAIL FRAME
Detail_Frame = Frame(root, bd=4, relief=RIDGE, bg="red")
Detail_Frame.place(x=550, y=100, width=750, height=570)

lbl_search = Label(Detail_Frame, text="Search By", bg="red", fg="white", font=("times new roman", 25, "bold"))
lbl_search.grid(row=0, column=0, padx=20, pady=10, sticky="w")

combo_search = ttk.Combobox(Detail_Frame, textvariable=search_by, width=10, font=("times new roman", 19, "bold"),
                            state="readonly")
combo_search["values"] = ("Date", "Class", "Section")
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
assembly_table = ttk.Treeview(table_frame, columns=("date", "class", "section", "teacher", "theme"),
                              xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
style = ttk.Style()
style.configure("Treeview.Heading", font=("times", 15, "bold"), foreground="blue")
style.configure("Treeview", font=("times", 12, "bold"), foreground="black")

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=assembly_table.xview)
scroll_y.config(command=assembly_table.yview)
assembly_table.heading("date", text="Date")
assembly_table.heading("class", text="Class")
assembly_table.heading("section", text="Section")
assembly_table.heading("teacher", text="Teacher")
assembly_table.heading("theme", text="Theme")
assembly_table["show"] = "headings"
assembly_table.column("date", width=100)
assembly_table.column("class", width=80)
assembly_table.column("section", width=80)
assembly_table.column("theme", width=400)
assembly_table.column("teacher", width=200)
assembly_table.pack(fill=BOTH, expand=1)
fetch_data()
assembly_table.bind("<ButtonRelease-1>", get_cursor)

root.mainloop()
