from tkinter import*
import pymysql
top2=Tk()
top2.configure(background="skyblue")
top2.geometry("600x500")
top2.title("employee window")
def back():
    top2.destroy()
    import adminlogin

def addcustomer():
    top2.destroy()
    import customerform
def updatecustomer():
    top2.destroy()
    import customerform    

def viewcustomer():
    top2.destroy()
    import customerdeleteform    
def deletecustomer():
    top2.destroy()
    import customerdeleteform    
def addbalance():
    top2.destroy()
    import balanceform
def withdrawbalance():
    top2.destroy()
    import balanceform
    
    
lb=Label(text="empolyee control panel",width=44,font=2,bg="black",fg="white",borderwidth=7,relief="sunken")
lb.place(x=100,y=40)    
btn1=Button(text="ADD CUSTOMER",command=addcustomer,width=22,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
btn1.place(x=190,y=100)
btn2=Button(text="VIEW CUSTOMER",command=viewcustomer,width=22,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
btn2.place(x=190,y=160)
btn3=Button(text="DELETE CUSTOMER",command=deletecustomer,width=22,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
btn3.place(x=190,y=220)
btn4=Button(text="UPDATE CUSTOMER",command=updatecustomer,width=22,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
btn4.place(x=190,y=280)
btn5=Button(text="ADD BALANCE",command=addbalance,width=22,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
btn5.place(x=190,y=340)
btn5=Button(text="WITHDRAW BALACE",command=withdrawbalance,width=22,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
btn5.place(x=190,y=400)
btn6=Button(text="back",width=11,font=2,bg="pink",fg="black",command=back)
btn6.place(x=450,y=450)

top2.mainloop()
