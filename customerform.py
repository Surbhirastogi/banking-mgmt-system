from tkinter import*
from tkcalendar import*
from tkinter import messagebox
import pymysql
import math
import random
top2=Tk()
top2.configure(background="skyblue")
top2.geometry("900x700")
top2.title("customer form")

def back():
    top2.destroy()
    import employeepanel

def submitcustomer():
    n=en1.get()
    d=en2.get()
    m=en3.get()
    g=var.get()
    a=en5.get()
    e=en6.get()
    p=en7.get()
    adh=en8.get()
    pan=en9.get()

    st="1234567890"
    l=len(st)
    acc=""
    for i in range(6):
        acc=acc+st[math.floor(random.random()*l)]
        
    
    con=pymysql.Connection(user="root",password="",host="localhost",port=3306,database="banking mgmt")
    cur=con.cursor()
    cur.execute("insert into addcustomer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(acc,n,d,m,g,a,e,p,adh,pan))
    con.commit()
    print("data inserted")
    messagebox.showinfo("alert","customer added")

var=StringVar()

def updatecustomer():
    n=en1.get()
    d=en2.get()
    m=en3.get()
    g=var.get()
    a=en5.get()
    e=en6.get()
    p=en7.get()
    adh=en8.get()
    pan=en9.get()
    
    con=pymysql.Connection(user="root",password="",host="localhost",port=3306,database="banking mgmt")
    cur=con.cursor()
    cur.execute("update addcustomer set cusdob=%s,cusaddress=%s,cusemail=%s,cusphoneno=%s,cusadharno=%s,cuspanno=%s where cusname=%s",(d,a,e,p,adh,pan,n))
    con.commit()
    print("data updated")
    messagebox.showinfo("alert","customer updated")

var=StringVar()


    

lb=Label(text="customer search form",width=55,font=2,bg="black",fg="white",borderwidth=12,relief="sunken")
lb.place(x=190,y=30)    
lb1=Label(text="Name",width=11,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
lb1.place(x=35,y=110)
en1=Entry(width=50,font=2,borderwidth=5,relief="sunken")
en1.place(x=200,y=110) 
lb2=Label(text="D.O.B",width=11,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
lb2.place(x=35,y=160)
en2=DateEntry(width=50,font=2,borderwidth=5,relief="sunken")
en2.place(x=200,y=160) 
lb3=Label(text="mother/father name",width=15,font=2,bg="pink",fg="black",borderwidth=6,relief="groove")
lb3.place(x=35,y=210)
en3=Entry(width=50,font=2,borderwidth=5,relief="sunken")
en3.place(x=200,y=210) 
lb4=Label(text="gender",width=11,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
lb4.place(x=35,y=270)
r=Radiobutton(text="Female",variable=var,value="Female",width=11,font=2)
r.place(x=240,y=270)
r1=Radiobutton(text="Male",variable=var,value="Male",width=11,font=2)
r1.place(x=450,y=270)
lb5=Label(text="address",width=11,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
lb5.place(x=35,y=320)
en5=Entry(width=50,font=2,borderwidth=5,relief="sunken")
en5.place(x=200,y=320) 

lb6=Label(text="e-mail",width=11,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
lb6.place(x=35,y=370)
en6=Entry(width=50,font=2,borderwidth=5,relief="sunken")
en6.place(x=200,y=370)
lb7=Label(text="phone no.",width=11,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
lb7.place(x=35,y=420)
en7=Entry(width=50,font=2,borderwidth=5,relief="sunken")
en7.place(x=200,y=420)

lb8=Label(text="adhar no.",width=11,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
lb8.place(x=35,y=470)
en8=Entry(width=50,font=2,borderwidth=5,relief="sunken")
en8.place(x=200,y=470)
lb9=Label(text="PAN No.",width=11,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
lb9.place(x=35,y=520)
en9=Entry(width=50,font=2,borderwidth=5,relief="sunken")
en9.place(x=200,y=520)



btn1=Button(text="submit",command=submitcustomer,width=15,font=2,bg="pink",fg="black")
btn1.place(x=150,y=630)
btn2=Button(text="back",command=back,width=15,font=2,bg="pink",fg="black")
btn2.place(x=350,y=630)
btn2=Button(text="update",command=updatecustomer,width=15,font=2,bg="pink",fg="black")
btn2.place(x=550,y=630)



top2.mainloop()
