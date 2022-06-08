from tkinter import *
from tkinter import ttk, Tk
from tkinter import messagebox, Toplevel
import pymysql
from PIL import ImageTk
import time
def add_timetable():
    condition = dval.get()
    if (len(condition) != 0):
        con = pymysql.connect(host="localhost", user="root", password="yashdeep1", database="schoolmanagementsystem2")
        mycursor = con.cursor()
        mycursor.execute("insert into ttdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                         (dval.get(), daval.get(), cval.get(), sval.get(), p1val.get(), f1val.get(), t1val.get(),
                          p2val.get(), f2val.get(), t2val.get(), p3val.get(), f3val.get(), t3val.get(), p4val.get(),
                          f4val.get(), t4val.get(), p5val.get(), f5val.get(), t5val.get(), p6val.get(), f6val.get(),
                          t6val.get()))

        con.commit()
        fetch_data()
        clear()
        con.close()
        messagebox.showinfo("Notification", "Record has been inserted")
    else:
        messagebox.showerror("Error", "Date cannot be empty")


def fetch_data():
    con = pymysql.connect(host="localhost", user="root", password="yashdeep1", database="schoolmanagementsystem2")
    mycursor = con.cursor()
    mycursor.execute("select * from ttdata")
    rows = mycursor.fetchall()
    if len(rows) != 0:
        tt_table.delete(*tt_table.get_children())
        for row in rows:
            tt_table.insert('', END, values=row)
        con.commit()
    con.close()


def clear():
    dval.set("")
    daval.set("")
    cval.set("")
    sval.set("")
    p1val.set("")
    f1val.set("")
    t1val.set("")
    p2val.set("")
    f2val.set("")
    t2val.set("")
    p3val.set("")
    f3val.set("")
    t3val.set("")
    p4val.set("")
    f4val.set("")
    t4val.set("")
    p5val.set("")
    f5val.set("")
    t5val.set("")
    p6val.set("")
    f6val.set("")
    t6val.set("")


def get_cursor(ev):
    cursor_row = tt_table.focus()
    content = tt_table.item(cursor_row)
    row = content['values']
    if (len(row) != 0):
        dval.set(row[0])
        daval.set(row[1])
        cval.set(row[2])
        sval.set(row[3])
        p1val.set(row[4])
        f1val.set(row[5])
        t1val.set(row[6])
        p2val.set(row[7])
        f2val.set(row[8])
        t2val.set(row[9])
        p3val.set(row[10])
        f3val.set(row[11])
        t3val.set(row[12])
        p4val.set(row[13])
        f4val.set(row[14])
        t4val.set(row[15])
        p5val.set(row[16])
        f5val.set(row[17])
        t5val.set(row[18])
        p6val.set(row[19])
        f6val.set(row[20])
        t6val.set(row[21])


def update_data():
    con = pymysql.connect ( host="localhost" , user="root" , password="yashdeep1" , database="schoolmanagementsystem2" )
    mycursor = con.cursor ( )
    mycursor.execute ( "update ttdata set Day=%s,Class=%s,Section=%s,P1=%s,F1=%s,T1=%s,P2=%s,F2=%s,T2=%s,P3=%s,F3=%s,T3=%s,P4=%s,F4=%s,T4=%s,P5=%s,F5=%s,T5=%s,P6=%s,F6=%s,T6=%s where Date=%s" ,
                       (daval.get ( ) ,
                        cval.get ( ) ,
                        sval.get ( ) ,
                        p1val.get ( ) ,
                        f1val.get ( ) ,
                        t1val.get ( ) ,
                        p1val.get ( ) ,
                        f1val.get ( ) ,
                        t1val.get ( ) ,
                        p1val.get ( ) ,
                        f1val.get ( ) ,
                        t1val.get ( ) ,
                        p4val.get ( ) ,
                        f4val.get ( ) ,
                        t4val.get ( ) ,
                        p5val.get ( ) ,
                        f5val.get ( ) ,
                        t5val.get ( ) ,
                        p6val.get ( ) ,
                        f6val.get ( ) ,
                        t6val.get ( ) ,
                        dval.get ( )) )
    con.commit ( )
    fetch_data ( )
    clear ( )
    messagebox.showinfo ( "Notifications" , "Data have been updated" )
    con.close ( )

def delete_data():
    con = pymysql.connect(host="localhost", user="root", password="yashdeep1", database="schoolmanagementsystem2")
    mycursor = con.cursor()
    mycursor.execute("delete from ttdata where Date=%s", dval.get())
    con.commit()
    fetch_data()
    clear()
    con.close()
    messagebox.showinfo ( "Notification" , "The selected data have been deleted" )

