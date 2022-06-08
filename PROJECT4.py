from tkinter import *
from tkinter import messagebox,ttk,Tk
import pymysql
import time
def add_attendance():
    condition = dval.get ( )
    if (len ( condition ) != 0):
        con = pymysql.connect ( host="localhost" , user="root" , password="yashdeep1" ,database="schoolmanagementsystem4" )
        mycursor = con.cursor ( )
        mycursor.execute ("insert into attdata values(%s,%s,%s,%s,%s,%s,%s,%s)" ,
                          (dval.get ( ) , daval.get ( ) , cval.get ( ) , sval.get ( ) , tval.get ( ) , pval.get ( ) , aval.get ( ) ,lval.get ( ) ) )
        con.commit ( )
        fetch_data ( )
        clear ( )
        con.close ( )
        messagebox.showinfo ( "Notification" , "Record has been inserted" )
    else:
        messagebox.showerror ( "Error" , "Date cannot be empty" )


def fetch_data():
    con = pymysql.connect ( host="localhost" , user="root" , password="yashdeep1" , database="schoolmanagementsystem4" )
    mycursor = con.cursor ( )
    mycursor.execute ( "select * from attdata" )
    rows = mycursor.fetchall ( )
    if len ( rows ) != 0:
        att_table.delete ( *att_table.get_children ( ) )
        for row in rows:
            att_table.insert ( '' , END , values=row )
        con.commit ( )
    con.close ( )


def clear():
    dval.set ( "" )
    daval.set ( "" )
    cval.set ( "" )
    sval.set ( "" )
    tval.set ( "" )
    pval.set ( "" )
    aval.set ( "" )
    lval.set ( "" )
    
def get_cursor(ev):
    cursor_row = att_table.focus ( )
    content = att_table.item ( cursor_row )
    row = content['values']
    if (len ( row ) != 0):
        dval.set ( row[0] )
        daval.set ( row[1] )
        cval.set ( row[2] )
        sval.set ( row[3] )
        tval.set ( row[4] )
        pval.set ( row[5] )
        aval.set ( row[6] )
        lval.set ( row[7] )

def update_data():
    con = pymysql.connect ( host="localhost" , user="root" , password="yashdeep1" , database="schoolmanagementsystem4" )
    mycursor = con.cursor ( )
    mycursor.execute (
        "update attdata set Day=%s,Class=%s,Section=%s,Total=%s,Present=%s,Absent=%s,Leave_=%s where Date=%s" ,
        (daval.get ( ) ,
         cval.get ( ) ,
         sval.get ( ) ,
         tval.get ( ) ,
         pval.get ( ) ,
         aval.get ( ) ,
         lval.get ( ) ,
         dval.get ( )) )
    con.commit ( )
    fetch_data ( )
    clear ( )
    messagebox.showinfo ( "Notifications" , "Data have been updated" )
    con.close ( )


def delete_data():
    con = pymysql.connect ( host="localhost" , user="root" , password="yashdeep1" , database="schoolmanagementsystem4" )
    mycursor = con.cursor ( )
    mycursor.execute ( "delete from attdata where Date=%s" , dval.get ( ) )
    con.commit ( )
    fetch_data ( )
    clear ( )
    con.close ( )
    messagebox.showinfo ( "Notification" , "The selected data have been deleted" )

def search_data():
    con = pymysql.connect ( host="localhost" , user="root" , password="yashdeep1" , database="schoolmanagementsystem4" )
    mycursor = con.cursor ( )

    mycursor.execute (
        "select * from attdata where " + str ( search_by.get ( ) ) + " LIKE '%" + str ( search_txt.get ( ) ) + "%'" )
    rows = mycursor.fetchall ( )
    if len ( rows ) != 0:
        att_table.delete ( *att_table.get_children ( ) )
        for row in rows:
            att_table.insert ( '' , END , values=row )
        con.commit ( )
    con.close ( )


# ..................................................................................................................................................EXIT BUTTON
def exit_():
    res = messagebox.askyesnocancel ( "Notification" , "Do you want to exit?" )
    if (res == True):
        root.destroy ( )


root = Tk( )
root.title ( "School Management System" )
root.geometry ( "1350x700+0+0" )
root.config ( bg="blue" )
# .....................................................................................
title = Label ( root , text="School Management System" , font=("times new roman" , 40 , "bold") , relief=GROOVE ,
                bd=10 ,bg="yellow" , fg="red" )
