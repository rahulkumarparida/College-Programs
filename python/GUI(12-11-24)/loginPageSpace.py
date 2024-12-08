from tkinter import *
Home = Tk()
Home.title("Login Page")
Home.geometry("400x400")
l1 = Label(Home,text="User ID",fg="cyan").place(x=50,y=50)
e1 = Entry(Home,bg="orange").place(x=150,y=50)
l2 = Label(Home,text="Password",fg="green").place(x=50,y=150)
e2 = Entry(Home,bg="orange").place(x=150,y=150)
b1 = Button(Home, text="Login",bg="red",fg="white").place(x=120,y=250)
b2 = Button(Home, text="Forget",bg="green",fg="white").place(x=180,y=250)
b3 = Button(Home, text="Cancel",bg="blue",fg="white").place(x=250,y=250)

Home.mainloop()
