from tkinter import *
Home = Tk()
Home.title("Login Page")

l1 = Label(Home,text="User ID",fg="cyan").grid(row=0,column=0)
e1 = Entry(Home,bg="orange").grid(row=0,column=1)
l2 = Label(Home,text="User ID",fg="green").grid(row=1,column=0)
e2 = Entry(Home,bg="orange").grid(row=1,column=1)
b1 = Button(Home, text="Login",bg="red",fg="white").grid(row=2,column=0)
b2 = Button(Home, text="Forget",bg="green",fg="white").grid(row=2,column=1)
b3 = Button(Home, text="Cancel",bg="blue",fg="white").grid(row=2,column=2)

Home.mainloop()
