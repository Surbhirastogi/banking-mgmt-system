from tkinter import*
import math
from tkinter import messagebox
import pymysql
top2=Tk()
top2.configure(background="skyblue")
top2.geometry("600x600")
top2.title("balance sheet")
def view():
    top2.destroy()
    import viewbalance

def exit():
    top2.destroy()
    import employeepanel    

def deposit():
    acc=int(en1.get())
    amnt=int(en2.get())
    con=pymysql.Connection(user="root",password="",host="localhost",port=3306,database="banking mgmt")
    cur=con.cursor()
    cur.execute("select * from balance where accountno=%s",(acc))
    data=cur.fetchall()
    for i in data:
        d=(i[1])
        t=d+amnt
        cur1=con.cursor()
        cur1.execute("update balance set amount=%s where accountno=%s",(t,acc))
        
    con.commit()
    messagebox.showinfo("alert","amount desposited successfully")
def withdraw():
    acc=int(en1.get())
    amnt=int(en2.get())
    con=pymysql.Connection(user="root",password="",host="localhost",port=3306,database="banking mgmt")
    cur=con.cursor()
    cur.execute("select * from balance where accountno=%s",(acc))
    data=cur.fetchall()
    for i in data:
        d=(i[1])
        t=d-amnt
        cur1=con.cursor()
        cur1.execute("update balance set amount=%s where accountno=%s",(t,acc))
        
    con.commit()
    messagebox.showinfo("alert","amount withdrawn successfully")
 

lb=Label(text="WELCOME",width=55,font=2,bg="black",fg="white",borderwidth=12,relief="sunken")
lb.place(x=40,y=30)  
lb1=Label(text="ACCOUNTNO.",width=20,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
lb1.place(x=35,y=110)
en1=Entry(width=30,font=2,borderwidth=5,relief="sunken")
en1.place(x=250,y=110) 
lb2=Label(text="ENTER AMOUNT",width=20,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
lb2.place(x=35,y=180)
en2=Entry(width=30,font=2,borderwidth=5,relief="sunken")
en2.place(x=250,y=180) 
lb2=Label(text="please select from the following",font=5,bg="yellow")
lb2.place(x=200,y=290)
btn1=Button(text="DEPOSIT FUND",command=deposit,width=20,font=2,bg="pink",fg="black")
btn1.place(x=340,y=340)
btn2=Button(text="WITHDRAW FUND",command=withdraw,width=20,font=2,bg="pink",fg="black")
btn2.place(x=100,y=340)
btn2=Button(text="VIEW BALANCE",command=view,width=20,font=2,bg="pink",fg="black")
btn2.place(x=100,y=400)
btn2=Button(text="NEW ACCOUNT",width=20,font=2,bg="pink",fg="black")
btn2.place(x=340,y=400)
btn2=Button(text="EXIT",command=exit,width=20,font=2,bg="pink",fg="black")
btn2.place(x=340,y=460)