title.place ( x=0 , y=0 , relwidth=1 )
# ......................................................................................................................................................VARIABLES
dval = StringVar ( )
daval = StringVar ( )
cval = StringVar ( )
sval = StringVar ( )
tval = StringVar ( )
pval = StringVar ( )
aval = StringVar ( )
lval = StringVar ( )
search_by = StringVar ( )
search_txt = StringVar ( )
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
Manage_Frame = Frame ( root , bd=4 , relief=RIDGE , bg="red" )
Manage_Frame.place ( x=20 , y=100 , width=560 , height=570 )

m_title = Label ( Manage_Frame , text="Manage Attendance" , bg="red" , fg="white" ,
                  font=("times new roman" , 30 , "bold") )
m_title.place ( x=70 , y=9 , width=400 )

lbl_date = Label ( Manage_Frame , text="Date:" , bg="red" , fg="white" , font=("times new roman" , 20 , "bold") ,
                   anchor="w" )
lbl_date.place ( x=10 , y=80 , width=100 )

txt_date = Entry ( Manage_Frame , textvariable=dval , font=("times new roman" , 20 , "bold") , width=10 , bd=5 ,
                   relief=GROOVE )
txt_date.place ( x=100 , y=78 , width=180 )

lbl_day = Label ( Manage_Frame , text="Day:" , bg="red" , fg="white" , font=("times new roman" , 20 , "bold") ,
                  anchor="w" )
lbl_day.place ( x=300 , y=80 , width=80 )

combo_day = ttk.Combobox ( Manage_Frame , textvariable=daval , font=("times new roman" , 19 , "bold") ,
                           state="readonly" )
