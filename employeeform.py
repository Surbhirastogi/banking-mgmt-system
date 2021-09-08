from tkinter import*
from tkcalendar import*
import math
import random
from tkinter import messagebox
import pymysql
top2=Tk()
top2.configure(background="skyblue")
top2.geometry("900x700")
top2.title("employee form")

def back():
    top2.destroy()
    import adminbutton
def submitemployee():
    n=en1.get()
    d=en2.get()
    m=en3.get()
    g=var.get()
    a=en5.get()
    e=en6.get()
    p=en7.get()
    adh=en8.get()
    q=en9.get()
    st="abcdefghijk21345678&#*"
    l=len(st)
    otp=""
    for i in range(5):
        otp=otp+st[math.floor(random.random()*l)]
        
    con=pymysql.Connection(user="root",password="",host="localhost",port=3306,database="banking mgmt")
    cur=con.cursor()
    cur.execute("insert into addemployee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",('',n,d,m,g,a,e,p,adh,q,otp))
    con.commit()
    print("data inserted")
    messagebox.showinfo("alert","employee added")

var=StringVar()
def updateemployee():
    i=en0.get()
    n=en1.get()
    d=en2.get()
    m=en3.get()
    g=var.get()
    a=en5.get()
    e=en6.get()
    p=en7.get()
    adh=en8.get()
    q=en9.get()
    
    con=pymysql.Connection(user="root",password="",host="localhost",port=3306,database="banking mgmt")
    cur=con.cursor()
    cur.execute("update addemployee set empname=%s,empdob=%s,empgender=%s,empaddress=%s,empemail=%s,empphone=%s,empaadhar=%s,empquaification=%s where empid=%s",(n,d,g,a,e,p,adh,q,i))
    con.commit()
    print("data updated")
    messagebox.showinfo("alert","employee updated")

var=StringVar()


def deleteemployee():
       i=en0.get()
       con=pymysql.Connection(user="root",password="",host="localhost",port=3306,database="banking mgmt")
       cur=con.cursor()
       cur.execute("delete from addemployee where empid=%s",(i))
       con.commit()
       print("data deleted")
       messagebox.showinfo("alert","employee deleted")
       
def viewemployee():
    i=en0.get()
    n=en1.get()
    d=en2.get()
    m=en3.get()
    g=var.get()
    a=en5.get()
    e=en6.get()
    p=en7.get()
    adh=en8.get()
    q=en9.get()
    
    con=pymysql.Connection(user="root",password="",host="localhost",port=3306,database="banking mgmt")
    cur=con.cursor()
    cur.execute("select *from addemployee where empid=%s",(i))
    data=cur.fetchall()
    for i in data:
        name.set(i[1])
        dob.set(i[2])
        mfname.set(i[3])
        var.set(i[4])
        address.set(i[5])
        email.set(i[6])
        phone.set(i[7])
        aadhar.set(i[8])
        quali.set(i[9])
        
    con.commit()
    print("employee data displayed")
    messagebox.showinfo("alert","employee fetched")

var=StringVar()

name=StringVar()
dob=StringVar()
mfname=StringVar()
gender=StringVar()
address=StringVar()
email=StringVar()
phone=StringVar()
aadhar=StringVar()
quali=StringVar()
lb=Label(text="empolyee form",width=55,font=2,bg="black",fg="white",borderwidth=12,relief="sunken")
lb.place(x=190,y=30)
lb0=Label(text="Id",width=11,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
lb0.place(x=35,y=110)
en0=Entry(textvariable=id,width=50,font=2,borderwidth=5,relief="sunken")
en0.place(x=200,y=110)
lb1=Label(text="Name",width=11,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
lb1.place(x=35,y=160)
en1=Entry(textvariable=name,width=50,font=2,borderwidth=5,relief="sunken")
en1.place(x=200,y=160) 
lb2=Label(text="D.O.B",width=11,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
lb2.place(x=35,y=210)
en2=DateEntry(textvariable=dob,width=49,font=2,borderwidth=5,relief="sunken")
en2.place(x=200,y=210) 
lb3=Label(text="mother/father name",width=15,font=2,bg="pink",fg="black",borderwidth=6,relief="groove")
lb3.place(x=35,y=270)
en3=Entry(textvariable=mfname,width=50,font=2,borderwidth=5,relief="sunken")
en3.place(x=200,y=270) 
lb4=Label(text="gender",width=11,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
lb4.place(x=35,y=320)
r=Radiobutton(text="Female",variable=var,value="Female",width=11,font=2)
r.place(x=240,y=320)
r1=Radiobutton(text="Male",variable=var,value="Male",width=11,font=2)
r1.place(x=450,y=320)
lb5=Label(text="address",width=11,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
lb5.place(x=35,y=370)
en5=Entry(textvariable=address,width=50,font=2,borderwidth=5,relief="sunken")
en5.place(x=200,y=370) 

lb6=Label(text="e-mail",width=11,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
lb6.place(x=35,y=420)
en6=Entry(textvariable=email,width=50,font=2,borderwidth=5,relief="sunken")
en6.place(x=200,y=420)
lb7=Label(text="phone no.",width=11,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
lb7.place(x=35,y=470)
en7=Entry(textvariable=phone,width=50,font=2,borderwidth=5,relief="sunken")
en7.place(x=200,y=470)

lb8=Label(text="adhar no.",width=11,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
lb8.place(x=35,y=520)
en8=Entry(textvariable=aadhar,width=50,font=2,borderwidth=5,relief="sunken")
en8.place(x=200,y=520)
lb9=Label(text="qualification",width=11,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
lb9.place(x=35,y=570)
en9=Entry(textvariable=quali,width=50,font=2,borderwidth=5,relief="sunken")
en9.place(x=200,y=570)



btn1=Button(text="submit",command=submitemployee,width=15,font=2,bg="pink",fg="black")
btn1.place(x=20,y=630)

btn2=Button(text="Delete",command=deleteemployee,width=15,font=2,bg="pink",fg="black")
btn2.place(x=180,y=630)
btn3=Button(text="update",command=updateemployee,width=15,font=2,bg="pink",fg="black")
btn3.place(x=340,y=630)
btn2=Button(text="view",command=viewemployee,width=15,font=2,bg="pink",fg="black")
btn2.place(x=500,y=630)
btn2=Button(text="back",command=back,width=15,font=2,bg="pink",fg="black")
btn2.place(x=700,y=630)



top2.mainloop()
