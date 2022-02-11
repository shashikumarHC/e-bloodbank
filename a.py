from tkinter import*
from tkinter import font
from PIL import Image,ImageTk
import mysql.connector as my
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from  datetime import date
import re
email=re.compile("(\d||[a-z])+@[a-z]{,5}\.[a-z]{,6}",re.I)
phone=re.compile("\+?(\d{2})?\s{,3}\d{10}")
blood=re.compile("a\+|a-|b\+|b-|ab\+|ab-|o\+|o-",re.I)
password=re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*\D)[a-zA-Z\d\D]{6,}$")
# database connection
db=my.connect(
    host="localhost",
    user="root",
    passwd="shashi11acharya",
    database="mini"
)
mycursor=db.cursor()
a2root =Tk()
a2root.title("BLOODBANK")
a2root.geometry("2000x2000")
def admin_login():
    global broot,be1,be2
    broot=tk.Toplevel()
    broot.title("L O G I N")
    broot.geometry("550x500")

    j=0
    r=0
    for i in range(100):
        c=str(222222+r)
        Frame(broot,width=10,height=500,bg='#'+c).place(x=j,y=0)
        j=j+10
        r=r+1
    Frame(broot,width=240,height=400,bg='grey').place(x=110,y=80)
    Frame(broot,width=260,height=400,bg='white').place(x=140,y=50)

    #label 1
    bl1=Label(broot,text="LOGIN-ID",bg='white')
    bl=('consoles',13)
    bl1.config(font=1)
    bl1.place(x=170,y=195)

    be1=Entry(broot,width=20,border=0)
    e1=('consoles')
    be1.config(font=1)
    be1.place(x=176,y=230)

    #label 2
    bl2=Label(broot,text="PASSWORD",bg='white')
    bl=('consoles',13)
    bl2.config(font=1)
    bl2.place(x=170,y=280)

    be2=Entry(broot,width=20,border=0,show="*")
    be2.config(font=1)
    be2.place(x=176,y=310)

    Frame(broot,width=200,height=2,bg="#141414").place(x=174,y=255)
    Frame(broot,width=200,height=2,bg="#141414").place(x=174,y=335)

    load=Image.open('icon.png')
    render=ImageTk.PhotoImage(load)
    img=tk.Label(broot,image=render)
    img.place(x=200,y=70)
    btn1=Button(broot,text="LOGIN ",width="8",height=1,font=("arial bold",15),command=cmd1,bg="black",fg="white")
    btn1.place(x=215,y=375)

    broot.mainloop()
def details(a):
    deroot =Tk()
    deroot.title("BLOODBANK")
    deroot.geometry("700x700")
    deroot.configure(bg="dark turquoise")
    Frame(deroot,width=500,height=500,bg='azure').place(x=100,y=100)

    lab1=Label(deroot,text="MY DETAILS",font=("arial bold",30),bg="azure",fg="black")
    lab1.place(x=220,y=120)

    lab2=Label(deroot,text="MOBILE NUMBER",font=("arial bold",14),bg="azure",fg="black")
    lab2.place(x=140,y=200)
    ent1=Entry(deroot,width=40,font=("arial bold",12))
    ent1.place(x=140,y=235)

    lab3=Label(deroot,text="EMAIL ADDRESS",font=("arial bold",14),bg="azure",fg="black")
    lab3.place(x=140,y=270)
    ent2=Entry(deroot,width=40,font=("arial bold",12))
    ent2.place(x=140,y=305)

    lab4=Label(deroot,text="ADDRESS",font=("arial bold",14),bg="azure",fg="black")
    lab4.place(x=140,y=335)
    ent3=Entry(deroot,width=40,font=("arial bold",12))
    ent3.place(x=140,y=370)
    def add_details():
        b=ent1.get()
        c=ent2.get()
        d=ent3.get()
        if b=='' or c=='' or d=='':
            messagebox.showinfo("blood bank","please fill all the values")
            details(a)
        else:
            mycursor.execute("update employee set address=%s,emailid=%s,phone=%s where employee_id=%s",(d,c,b,a))
            db.commit()
            messagebox.showinfo("blood bank","Details added successfully\n please login again to continue your work")
    btn=Button(deroot,text="UPDATE INFORMATION",width="20",font=("arial bold",20),bg="black",fg="white",command=add_details)
    btn.place(x=150,y=450)
    deroot.mainloop()
def cmd1():
    a=be1.get()
    b=be2.get()
    mycursor.execute("select ename from login where loginid=%s and password=%s",(a,b))
    c=mycursor.fetchall()
    if len(c)!=0:
        messagebox.showinfo("blood bank","welcome "+c[0][0])
        mycursor.execute("select address from employee where employee_id=%s ",(a,))
        b=mycursor.fetchone()
        if b[0]==None:
            details(a)
        else:
            if 'a' in a:
                admin()
            elif 'l' in a:
                lab()
            elif 's' in a:
                stk_a()
    else:
        messagebox.showinfo("blood bank","Incorect Credentials")