def search_data():
    con = pymysql.connect(host="localhost", user="root", password="yashdeep1", database="schoolmanagementsystem2")
    mycursor = con.cursor()

    mycursor.execute("select * from ttdata where " + str(search_by.get()) + " LIKE '%" + str(search_txt.get()) + "%'")
    rows = mycursor.fetchall()
    if len(rows) != 0:
        tt_table.delete(*tt_table.get_children())
        for row in rows:
            tt_table.insert('', END, values=row)
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
# ......................................................................................................................................................VARIABLES
dval = StringVar()
daval = StringVar()
cval = StringVar()
sval = StringVar()
p1val = StringVar()
f1val = StringVar()
t1val = StringVar()
p2val = StringVar()
f2val = StringVar()
t2val = StringVar()
p3val = StringVar()
f3val = StringVar()
t3val = StringVar()
p4val = StringVar()
f4val = StringVar()
t4val = StringVar()
p5val = StringVar()
f5val = StringVar()
t5val = StringVar()
p6val = StringVar()
f6val = StringVar()
t6val = StringVar()
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
Manage_Frame.place(x=20, y=100, width=560, height=570)

m_title = Label(Manage_Frame, text="Manage Timetable", bg="red", fg="white", font=("times new roman", 30, "bold"))
m_title.place(x=70, y=9, width=400)

lbl_date = Label(Manage_Frame, text="Date:", bg="red", fg="white", font=("times new roman", 20, "bold"), anchor="w")
lbl_date.place(x=10, y=80, width=100)

txt_date = Entry(Manage_Frame, textvariable=dval, font=("times new roman", 20, "bold"), width=10, bd=5, relief=GROOVE)
txt_date.place(x=100, y=78, width=180)

lbl_day = Label(Manage_Frame, text="Day:", bg="red", fg="white", font=("times new roman", 20, "bold"), anchor="w")
lbl_day.place(x=300, y=80, width=80)

combo_day = ttk.Combobox(Manage_Frame, textvariable=daval, font=("times new roman", 19, "bold"), state="readonly")
combo_day["values"] = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
combo_day.place(x=370, y=80, width=170)

lbl_class = Label(Manage_Frame, text="Class:", bg="red", fg="white", font=("times new roman", 20, "bold"), anchor="w")
lbl_class.place(x=10, y=130, width=110)

