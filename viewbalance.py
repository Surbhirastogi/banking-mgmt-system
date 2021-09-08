from tkinter import*
from tkinter import messagebox
import pymysql
top2=Tk()
top2.configure(background="skyblue")
top2.geometry("600x600")
top2.title("balance view")

def exit():
    top2.destroy()
    import balanceform

def oldbalance():
    oldbal=en1.get()
    con=pymysql.Connection(user="root",password="",host="localhost",port=3306,database="banking mgmt")
    cur=con.cursor()
    cur.execute("select * from balance where accountno=%s",(acc))
    data=cur.fetchall()
    

btn2=Button(text="EXIT",command=exit,width=20,font=2,bg="pink",fg="black")
btn2.place(x=340,y=460)
lb0=Label(text="hi!",width=5,font=2,bg="yellow",fg="black",borderwidth=5,relief="groove")
lb0.place(x=100,y=30)
lb0=Label(text="you can check your current status fron here",width=40,font=2,bg="white",fg="black",borderwidth=5,relief="groove")
lb0.place(x=100,y=90)
en1=Entry(width=30,font=2,borderwidth=5,relief="sunken")
en1.place(x=160,y=30) 
lb1=Label(text="OLD BALANCE",width=20,font=2,bg="yellow",fg="black",borderwidth=5,relief="groove")
lb1.place(x=50,y=150)
en1=Entry(width=30,font=2,borderwidth=5,relief="sunken")
en1.place(x=250,y=150) 
lb2=Label(text="DEPOSITED AMOUNT",width=20,font=5,bg="yellow",borderwidth=5,relief="groove")
lb2.place(x=50,y=220)
en2=Entry(width=30,font=2,borderwidth=5,relief="sunken")
en2.place(x=250,y=220)
lb3=Label(text="CURRENT BALANCE",width=20,font=5,bg="yellow",borderwidth=5,relief="groove")
lb3.place(x=50,y=290)
en4=Entry(width=30,font=2,borderwidth=5,relief="sunken")
en4.place(x=250,y=290) 

top2.mainloop()