def add_stk():
    l=stke1.get()
    m=stke2.get()
    if l=='' or m=='':
        messagebox.showinfo("Blood Bank","PLEASE ENTER VALUES")
    elif int(l)>8 or int(l)<0:
        messagebox.showinfo("Blood Bank","PLEASE ENTER VALID STKID") 
    else:
        try:
            int(m)
            n=date.today()
            mycursor.execute("insert into stk_collection values (%s,%s,%s)",(l,m,n))
            db.commit()
            mycursor.execute("update stock set stk=stk+%s where stkid=%s",(m,l))
            db.commit()
            messagebox.showinfo("Blood Bank","Stock updated")
        except:
           messagebox.showinfo("Blood Bank","PLEASE ENTER VALID STK VALUE") 
def stk_a():
    global stke1,stke2
    stkroot =Tk()
    stkroot.title("BLOODBANK")
    stkroot.geometry("700x700")
    stkroot.configure(bg="dark turquoise")
    Frame(stkroot,width=500,height=500,bg='azure').place(x=100,y=100)

    lab1=Label(stkroot,text="STOCK DETAILS",font=("arial bold",30),bg="azure",fg="black")
    lab1.place(x=220,y=120)

    lab2=Label(stkroot,text="STOCK NUMBER",font=("arial bold",14),bg="azure",fg="black")
    lab2.place(x=140,y=220)
    stke1=Entry(stkroot,width=40,font=("arial bold",12))
    stke1.place(x=140,y=255)
    lab3=Label(stkroot,text="QUANTITY",font=("arial bold",14),bg="azure",fg="black")
    lab3.place(x=140,y=320)
    stke2=Entry(stkroot,width=40,font=("arial bold",12))
    stke2.place(x=140,y=355)
    b=Button(stkroot,text="ADD STOCK",width="20",font=("arial bold",20),bg="black",fg="white",command=add_stk)
    b.place(x=150,y=450)
    stkroot.mainloop()
def approve():
    a=l_id.get()
    if a=='':
        messagebox.showinfo("Blood Bank","ENTER VALID ID")
        lab()
    else:
        mycursor.execute("UPDATE doner SET status='approved' where dno=%s"%a)
        db.commit()
        messagebox.showinfo("Blood Bank","DATA ADDED")
        lab()
def reject():
    a=l_id.get()
    if a=='':
        messagebox.showinfo("Blood Bank","ENTER VALID ID")
        lab()
    else:
        mycursor.execute("UPDATE doner SET status='discarded' where dno=%s"%a)
        db.commit()
        messagebox.showinfo("Blood Bank","DATA ADDED")
        lab()
def lab():
    global l_id,labroot
    labroot=Tk()
    labroot.geometry("2000x2000")
    labroot.configure(bg="lightblue")
    # table styling
    style=ttk.Style(labroot)
    style.theme_use("clam")
    style.configure("Treeview",background="lightgray",forground="white",fieldbackground="silver",rowheight=40,font=("times new roman",13,"bold"))
    style.configure("Treeview.Heading",background="lightgray",forground="white",fieldbackground="silver",rowheight=40,font=("times new roman",20,"bold"))
    style.map('Treeview',background=[('selected','gray')])
    style.map('Treeview.Heading',background="gray")
    l_heading=Label(labroot,text="Laboratory",font = ("times new roman",30,"bold"),bg="white", fg="black").place(x=650,y=20)
    lname = Label(labroot, text="UserId",font = ("times new roman",20,"bold"),bg="white", fg="black").place(x=400,y=100)
    l_id = Entry(labroot,font=("times new roman",20,"bold"))
    l_id.place(x=550,y=100,width=250)
    btn1=Button(labroot,text="Approve",width="8",height=1,font=("arial bold",15),bg="black",fg="white",command=approve)
    btn1.place(x=850,y=100)
    btn1=Button(labroot,text="Reject",width="8",height=1,font=("arial bold",15),bg="black",fg="white",command=reject)
    btn1.place(x=1000,y=100)
    # retrival query
    mycursor.execute('select dno,name,age,contactnumber,bloodgroup from doner where status="pending"')
    data=mycursor.fetchall()
    frm=Frame(labroot)
    frm.pack(padx=100,pady=200)
    # table creation
    tree=ttk.Treeview(frm,columns=(1,2,3,4,5),show="headings",height=30)
    tree.heading(1,text="UserId",anchor=CENTER)
    tree.heading(2,text="Name",anchor=CENTER)
    tree.heading(3,text="Age",anchor=CENTER)
    tree.heading(4,text="Phone",anchor=CENTER)
    tree.heading(5,text="Group",anchor=CENTER)
    for i in data:
        tree.insert("",'end',values=i)
    tree.pack()
    labroot.mainloop()