combo_day["values"] = ("Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "Saturday")
combo_day.place ( x=370 , y=80 , width=170 )

lbl_class = Label ( Manage_Frame , text="Class:" , bg="red" , fg="white" , font=("times new roman" , 20 , "bold") ,
                    anchor="w" )
lbl_class.place ( x=10 , y=140 , width=110 )

combo_class = ttk.Combobox ( Manage_Frame , textvariable=cval , font=("times new roman" , 19 , "bold") ,
                             state="readonly" )
combo_class["values"] = (
    "Nursery" , "Primary" , "1st" , "2nd" , "3rd" , "4th" , "5th" , "6th" , "7th" , "8th" , "9th" , "10th" , "11th" ,
    "12th")
combo_class.place ( x=100 , y=138 , width=180 )

lbl_sec = Label ( Manage_Frame , text="Sec:" , bg="red" , fg="white" , font=("times new roman" , 20 , "bold") ,
                  anchor="w" )
lbl_sec.place ( x=300 , y=140 , width=80 )

combo_Section = ttk.Combobox ( Manage_Frame , textvariable=sval , font=("times new roman" , 19 , "bold") ,
                               state="readonly" )
combo_Section["values"] = ("A" , "B" , "C" , "D")
combo_Section.place ( x=370 , y=140 , width=170 )

lbl_total = Label ( Manage_Frame , text="Total:" , bg="red" , fg="white" , font=("times new roman" , 20 , "bold") ,
                 anchor="w" )
lbl_total.place ( x=10 , y=200 , width=150 )

txt_total = Entry ( Manage_Frame , textvariable=tval , font=("times new roman" , 20 , "bold") , bd=5 , relief=GROOVE )
txt_total.place ( x=150 , y=200 , width=150 )

lbl_present = Label ( Manage_Frame , text="Present:" , bg="red" , fg="white" , font=("times new roman" , 20 , "bold") ,
                 anchor="w" )
lbl_present.place ( x=10 , y=260 , width=150 )

txt_present = Entry ( Manage_Frame , width=10 , textvariable=pval , font=("times new roman" , 20 , "bold") , bd=5 ,
                 relief=GROOVE )
txt_present.place ( x=150 , y=260 , width=150 )

lbl_absent = Label ( Manage_Frame , text="Absent:" , bg="red" , fg="white" , font=("times new roman" , 20 , "bold") ,
                 anchor="w" )
lbl_absent.place ( x=10 , y=320 , width=150 )

txt_absent = Entry ( Manage_Frame , width=10 , textvariable=aval , font=("times new roman" , 20 , "bold") , bd=5 ,
                 relief=GROOVE )
txt_absent.place ( x=150 , y=320 , width=150 )

lbl_Leave = Label ( Manage_Frame , text="Leave:" , bg="red" , fg="white" , font=("times new roman" , 20 , "bold") ,
                 anchor="w" )
lbl_Leave.place ( x=10 , y=380 , width=150 )

txt_Leave = Entry ( Manage_Frame , textvariable=lval , font=("times new roman" , 20 , "bold") , bd=5 , relief=GROOVE )
txt_Leave.place ( x=150 , y=380 , width=150 )
# ....................................................................................................................................BUTTON FRAME

btn_frame = Frame ( Manage_Frame , bd=4 , relief=RIDGE , bg="red" )
btn_frame.place ( x=50 , y=480 , width=470 )

addbtn = Button ( btn_frame , text="ADD" , width=10 , command=add_attendance).grid ( row=0 , column=0 , padx=5 ,pady=10 )
updatebtn = Button ( btn_frame , text="UPDATE" , width=10 , command=update_data ).grid ( row=0 , column=1 , padx=5 ,pady=10 )
deletebtn = Button ( btn_frame , text="DELETE" , width=10 , command=delete_data ).grid ( row=0 , column=2 , padx=5 ,pady=10 )
clearbtn = Button ( btn_frame , text="CLEAR" , width=10 , command=clear ).grid ( row=0 , column=3 , padx=5 , pady=10 )
exitbtn = Button ( btn_frame , text="EXIT" , width=10 , command=exit_ ).grid ( row=0 , column=4 , padx=5 , pady=10 )
# ....................................................................................................................................DETAIL FRAME
Detail_Frame = Frame ( root , bd=4 , relief=RIDGE , bg="red" )
Detail_Frame.place ( x=590 , y=100 , width=740 , height=570 )

lbl_search = Label ( Detail_Frame , text="Search By" , bg="red" , fg="white" , font=("times new roman" , 25 , "bold") )
lbl_search.grid ( row=0 , column=0 , padx=10 , pady=10 , sticky="w" )

combo_search = ttk.Combobox ( Detail_Frame , textvariable=search_by , width=10 ,
                              font=("times new roman" , 19 , "bold") ,
                              state="readonly" )
combo_search["values"] = ("Date" , "Class" , "Section")
combo_search.grid ( row=0 , column=1 , padx=20 , pady=10 )

txt_search = Entry ( Detail_Frame , textvariable=search_txt , width=15 , font=("times new roman" , 12 , "bold") , bd=5 ,
                     relief=GROOVE )
txt_search.grid ( row=0 , column=2 , padx=15 , pady=10 , sticky="w" )

searchbtn = Button ( Detail_Frame , text="SEARCH" , width=10 , command=search_data ).grid ( row=0 , column=3 , padx=10 ,
                                                                                            pady=10 )
showallbtn = Button ( Detail_Frame , text="SHOWALL" , width=10 , command=fetch_data ).grid ( row=0 , column=4 ,
                                                                                             padx=10 , pady=10 )

# .................................................................................................................................................Table Frame
table_frame = Frame ( Detail_Frame , bd=4 , relief=RIDGE , bg="red" )
table_frame.place ( x=10 , y=70 , width=720 , height=475 )

scroll_x = Scrollbar ( table_frame , orient=HORIZONTAL )
scroll_y = Scrollbar ( table_frame , orient=VERTICAL )
att_table = ttk.Treeview ( table_frame , columns=(
    "date" , "day" , "class" , "section" , "total" , "present" , "absent" , "Leave") , xscrollcommand=scroll_x.set , yscrollcommand=scroll_y.set )

style = ttk.Style ( )
style.configure ( "Treeview.Heading" , font=("times" , 15 , "bold") , foreground="blue" )
style.configure ( "Treeview" , font=("times" , 12 , "bold") , foreground="black" )

scroll_x.pack ( side=BOTTOM , fill=X )
scroll_y.pack ( side=RIGHT , fill=Y )
scroll_x.config ( command=att_table.xview )
scroll_y.config ( command=att_table.yview )
att_table.heading ( "date" , text="Date" )
att_table.heading ( "day" , text="Day" )
att_table.heading ( "class" , text="Class" )
att_table.heading ( "section" , text="Section" )
att_table.heading ( "total" , text="Total" )
att_table.heading ( "present" , text="Present" )
att_table.heading ( "absent" , text="Absent" )
att_table.heading ( "Leave" , text="Leave" )
att_table["show"] = "headings"
att_table.column ( "date" , width=100 )
att_table.column ( "day" , width=100 )
att_table.column ( "class" , width=80 )
att_table.column ( "section" , width=80 )
att_table.column ( "total" , width=90 )
att_table.column ( "present" , width=90 )
att_table.column ( "absent" , width=90 )
att_table.column ( "Leave" , width=90 )
att_table.pack ( fill=BOTH , expand=1 )
fetch_data ( )
att_table.bind ( "<ButtonRelease-1>" , get_cursor )

root.mainloop ( )