combo_class = ttk.Combobox(Manage_Frame, textvariable=cval, font=("times new roman", 19, "bold"), state="readonly")
combo_class["values"] = (
"Nursery", "Primary", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th")
combo_class.place(x=100, y=128, width=180)

lbl_sec = Label(Manage_Frame, text="Sec:", bg="red", fg="white", font=("times new roman", 20, "bold"), anchor="w")
lbl_sec.place(x=300, y=130, width=80)

combo_Section = ttk.Combobox(Manage_Frame, textvariable=sval, font=("times new roman", 19, "bold"), state="readonly")
combo_Section["values"] = ("A", "B", "C", "D")
combo_Section.place(x=370, y=130, width=170)

lbl_p1 = Label(Manage_Frame, text="P-1:", bg="red", fg="white", font=("times new roman", 20, "bold"), anchor="w")
lbl_p1.place(x=10, y=180, width=50)

txt_p1 = Entry(Manage_Frame, textvariable=p1val, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
txt_p1.place(x=70, y=180, width=130)

lbl_f1 = Label(Manage_Frame, text="From", bg="red", fg="white", font=("times new roman", 20, "bold"), anchor="w")
lbl_f1.place(x=210, y=180, width=70)

txt_f1 = Entry(Manage_Frame, width=10, textvariable=f1val, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
txt_f1.place(x=290, y=180, width=100)

lbl_t1 = Label(Manage_Frame, text="To", bg="red", fg="white", font=("times new roman", 20, "bold"), anchor="w")
lbl_t1.place(x=400, y=180, width=50)

txt_t1 = Entry(Manage_Frame, width=10, textvariable=t1val, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
txt_t1.place(x=450, y=180, width=100)

lbl_p2 = Label(Manage_Frame, text="P-2:", bg="red", fg="white", font=("times new roman", 20, "bold"), anchor="w")
lbl_p2.place(x=10, y=230, width=50)

txt_p2 = Entry(Manage_Frame, textvariable=p2val, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
txt_p2.place(x=70, y=230, width=130)

lbl_f2 = Label(Manage_Frame, text="From", bg="red", fg="white", font=("times new roman", 20, "bold"), anchor="w")
lbl_f2.place(x=210, y=230, width=70)

txt_f2 = Entry(Manage_Frame, width=10, textvariable=f2val, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
txt_f2.place(x=290, y=230, width=100)

lbl_t2 = Label(Manage_Frame, text="To", bg="red", fg="white", font=("times new roman", 20, "bold"), anchor="w")
lbl_t2.place(x=400, y=230, width=50)

txt_t2 = Entry(Manage_Frame, width=10, textvariable=t2val, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
txt_t2.place(x=450, y=230, width=100)

lbl_p3 = Label(Manage_Frame, text="P-3:", bg="red", fg="white", font=("times new roman", 20, "bold"), anchor="w")
lbl_p3.place(x=10, y=280, width=50)

txt_p3 = Entry(Manage_Frame, textvariable=p3val, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
txt_p3.place(x=70, y=280, width=130)

lbl_f3 = Label(Manage_Frame, text="From", bg="red", fg="white", font=("times new roman", 20, "bold"), anchor="w")
lbl_f3.place(x=210, y=280, width=70)

txt_f3 = Entry(Manage_Frame, width=10, textvariable=f3val, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
txt_f3.place(x=290, y=280, width=100)

lbl_t3 = Label(Manage_Frame, text="To", bg="red", fg="white", font=("times new roman", 20, "bold"), anchor="w")
lbl_t3.place(x=400, y=280, width=50)

txt_t3 = Entry(Manage_Frame, width=10, textvariable=t3val, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
txt_t3.place(x=450, y=280, width=100)

lbl_p4 = Label(Manage_Frame, text="P-4:", bg="red", fg="white", font=("times new roman", 20, "bold"), anchor="w")
lbl_p4.place(x=10, y=330, width=50)

txt_p4 = Entry(Manage_Frame, textvariable=p4val, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
txt_p4.place(x=70, y=330, width=130)

lbl_f4 = Label(Manage_Frame, text="From", bg="red", fg="white", font=("times new roman", 20, "bold"), anchor="w")
lbl_f4.place(x=210, y=330, width=70)

txt_f4 = Entry(Manage_Frame, width=10, textvariable=f4val, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
txt_f4.place(x=290, y=330, width=100)

lbl_t4 = Label(Manage_Frame, text="To", bg="red", fg="white", font=("times new roman", 20, "bold"), anchor="w")
lbl_t4.place(x=400, y=330, width=50)

txt_t4 = Entry(Manage_Frame, width=10, textvariable=t4val, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
txt_t4.place(x=450, y=330, width=100)

lbl_p5 = Label(Manage_Frame, text="P-5:", bg="red", fg="white", font=("times new roman", 20, "bold"), anchor="w")
lbl_p5.place(x=10, y=380, width=50)

txt_p5 = Entry(Manage_Frame, textvariable=p5val, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
txt_p5.place(x=70, y=380, width=130)

lbl_f5 = Label(Manage_Frame, text="From", bg="red", fg="white", font=("times new roman", 20, "bold"), anchor="w")
lbl_f5.place(x=210, y=380, width=70)

txt_f5 = Entry(Manage_Frame, width=10, textvariable=f5val, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
txt_f5.place(x=290, y=380, width=100)

lbl_t5 = Label(Manage_Frame, text="To", bg="red", fg="white", font=("times new roman", 20, "bold"), anchor="w")
lbl_t5.place(x=400, y=380, width=50)

txt_t5 = Entry(Manage_Frame, width=10, textvariable=t5val, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
txt_t5.place(x=450, y=380, width=100)

lbl_p6 = Label(Manage_Frame, text="P-6:", bg="red", fg="white", font=("times new roman", 20, "bold"), anchor="w")
lbl_p6.place(x=10, y=430, width=50)

txt_p6 = Entry(Manage_Frame, textvariable=p6val, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
txt_p6.place(x=70, y=430, width=130)

lbl_f6 = Label(Manage_Frame, text="From", bg="red", fg="white", font=("times new roman", 20, "bold"), anchor="w")
lbl_f6.place(x=210, y=430, width=70)

txt_f6 = Entry(Manage_Frame, width=10, textvariable=f6val, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
txt_f6.place(x=290, y=430, width=100)

lbl_t6 = Label(Manage_Frame, text="To", bg="red", fg="white", font=("times new roman", 20, "bold"), anchor="w")
lbl_t6.place(x=400, y=430, width=50)

txt_t6 = Entry(Manage_Frame, width=10, textvariable=t6val, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
txt_t6.place(x=450, y=430, width=100)
# ....................................................................................................................................BUTTON FRAME
btn_frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="red")
btn_frame.place(x=50, y=485, width=470)

addbtn = Button(btn_frame, text="ADD", width=10, command=add_timetable).grid(row=0, column=0, padx=5, pady=10)
updatebtn = Button(btn_frame, text="UPDATE", width=10, command=update_data).grid(row=0, column=1, padx=5, pady=10)
deletebtn = Button(btn_frame, text="DELETE", width=10, command=delete_data).grid(row=0, column=2, padx=5, pady=10)
clearbtn = Button(btn_frame, text="CLEAR", width=10, command=clear).grid(row=0, column=3, padx=5, pady=10)
exitbtn = Button(btn_frame, text="EXIT", width=10, command=exit_).grid(row=0, column=4, padx=5, pady=10)
# ....................................................................................................................................DETAIL FRAME
Detail_Frame = Frame(root, bd=4, relief=RIDGE, bg="red")
Detail_Frame.place(x=590, y=100, width=740, height=570)

lbl_search = Label(Detail_Frame, text="Search By", bg="red", fg="white", font=("times new roman", 25, "bold"))
lbl_search.grid(row=0, column=0, padx=10, pady=10, sticky="w")

combo_search = ttk.Combobox(Detail_Frame, textvariable=search_by, width=10, font=("times new roman", 19, "bold"),
                            state="readonly")
combo_search["values"] = ("Date", "Class", "Section")
combo_search.grid(row=0, column=1, padx=20, pady=10)

txt_search = Entry(Detail_Frame, textvariable=search_txt, width=15, font=("times new roman", 12, "bold"), bd=5,
                   relief=GROOVE)
txt_search.grid(row=0, column=2, padx=15, pady=10, sticky="w")

searchbtn = Button(Detail_Frame, text="SEARCH", width=10, command=search_data).grid(row=0, column=3, padx=10, pady=10)
showallbtn = Button(Detail_Frame, text="SHOWALL", width=10, command=fetch_data).grid(row=0, column=4, padx=10, pady=10)

# .................................................................................................................................................Table Frame
table_frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="red")
table_frame.place(x=10, y=70, width=720, height=475)

scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
scroll_y = Scrollbar(table_frame, orient=VERTICAL)
tt_table = ttk.Treeview(table_frame, columns=(
"date", "day", "class", "section", "p1", "f1", "t1", "p2", "f2", "t2", "p3", "f3", "t3", "p4", "f4", "t4", "p5", "f5",
"t5", "p6", "f6", "t6"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

style = ttk.Style()
style.configure("Treeview.Heading", font=("times", 15, "bold"), foreground="blue")
style.configure("Treeview", font=("times", 12, "bold"), foreground="black")

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=tt_table.xview)
scroll_y.config(command=tt_table.yview)
tt_table.heading("date", text="Date")
tt_table.heading("day", text="Day")
tt_table.heading("class", text="Class")
tt_table.heading("section", text="Section")
tt_table.heading("p1", text="Period-1")
tt_table.heading("f1", text="From")
tt_table.heading("t1", text="To")
tt_table.heading("p2", text="Period-2")
tt_table.heading("f2", text="From")
tt_table.heading("t2", text="To")
tt_table.heading("p3", text="Period-3")
tt_table.heading("f3", text="From")
tt_table.heading("t3", text="To")
tt_table.heading("p4", text="Period-4")
tt_table.heading("f4", text="From")
tt_table.heading("t4", text="To")
tt_table.heading("p5", text="Period-5")
tt_table.heading("f5", text="From")
tt_table.heading("t5", text="To")
tt_table.heading("p6", text="Period-6")
tt_table.heading("f6", text="From")
tt_table.heading("t6", text="To")
tt_table["show"] = "headings"
tt_table.column("date", width=100)
tt_table.column("day", width=100)
tt_table.column("class", width=80)
tt_table.column("section", width=80)
tt_table.column("p1", width=140)
tt_table.column("f1", width=90)
tt_table.column("t1", width=90)
tt_table.column("p2", width=140)
tt_table.column("f2", width=90)
tt_table.column("t2", width=90)
tt_table.column("p3", width=140)
tt_table.column("f3", width=90)
tt_table.column("t3", width=90)
tt_table.column("p4", width=140)
tt_table.column("f4", width=90)
tt_table.column("t4", width=90)
tt_table.column("p5", width=140)
tt_table.column("f5", width=90)
tt_table.column("t5", width=90)
tt_table.column("p6", width=140)
tt_table.column("f6", width=90)
tt_table.column("t6", width=90)
tt_table.pack(fill=BOTH, expand=1)
fetch_data()
tt_table.bind("<ButtonRelease-1>", get_cursor)

root.mainloop()