def admin():
    droot=Tk()
    droot.title("A D M I N")
    droot.geometry("2000x2000")
    droot.configure(bg="lightblue")
    dl0=Label(droot,text="BLOOD BANK",bg='white')
    dl=('consoles',13)
    dl0.config(font=("arial bold",30))
    dl0.place(x=600,y=50)
    mycursor.execute("select count(name) from doner where status='approved'")
    a=mycursor.fetchone()
    Frame(droot,width=300,height=100,bg='white').place(x=950,y=120)
    dl1=Label(droot,text="Number Of Approved Donor",bg='white')
    dl=('consoles',13)
    dl1.config(font=("arial bold",15))
    dl1.place(x=970,y=130)
    dl2=Label(droot,text=a[0],bg='white')
    dl=('consoles',13)
    dl2.config(font=("arial bold",15))
    dl2.place(x=1100,y=170)

    mycursor.execute("select SUM(quantity) from seekers where given!='null' and sdate=%s",(date.today(),))
    a=mycursor.fetchone()
    Frame(droot,width=300,height=100,bg='white').place(x=580,y=120)
    dl1=Label(droot,text="Todays given stock",bg='white')
    dl=('consoles',13)
    dl1.config(font=("arial bold",15))
    dl1.place(x=640,y=130)
    dl2=Label(droot,text=a[0],bg='white')
    dl=('consoles',13)
    dl2.config(font=("arial bold",15))
    dl2.place(x=700,y=170)

    mycursor.execute('delete from seekers where given="null" and sdate!=%s',(date.today(),))
    db.commit()
    mycursor.execute("select SUM(quantity) from seekers where given='null'")
    a=mycursor.fetchone()
    Frame(droot,width=300,height=100,bg='white').place(x=200,y=120)
    dl1=Label(droot,text="Requried Blood",bg='white')
    dl=('consoles',13)
    dl1.config(font=("arial bold",15))
    dl1.place(x=270,y=130)
    dl2=Label(droot,text=a[0],bg='white')
    dl=('consoles',13)
    dl2.config(font=("arial bold",15))
    dl2.place(x=330,y=170)
    style=ttk.Style(droot)
    style.theme_use("clam")
    style.configure("Treeview",background="lightgray",forground="white",fieldbackground="silver",rowheight=40,font=("times new roman",13,"bold"))
    style.configure("Treeview.Heading",background="lightgray",forground="white",fieldbackground="silver",rowheight=40,font=("times new roman",20,"bold"))
    style.map('Treeview',background=[('selected','gray')])
    style.map('Treeview.Heading',background="gray")
    mycursor.execute('select * from stock')
    data=mycursor.fetchall()
    frm=Frame(droot)
    frm.pack(padx=100,pady=230)
    tree=ttk.Treeview(frm,columns=(1,2,3),show="headings",height=8)
    tree.heading(1,text="StockId",anchor=CENTER)
    tree.heading(2,text="Blood",anchor=CENTER)
    tree.heading(3,text="Stock",anchor=CENTER)
    for i in data:
        tree.insert("",'end',values=i)
    tree.pack()
    dbtn1=Button(droot,text="Add User",height=1,font=("arial bold",20),bg="black",fg="white",command=add_user)
    dbtn1.place(x=100,y=700)
    dbtn2=Button(droot,text="View Donor's",height=1,font=("arial bold",20),bg="black",fg="white",command=view)
    dbtn2.place(x=600,y=700)
    dbtn3=Button(droot,text="View Seeker's",height=1,font=("arial bold",20),bg="black",fg="white",command=seekers)
    dbtn3.place(x=1200,y=700)
    droot.mainloop()

def view():
    vroot=Tk()
    vroot.title("D O N E R S")
    vroot.configure(bg="lightblue")
    vl=Label(vroot,text="ACTIVE DONOR",bg='white')
    vl.config(font=("arial bold",30))
    vl.place(x=450,y=100)
    style=ttk.Style(vroot)
    style.theme_use("clam")
    style.configure("Treeview",background="lightgray",forground="white",fieldbackground="silver",rowheight=40,font=("times new roman",13,"bold"))
    style.configure("Treeview.Heading",background="lightgray",forground="white",fieldbackground="silver",rowheight=40,font=("times new roman",20,"bold"))
    style.map('Treeview',background=[('selected','gray')])
    style.map('Treeview.Heading',background="gray")
    mycursor.execute('select dno,name,age,contactnumber,bloodgroup from doner where status="approved"')
    data=mycursor.fetchall()
    frm=Frame(vroot)
    frm.pack(padx=100,pady=200)
    # table creation
    tree=ttk.Treeview(frm,columns=(1,2,3,4,5),show="headings")
    tree.heading(1,text="UserId",anchor=CENTER)
    tree.heading(2,text="Name",anchor=CENTER)
    tree.heading(3,text="Age",anchor=CENTER)
    tree.heading(4,text="Phone",anchor=CENTER)
    tree.heading(5,text="Group",anchor=CENTER)
    for i in data:
        tree.insert("",'end',values=i)
    tree.pack()
    vroot.mainloop()
def db_adduser():
    a=ue1.get()
    b=ue2.get()
    c=ue3.get()
    try:
        if a=='' or b=='' or c=='':
            messagebox.showinfo("blood bank","PLEASE FILL ALL THE VALUES")
            admin()
        else:
            mycursor.execute("insert into login values(%s,%s,%s)",(a,c,b))
            db.commit()
            mycursor.execute("insert into employee (employee_id,ename) values (%s,%s)",(a,b))
            db.commit()
            messagebox.showinfo("BLOOD BANK","USER ADDED!....")
            admin()
    except:
            messagebox.showinfo("BLOOD BANK","ENTER VALID VALUES!....")
            admin()
