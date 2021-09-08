from tkinter import*
top1=Tk()
top1.configure(background="skyblue")
top1.geometry("600x500")
top1.title("admin window")
def back():
    top1.destroy()
    import adminlogin

def addemployee():
    top1.destroy()
    import employeeform
def viewemployee():
    top1.destroy()
    import employeeform
def deleteemployee():
    top1.destroy()
    import employeeform
def updateemployee():
    top1.destroy()
    import employeeform     
    
lb=Label(text="ADMIN CONTROL PANEL",width=44,font=2,bg="black",fg="white",borderwidth=7,relief="sunken")
lb.place(x=100,y=40)    
btn1=Button(text="ADD EMPLOYEE",command=addemployee,width=22,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
btn1.place(x=190,y=100)
btn2=Button(text="VIEW EMPLOYEE",command=viewemployee,width=22,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
btn2.place(x=190,y=160)
btn3=Button(text="DELETE EMPLOYEE",command=deleteemployee,width=22,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
btn3.place(x=190,y=220)
btn4=Button(text="UPDATE EMPLOYEE",command=updateemployee,width=22,font=2,bg="pink",fg="black",borderwidth=5,relief="groove")
btn4.place(x=190,y=280)
btn5=Button(text="back",width=22,font=2,bg="pink",fg="black",borderwidth=5,relief="groove",command=back)
btn5.place(x=300,y=350)

top1.mainloop()
