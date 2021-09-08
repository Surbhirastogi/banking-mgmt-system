from tkinter import*
from tkinter import messagebox
import pymysql

top2=Tk()
top2.configure(background="skyblue")
top2.geometry("800x800")
top2.title("customer delete and view")

def back():
    top2.destroy()
    import employeepanel

def deletecustomer():
    

   
    acc=en0.get()   
    
    con=pymysql.Connection(user="root",password="",host="localhost",port=3306,database="banking mgmt")
    cur=con.cursor()
    cur.execute("delete from addcustomer where accountno=%s",(acc))
    con.commit()
    print("data deleted")
    messagebox.showinfo("alert","customer deleted")

var=StringVar()

def updatecustomer():
    acc=en0.get()
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
    cur.execute("update addcustomer set cusname=%s,cusdob=%s,cusaddress=%s,cusemail=%s,cusphoneno=%s,cusadharno=%s,cuspanno=%s where accountno=%s",(n,d,a,e,p,adh,pan,acc))
    con.commit()
    print("data updated")
    messagebox.showinfo("alert","customer updated")

var=StringVar()
def viewcustomer():
    acc=en0.get()
    con=pymysql.Connection(user="root",password="",host="localhost",port=3306,database="banking mgmt")
    cur=con.cursor()
    cur.execute("select *from addcustomer where accountno=%s",(acc))
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
        pan.set(i[9])
    messagebox.showinfo("alert","customer fetched")

var=StringVar()
name=StringVar()
dob=StringVar()
mfname=StringVar()
address=StringVar()
email=StringVar()
phone=StringVar()
aadhar=StringVar()
pan=StringVar()
    

lb=Label(text="CUSTOMER DELETE AND VIEW FORM",width=55,font=2,bg="black",fg="white",borderwidth=12,relief="sunken")
lb.place(x=150,y=30)
lb0=Label(text="AccountNo.",width=11,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
lb0.place(x=35,y=110)
en0=Entry(width=50,font=2,borderwidth=5,relief="sunken")
en0.place(x=200,y=110) 
lb1=Label(text="Name",width=11,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
lb1.place(x=35,y=160)
en1=Entry(textvariable=name,width=50,font=2,borderwidth=5,relief="sunken")
en1.place(x=200,y=160) 
lb2=Label(text="D.O.B",width=11,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
lb2.place(x=35,y=210)
en2=Entry(textvariable=dob,width=50,font=2,borderwidth=5,relief="sunken")
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
lb9=Label(text="PAN No.",width=11,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
lb9.place(x=35,y=570)
en9=Entry(textvariable=pan,width=50,font=2,borderwidth=5,relief="sunken")
en9.place(x=200,y=570)


btn2=Button(text="view",command=viewcustomer,width=15,font=2,bg="pink",fg="black")
btn2.place(x=40,y=670)

btn2=Button(text="delete",command=deletecustomer,width=15,font=2,bg="pink",fg="black")
btn2.place(x=240,y=670)
btn2=Button(text="update",command=updatecustomer,width=15,font=2,bg="pink",fg="black")
btn2.place(x=440,y=670)

btn2=Button(text="back",command=back,width=15,font=2,bg="pink",fg="black")
btn2.place(x=640,y=670)


top2.mainloop()