def add_user():
    global uroot,ue1,ue2,ue3
    uroot=Tk()
   # uroot.geometry("1000x1000")
    uroot.configure(bg="lightblue")
    uroot.title("U S E R S D E T A I L")
    ul=Label(uroot,text="ADD USER",bg='white')
    ul.config(font=("arial bold",30))
    ul.place(x=500,y=40)
    ul1=Label(uroot,text="LoginId",bg='white')
    ul1.config(font=("arial bold",15))
    ul1.place(x=150,y=120)
    ue1=Entry(uroot,width=20,border=0,font=("times new roman",15))
    ue1.place(x=150,y=160)
    ul2=Label(uroot,text="User Name",bg='white')
    ul2.config(font=("arial bold",15))
    ul2.place(x=430,y=120)
    ue2=Entry(uroot,width=20,border=0,font=("times new roman",15))
    ue2.place(x=430,y=160)
    ul3=Label(uroot,text="Password",bg='white')
    ul3.config(font=("arial bold",15))
    ul3.place(x=710,y=120)
    ue3=Entry(uroot,width=20,border=0,font=("times new roman",15))
    ue3.place(x=710,y=160)
    ubtn3=Button(uroot,text="ADD",height=1,font=("arial bold",15),bg="black",fg="white",command=db_adduser)
    ul4=Label(uroot,text="MAIN USERS",bg='white')
    ul4.config(font=("arial bold",20))
    ul4.place(x=515,y=200)
    ubtn3.place(x=1000,y=140)
    style=ttk.Style(uroot)
    style.theme_use("clam")
    style.configure("Treeview",background="lightgray",forground="white",fieldbackground="silver",rowheight=40,font=("times new roman",13,"bold"))
    style.configure("Treeview.Heading",background="lightgray",forground="white",fieldbackground="silver",rowheight=40,font=("times new roman",20,"bold"))
    style.map('Treeview',background=[('selected','gray')])
    style.map('Treeview.Heading',background="gray")
    mycursor.execute('select * from employee')
    data=mycursor.fetchall()
    frm=Frame(uroot)
    frm.pack(padx=100,pady=250)
    # table creation
    tree=ttk.Treeview(frm,columns=(1,2,3,4,5),show="headings")
    tree.heading(1,text="EmployeeId",anchor=CENTER)
    tree.heading(2,text="Name",anchor=CENTER)
    tree.heading(3,text="Address",anchor=CENTER)
    tree.heading(4,text="Email",anchor=CENTER)
    tree.heading(5,text="Phone",anchor=CENTER)
    for i in data:
        tree.insert("",'end',values=i)
    tree.pack()
    ubtn4=Button(uroot,text="REMOVE USER",height=1,font=("arial bold",20),bg="black",fg="white",command=del_user)
    ubtn4.place(x=950,y=640)
    uroot.mainloop()
def del_user():
    global delroot,due2
    delroot=Tk()
    delroot.configure(bg="lightblue")
    delroot.geometry("400x400")
    dul2=Label(delroot,text="Employee id",bg='white')
    dul2.config(font=("arial bold",15))
    dul2.place(x=100,y=120)
    due2=Entry(delroot,width=20,border=0,font=("times new roman",15))
    due2.place(x=100,y=160)
    dubtn4=Button(delroot,text="REMOVE",height=1,font=("arial bold",15),bg="black",fg="white",command=delete)
    dubtn4.place(x=100,y=200)
    delroot.mainloop()
def delete():
    a=due2.get()
    mycursor.execute("delete from login where loginid=%s",(a,))
    db.commit()
    mycursor.execute("delete from employee where employee_id=%s",(a,))
    db.commit()
    messagebox.showinfo("BLOOD BANK","User Deleted")
    admin()
def seekers():
    s1root=Tk()
    s1root.configure(bg="lightblue")
    mycursor.execute('select name,phone,requested,given,quantity from seekers where given!="null" order by sdate desc')
    data=mycursor.fetchall()
    style=ttk.Style(s1root)
    style.theme_use("clam")
    style.configure("Treeview",background="lightgray",forground="white",fieldbackground="silver",rowheight=40,font=("times new roman",13,"bold"))
    style.configure("Treeview.Heading",background="lightgray",forground="white",fieldbackground="silver",rowheight=40,font=("times new roman",20,"bold"))
    style.map('Treeview',background=[('selected','gray')])
    style.map('Treeview.Heading',background="gray")
    frm=Frame(s1root)
    frm.pack(padx=100,pady=100)
    tree=ttk.Treeview(frm,columns=(1,2,3,4,5),show="headings",height=3)
    tree.heading(1,text="Name",anchor=CENTER)
    tree.heading(2,text="Phone",anchor=CENTER)
    tree.heading(3,text="requested",anchor=CENTER)
    tree.heading(4,text="given",anchor=CENTER)
    tree.heading(5,text="quantity",anchor=CENTER)
    for i in data:
        tree.insert("",'end',values=i)
    tree.pack()
    mycursor.execute('select name,phone,requested,given,quantity from seekers where given="null"')
    data1=mycursor.fetchall()
    sl2=Label(s1root,text="Requried Blood",bg='white')
    sl2.config(font=("arial bold",25))
    sl2.place(x=480,y=400)
    sl1=Label(s1root,text="Given Blood",bg='white')
    sl1.config(font=("arial bold",25))
    sl1.place(x=500,y=33)
    frm1=Frame(s1root)
    frm1.pack(padx=100,pady=100)
    tree=ttk.Treeview(frm1,columns=(1,2,3,4,5),show="headings",height=3)
    tree.heading(1,text="Name",anchor=CENTER)
    tree.heading(2,text="Phone",anchor=CENTER)
    tree.heading(3,text="requested",anchor=CENTER)
    tree.heading(4,text="given",anchor=CENTER)
    tree.heading(5,text="quantity",anchor=CENTER)
    for i in data1:
        tree.insert("",'end',values=i)
    tree.pack()
    s1root.mainloop()
