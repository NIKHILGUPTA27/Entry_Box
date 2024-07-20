from tkinter import*
HU=Tk()
HU.title("My Page")
def cal_SI ():
    Result.delete(0,END)
    p=int(E1.get())
    t=int(E2.get())
    r=int(E3.get())
    si=(p*r*t)/100
    Result.insert(0,si)
def cal_CI ():
    Result.delete(0,END)
    p=int(E1.get())
    t=int(E2.get())
    r=int(E3.get())
    si=(p*r*t)/100
    ci=si+p
    Result.insert(0,ci)
        
    
Result=Entry(HU,font=("calibri",25,"bold"),bg="pink",fg="blue",bd=15,width=35)
Result.grid(columnspan=2)
L1=Label(HU,text=" PA:- ",font=("calibri",20,"bold"),fg="green")
L1.grid(row=1,column=0)
L2=Label(HU,text=" Time:- ",font=("calibri",20,"bold"),fg="green")
L2.grid(row=2,column=0)
L3=Label(HU,text=" Rate:- ",font=("calibri",20,"bold"),fg="green")
L3.grid(row=3,column=0)

E1=Entry(HU,font=("calibri",25,"bold"),bg="pink",fg="Blue",bd=10,width=17)
E1.grid(row=1,column=1)
E2=Entry(HU,font=("calibri",25,"bold"),bg="pink",fg="Blue",bd=10,width=17)
E2.grid(row=2,column=1)

E3=Entry(HU,font=("calibri",25,"bold"),bg="pink",fg="Blue",bd=10,width=17)
E3.grid(row=3,column=1)
B1=Button(HU,text=" SI:- ",font=("calibri",20,"bold"),bg="pink",fg="Blue",bd=10,width=20,command=cal_SI)
B1.grid(row=4,column=0)
B2=Button(HU,text=" CI:- ",font=("calibri",20,"bold"),bg="pink",fg="Blue",bd=10,width=20,command=cal_CI)
B2.grid(row=4,column=1)
HU.mainloop()
