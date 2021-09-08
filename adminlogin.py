from tkinter import*
import pymysql
from tkinter import messagebox
top=Tk()
top.title("banking management system")
top.configure(background="skyblue")
top.geometry("600x500")

def aa():
    e=en.get()
    p=en1.get()
    
    if(e=="surbhi2000@gmail.com" and p=="abcde"):
        top.destroy()
        import adminbutton
    else:
        messagebox.showinfo("alert","invalid user")

def bb():
    e=en.get()
    p=en1.get()
    con=pymysql.Connection(user="root",password="",host="localhost",port=3306,database="banking mgmt")
    cur=con.cursor()
    cur.execute("select * from addemployee where empemail=%s and password=%s",(e,p))
    cur.fetchall()
    d=int(cur.rowcount)
    if (d<=0):
        messagebox.showinfo("alert","invalid user")
        
    else:
        messagebox.showinfo("alert","valid user")
        top.destroy()
        import employeepanel
           
lb=Label(text="ADMIN LOGIN",width=44,height=2,font=20,bg="black",fg="white",borderwidth=5,relief="ridge")
lb.place(x=100,y=20)
lb1=Label(text="enter e-mail",width=22,font=2,bg="white",fg="black",borderwidth=5,relief="groove")
lb1.place(x=40,y=100)
en=Entry(width=30,font=2,borderwidth=5,relief="sunken")
en.place(x=300,y=100)          
          
lb2=Label(text="enter password",width=22,font=2,bg="white",fg="black",borderwidth=5,relief="groove")
lb2.place(x=40,y=150)
en1=Entry(width=30,font=2,borderwidth=5,relief="sunken")
en1.place(x=300,y=150)
btn=Button(text="admin login",width=22,font=2,bg="pink",fg="black",borderwidth=5,relief="groove",command=aa)

btn.place(x=200,y=300)
btn1=Button(text="employee login",width=22,font=2,bg="pink",fg="black",borderwidth=5,relief="groove",command=bb)

btn1.place(x=200,y=390)
          
top.mainloop()