def doner():
    global root,a_name,a_address,a_age,a_bgrp,a_mail,a_uname,a_num,a_pass
    root = Tk()
    root.title("DONOR REGISTRATION FORM")
    root.geometry("2000x2000+0+0")
    a2frame=Frame(root,bg="pink")
    a2frame.place(x=400,y=0,height=2000,width=1600) 
    alframe = Frame(root,bg='black')
    alframe.place(x=60,y=80,height=600,width=570)
    a1name = Label(alframe, text="THE NEED",font = ("times new roman",50,"bold"),bg="black", fg="white").place(x=115,y=100)
    a2name = Label(alframe, text="FOR BLOOD",font = ("times new roman",50,"bold"),bg="black", fg="white").place(x=80,y=195)
    a3name = Label(alframe, text="IS ALWAYS",font = ("times new roman",50,"bold"),bg="black", fg="white").place(x=90,y=290)
    a4name = Label(alframe, text="THERE",font = ("times new roman",50,"bold"),bg="black", fg="white").place(x=160,y=385)
    #register frame
    aframe = Frame(root,bg='white')
    aframe.place(x=630,y=80,height=600,width=800)
    atitle = Label(aframe, text="DONOR DETAILS",font = ("times new roman",20,"bold"),bg="white", fg="black").place(x=60,y=30)
    aname = Label(aframe, text="NAME",font = ("times new roman",15,"bold"),bg="white", fg="black").place(x=60,y=100)
    a_name = Entry(aframe,font=("times new roman",15,"bold"),bg="lightpink")
    a_name.place(x=60,y=130,width=250)
    anum = Label(aframe, text="CONTACT NUMBER",font = ("times new roman",15,"bold"),bg="white", fg="black").place(x=435,y=100)
    a_num = Entry(aframe,font=("times new roman",15,"bold"),bg="lightpink")
    a_num.place(x=435,y=130,width=250)
    aage = Label(aframe, text="AGE",font = ("times new roman",15,"bold"),bg="white", fg="black").place(x=60,y=170)
    a_age = Entry(aframe,font=("times new roman",15,"bold"),bg="lightpink")
    a_age.place(x=60,y=200,width=250)
    abgrp = Label(aframe, text="BLOOD GROUP",font = ("times new roman",15,"bold"),bg="white", fg="black").place(x=435,y=170)
    a_bgrp = Entry(aframe,font=("times new roman",15,"bold"),bg="lightpink")
    a_bgrp.place(x=435,y=200,width=250)

    aaddress = Label(aframe, text="ADDRESS",font = ("times new roman",15,"bold"),bg="white", fg="black").place(x=60,y=240)
    a_address = Entry(aframe,font=("times new roman",15,"bold"),bg="lightpink")
    a_address.place(x=60,y=270,width=250)
    amail = Label(aframe, text="MAIL ADDRESS",font = ("times new roman",15,"bold"),bg="white", fg="black").place(x=435,y=240)
    a_mail = Entry(aframe,font=("times new roman",15,"bold"),bg="lightpink")
    a_mail.place(x=435,y=270,width=250)
            
    ausername = Label(aframe, text="USER NAME",font = ("times new roman",15,"bold"),bg="white", fg="black").place(x=60,y=310)
    a_uname = Entry(aframe,font=("times new roman",15,"bold"),bg="lightpink")
    a_uname.place(x=60,y=340,width=250)
    abgrp = Label(aframe, text="PASSWORD",font = ("times new roman",15,"bold"),bg="white", fg="black").place(x=435,y=310)
    a_pass = Entry(aframe,font=("times new roman",15,"bold"),bg="lightpink",show="*")
    a_pass.place(x=435,y=340,width=250)
    abtn=Button(root,text="SIGN UP",width="25",font=("arial bold",20),bg="black",fg="white",command=fn)
    abtn.place(x=750,y=500)
    abtn1=Button(root,text="SIGN IN",width="25",font=("arial bold",20),bg="black",fg="white",command=login)
    abtn1.place(x=750,y=570)


    root.mainloop()
