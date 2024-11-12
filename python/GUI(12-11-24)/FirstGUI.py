from tkinter import *

Win = Tk()
Win.title("Addition")
Win.geometry("600x400")

a = DoubleVar(value=" ")
b = DoubleVar(value=" ")
c = DoubleVar(value=" ")

def addClick():
    c.set(a.get() + b.get())

def clearClick():
    a.set(" ")
    b.set(" ")
    c.set(" ")

# UI elements
l1 = Label(Win, text="Enter 1st number: ")
l1.grid(row=0, column=0)

t1 = Entry(Win, width=10, textVariable=a)
t1.grid(row=0, column=1)

l2 = Label(Win, text="Enter 2nd number: ")
l2.grid(row=1, column=0)

t2 = Entry(Win, width=10, textVariable=b)
t2.grid(row=1, column=1)

b1 = Button(Win, text="+", command=addClick)
b1.grid(row=2, column=0)

b2 = Button(Win, text="Clear", command=clearClick)
b2.grid(row=2, column=1)

l3 = Label(Win, text="Result: ")
l3.grid(row=3, column=0)

t3 = Entry(Win, width=30, state="readonly", textVariable=c)
t3.grid(row=3, column=1)

# Start the main event loop
Win.mainloop()
