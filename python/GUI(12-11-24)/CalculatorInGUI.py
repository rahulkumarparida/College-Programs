from tkinter import *
Home = Tk()
Home.title = "Addtion of Two Numbers"

l1 = Label(Home,text="First Number : ").grid(row=0,column=0)
l2 = Label(Home,text="Second Number : ").grid(row=1,column=0)
l3 = Label(Home,text="Result : ").grid(row=2,column=0)
a= StringVar()
b= StringVar()
c= StringVar()
e1 = Entry(Home,textvariable = a).grid(row=0,column=1)
e2 = Entry(Home,textvariable = b).grid(row=1,column=1)
e3 = Entry(Home,textvariable = c).grid(row=2,column=1)
def add():
    x=int(a.get())
    y=int(b.get())
    z=x+y
    c.set(z)
b1= Button(Home,text="add",command=add).grid(row=4,column=0)

def sub():
    x=int(a.get())
    y=int(b.get())
    z=x-y
    c.set(z)
b2= Button(Home,text="substract",command=sub).grid(row=4,column=1)

def mul():
    x=int(a.get())
    y=int(b.get())
    z=x*y
    c.set(z)
b3= Button(Home,text="multiply",command=mul).grid(row=4,column=2)

def div():
    x=int(a.get())
    y=int(b.get())
    z=x/y
    c.set(z)
b4= Button(Home,text="divide",command=div).grid(row=4,column=3)

def mod():
    x=int(a.get())
    y=int(b.get())
    z=x%y
    c.set(z)
b5= Button(Home,text="add",command=mod).grid(row=4,column=4)

Home.mainloop()