def fn():
    try:
        a=a_name.get()
        b=a_age.get()
        c=a_address.get()
        d=a_uname.get()
        e=a_num.get()
        f=a_bgrp.get()
        g=a_mail.get()
        h=a_pass.get()
        #print(a,b,c,d,e,f,g,h)
        if email.search(g)==None:
            messagebox.showinfo("blood bank","enter valid email")
        elif phone.search(e)==None:
            messagebox.showinfo("blood bank","enter valid phone number")
        elif blood.search(f)==None:
            messagebox.showinfo("blood bank","enter valid blood group")
        elif password.search(h)==None:
            messagebox.showinfo("blood bank","weak password\n password must contaion number alpabet and must be more than 6 charector")
        elif int(b) and email.search(g) and phone.search(e) and blood.search(f):
            mycursor.execute("insert into doner (name,age,address,username,contactnumber,bloodgroup,email,password,status) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(a,b,c,d,e,f,g,h,"pending"))
            db.commit()
            messagebox.showinfo("blood bank","Data added")
    except:
        messagebox.showinfo("blood bank","enter valid values")
def login():
        global aroot,ae1,ae2
        aroot=tk.Toplevel()
        aroot.title("L O G I N")
        aroot.geometry("600x600")
        #broot.configure(bg="blue")
        aroot.resizable(0,0)
        j=0
        r=0
        for i in range(100):
                c=str(222222+r)
                Frame(aroot,width=10,height=600,bg='#'+c).place(x=j,y=0)
                j=j+10
                r=r+1
        Frame(aroot,width=400,height=450,bg='grey').place(x=90,y=90)
        Frame(aroot,width=400,height=450,bg='white').place(x=110,y=70)

        #label 1
        al1=Label(aroot,text="USERNAME",bg='white')
        al=('consoles',13)
        al1.config(font=1)
        al1.place(x=170,y=180)

        ae1=Entry(aroot,width=20,border=0)
        a1=('consoles')
        ae1.config(font=1)
        ae1.place(x=176,y=210)

        #label 2
        al2=Label(aroot,text="PASSWORD",bg='white')
        al=('consoles',13)
        al2.config(font=1)
        al2.place(x=170,y=250)

        ae2=Entry(aroot,width=20,border=0,show="*")
        ae2.config(font=1)
        ae2.place(x=176,y=280)

        Frame(aroot,width=255,height=2,bg="#141414").place(x=174,y=238)
        Frame(aroot,width=255,height=2,bg="#141414").place(x=174,y=306)
        load=Image.open('a.png')
        render=ImageTk.PhotoImage(load)
        img=tk.Label(aroot,image=render)
        img.place(x=250,y=70)
        abtn1=Button(aroot,text="LOGIN ",width="8",height=1,font=("arial bold",15),bg="black",fg="white",command=cmd)
        abtn1.place(x=240,y=340)

        al3=Label(aroot,text="NEW DONOR?",bg='white')
        al=('consoles',13)
        al3.config(font=1)
        al3.place(x=225,y=400)

        abtn2=Button(aroot,text="SIGN UP ",width="8",height=1,font=("arial bold",15),bg="black",fg="white",command=aroot.destroy)
        abtn2.place(x=240,y=440)

        aroot.mainloop()
def cmd():
        a=ae1.get()                                                                                                                                                                                                                           
        b=ae2.get()
        mycursor.execute("select name from doner where username=%s and password=%s and status='approved'",(a,b))
        c=mycursor.fetchall()
        if  len(c)!=0:
                messagebox.showinfo("blood bank","hello "+c[0][0])
                donor()
        else:
                mycursor.execute("select name from doner where username=%s and password=%s and status='discarded'",(a,b))
                c=mycursor.fetchall()
                if len(c)!=0:
                        messagebox.showinfo("blood bank","sorry to inform you have blood issue")
                        mycursor.execute("delete from doner where username=%s and password=%s and status='discarded'",(a,b))
                        db.commit()
                else:
                    mycursor.execute("select name from doner where username=%s and password=%s and status='pending'",(a,b))
                    c=mycursor.fetchall()
                    if len(c)!=0:
                        messagebox.showinfo("blood bank","PLEASE WAIT! THE RESULT WILL BE GIVEN SOON")
                    else:
                        messagebox.showinfo("blood bank","enter valid username and password")
def donor():
        dnroot=Tk()
        dnroot.title("D O N O R P A G E")
        dnroot.configure(bg="lightblue")
        dnroot.geometry("2000x2000")
        dn1name = Label(dnroot, text="WELCOME TO BLOOD BANK",font = ("times new roman",30,"bold"),bg="black", fg="white").place(x=450,y=50)
        dn2name = Label(dnroot, text='Now you can donate your blood',font = ("times new roman",25,"bold"),bg="lightblue" ).place(x=520,y=125)
        dn3name = Label(dnroot, text='Things to do after blood donation:',font = ("times new roman",20,"bold"),bg="lightblue" ).place(x=100,y=210)
        dn4name = Label(dnroot, text=r'''1.After donating whole blood, a person often sits and relaxes for about 15 minutesTrusted Source. An attendant may 
        offer water, juice, or snacks to help prevent or address any fatigue or dizziness.''',font = ("times new roman",20,"bold"),bg="lightblue" ).place(x=100,y=250)
        dn5name = Label(dnroot, text='2.When the person feels ready, they can return to most of their usual activities, often within a few hours.',font = ("times new roman",20,"bold"),bg="lightblue" ).place(x=100,y=320)
        dn6name = Label(dnroot, text=r'''3.The blood contains iron, and each donation may cause the body to lose 200–250 milligrams of the mineral.
        Eating iron-rich foods can help replenish levels of the mineral in the blood''',font = ("times new roman",20,"bold"),bg="lightblue" ).place(x=100,y=360)
        dn7name = Label(dnroot, text='4.Donating blood removes fluids from the body. A person can help restore them by drinking water, broth, or herbal tea.',font = ("times new roman",20,"bold"),bg="lightblue" ).place(x=100,y=430)
        dn8name = Label(dnroot, text='Benefits of Blood Donatiton:',font = ("times new roman",20,"bold"),bg="lightblue" ).place(x=100,y=495)
        dn9name = Label(dnroot, text='1.Reduce stress',font = ("times new roman",20,"bold"),bg="lightblue" ).place(x=100,y=535)
        dn10name = Label(dnroot, text='2.Improve your emotional well-being',font = ("times new roman",20,"bold"),bg="lightblue" ).place(x=100,y=575)
        dn11name = Label(dnroot, text='3.Benefit your physical health',font = ("times new roman",20,"bold"),bg="lightblue" ).place(x=100,y=615)
        dn12name = Label(dnroot, text='4.Help get rid of negative feelings',font = ("times new roman",20,"bold"),bg="lightblue" ).place(x=100,y=655)
        dn13name = Label(dnroot, text='5.Provide a sense of belonging and reduce isolation',font = ("times new roman",20,"bold"),bg="lightblue" ).place(x=100,y=695)
        dn14name = Label(dnroot, text='Free health check up:',font = ("times new roman",20,"bold"),bg="lightblue" ).place(x=900,y=495)
        dn15name = Label(dnroot, text='1.Pulse',font = ("times new roman",20,"bold"),bg="lightblue" ).place(x=900,y=535)
        dn16name = Label(dnroot, text='2.Blood pressure',font = ("times new roman",20,"bold"),bg="lightblue" ).place(x=900,y=575)
        dn17name = Label(dnroot, text='3.Body temperature',font = ("times new roman",20,"bold"),bg="lightblue" ).place(x=900,y=615)
        dn18name = Label(dnroot, text='4.Hemoglobin levels',font = ("times new roman",20,"bold"),bg="lightblue" ).place(x=900,y=655)
        dnroot.mainloop()
def distubution(c,d):
    op=[1,5]
    on=[5]
    ap=[3,1,7,5]
    an=[7,5]
    bp=[4,1,8,5]
    bn=[8,5]
    abp=[2,1,3,4,6,5,7,8]
    abn=[6,5,7,8]
    if c=="O+":
        for i in op:
            mycursor.execute("select blood from stock where stkid=%s and stk >= %s",(i,d))
            a=mycursor.fetchone()
            if a!=None:
                 mycursor.execute("update stock set stk=stk-%s where stkid=%s",(d,i))
                 db.commit()
                 return a[0]
        else:
            return "null"
    elif c=="O-":
        for i in on:
            mycursor.execute("select blood from stock where stkid=%s and stk >= %s",(i,d))
            a=mycursor.fetchone()
            if a!=None:
                 mycursor.execute("update stock set stk=stk-%s where stkid=%s",(d,i))
                 db.commit()
                 return a[0]
        else:
            return "null"
    elif c=="A+":
        for i in ap:
            mycursor.execute("select blood from stock where stkid=%s and stk >= %s",(i,d))
            a=mycursor.fetchone()
            if a!=None:
                 mycursor.execute("update stock set stk=stk-%s where stkid=%s",(d,i))
                 db.commit()
                 return a[0]
        else:
            return "null"
    elif c=="A-":
        for i in an:
            mycursor.execute("select blood from stock where stkid=%s and stk >= %s",(i,d))
            a=mycursor.fetchone()
            if a!=None:
                 mycursor.execute("update stock set stk=stk-%s where stkid=%s",(d,i))
                 db.commit()
                 return a[0]
        else:
            return "null"
    elif c=="B+":
        for i in bp:
            mycursor.execute("select blood from stock where stkid=%s and stk >= %s",(i,d))
            a=mycursor.fetchone()
            if a!=None:
                 mycursor.execute("update stock set stk=stk-%s where stkid=%s",(d,i))
                 db.commit()
                 return a[0]
        else:
            return "null"
    elif c=="B-":
        for i in bn:
            mycursor.execute("select blood from stock where stkid=%s and stk >= %s",(i,d))
            a=mycursor.fetchone()
            if a!=None:
                 mycursor.execute("update stock set stk=stk-%s where stkid=%s",(d,i))
                 db.commit()
                 return a[0]
        else:
            return "null"
    elif c=="AB+":
        for i in abp:
            mycursor.execute("select blood from stock where stkid=%s and stk >= %s",(i,d))
            a=mycursor.fetchone()
            if a!=None:
                 mycursor.execute("update stock set stk=stk-%s where stkid=%s",(d,i))
                 db.commit()
                 return a[0]
        else:
            return "null"
    elif c=="AB-":
        for i in abn:
            mycursor.execute("select blood from stock where stkid=%s and stk >= %s",(i,d))
            a=mycursor.fetchone()
            if a!=None:
                 mycursor.execute("update stock set stk=stk-%s where stkid=%s",(d,i))
                 db.commit()
                 return a[0]
        else:
            return "null"
def seeker():
    try:
        a=se1.get()
        b=se2.get()
        c=se3.get().upper()
        d=se4.get()
        e=date.today()
        stk=distubution(c,d)
        if phone.search(b)==None:
            messagebox.showinfo("BLOOD BANK","enter valid phone number")
        if blood.search(c)==None:
            messagebox.showinfo("BLOOD BANK","enter valid blood group")
        elif phone.search(b) and blood.search(c) and int(d):
            if stk=="null":
                messagebox.showinfo("BLOOD BANK","Sorry blood is not available")
            else:
                    messagebox.showinfo("BLOOD BANK","Blood is available, You can collect it from the bank")
            mycursor.execute("insert into seekers (name,phone,requested,quantity,sdate,given) values(%s,%s,%s,%s,%s,%s)",(a,b,c,d,e,stk))
            db.commit()
        else:
            messagebox.showinfo("BLOOD BANK","enter valid values")
    except:
        messagebox.showinfo("BLOOD BANK","PLEASE FILL ALL THE DETAILS")
def seekers_a():
    global sroot,se1,se2,click1,click2,se3,se4
    sroot=Tk()
    sroot.geometry("2000x2000")
    sroot.configure(bg="lightblue")
    sroot.title("S E E K E R D E T A I L S")
    sl=Label(sroot,text="ADD YOUR DETAILS",bg='white')
    sl.config(font=("arial bold",30))
    sl.place(x=600,y=40)
    sl1=Label(sroot,text="Name",bg='white')
    sl1.config(font=("arial bold",15))
    sl1.place(x=150,y=120)
    se1=Entry(sroot,width=20,border=0,font=("times new roman",15))
    se1.place(x=150,y=160)
    sl2=Label(sroot,text="Phone",bg='white')
    sl2.config(font=("arial bold",15))
    sl2.place(x=430,y=120)
    se2=Entry(sroot,width=20,border=0,font=("times new roman",15))
    se2.place(x=430,y=160)
    sl3=Label(sroot,text="Blood group",bg='white')
    sl3.config(font=("arial bold",15))
    sl3.place(x=710,y=120)
    se3=Entry(sroot,width=20,border=0,font=("times new roman",15))
    se3.place(x=710,y=160)
    # click1=StringVar()
    # drop1=OptionMenu(sroot,click1,"O+","AB+","A+","B+","O-","AB-","A-","B-")
    # drop1.pack()
    sl4=Label(sroot,text="Quantity",bg='white')
    sl4.config(font=("arial bold",15))
    sl4.place(x=990,y=120)
    se4=Entry(sroot,width=20,border=0,font=("times new roman",15))
    se4.place(x=990,y=160)
    # click2=StringVar()
    # drop2=OptionMenu(sroot,click2,1,2,3,4,5,6,7,8,9,10)
    # drop2.place(x=990,y=160)
    sbtn3=Button(sroot,text="REQUEST",height=1,font=("arial bold",15),bg="black",fg="white",command=seeker)
    sbtn3.place(x=1300,y=135)
    style=ttk.Style(sroot)
    style.theme_use("clam")
    style.configure("Treeview",background="lightgray",forground="white",fieldbackground="silver",rowheight=40,font=("times new roman",13,"bold"))
    style.configure("Treeview.Heading",background="lightgray",forground="white",fieldbackground="silver",rowheight=40,font=("times new roman",20,"bold"))
    style.map('Treeview',background=[('selected','gray')])
    style.map('Treeview.Heading',background="gray")
    mycursor.execute('select * from stock')
    data=mycursor.fetchall()
    frm=Frame(sroot)
    frm.pack(padx=100,pady=230)
    tree=ttk.Treeview(frm,columns=(1,2,3),show="headings",height=8)
    tree.heading(1,text="StockId",anchor=CENTER)
    tree.heading(2,text="Blood",anchor=CENTER)
    tree.heading(3,text="Stock",anchor=CENTER)
    for i in data:
        tree.insert("",'end',values=i)
    tree.pack()
    sroot.mainloop()
a2root.configure(bg="red4")
lab1=Label(a2root,text="WELCOME TO BLOOD BANK",font=("arial bold",65),fg="white",bg="red4")
lab1.place(x=150,y=50)

lab2=Label(a2root,text="The blood you donate gives someone \n another chance of life ",font=("arial bold",30),fg="white",bg="red4")
lab2.place(x=150,y=200)

lab2=Label(a2root,text="GIVE THE GIFT OF LIFE",font=("arial",55),fg="white",bg="red4")
lab2.place(x=80,y=350)

lab2=Label(a2root,text="DONATE BLOOD",font=("arial bold",70),fg="white",bg="red4")
lab2.place(x=120,y=450)

btn=Button(a2root,text="ADMIN/STAFF",width="20",font=("arial bold",20),bg="black",fg="white",command=admin_login)
btn.place(x=1000,y=250)

btn=Button(a2root,text="DONOR",width="20",font=("arial bold",20),bg="black",fg="white",command=doner)
btn.place(x=1000,y=350)

btn=Button(a2root,text="EMERGENCY LOGIN",width="20",font=("arial bold",20),bg="black",fg="white",command=seekers_a)
btn.place(x=1000,y=450)

frm = Frame(a2root,width=2000,height=250,bg="black").place(x=0,y=600)
lab2=Label(frm,text="Address: ABC road,\n near DEF karnataka\n hassan-573201\n head office",font=("arial bold",15),fg="white",bg="black")
lab2.place(x=120,y=670)

lab2=Label(frm,text="Mail Address: abc1990@gmail.com",font=("arial bold",15),fg="white",bg="black")
lab2.place(x=1000,y=670)

lab2=Label(frm,text="Contact Number: 8874513054",font=("arial bold",15),fg="white",bg="black")
lab2.place(x=1000,y=720)


a2root.mainloop()

