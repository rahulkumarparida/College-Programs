from tkinter import *

# Set up the main window
Home = Tk()
Home.title("Addition of Two Numbers")
Home.geometry("400x250")  # Set window size
Home.config(bg="lightblue")  # Set background color

# Define fonts and colors
font_label = ("Arial", 12)
font_entry = ("Arial", 12)
font_button = ("Arial", 10, "bold")
bg_button = "lightgreen"
fg_button = "black"

# Create Labels with styling
l1 = Label(Home, text="First Number: ", font=font_label, bg="lightblue").grid(row=0, column=0, padx=10, pady=10, sticky="e")
l2 = Label(Home, text="Second Number: ", font=font_label, bg="lightblue").grid(row=1, column=0, padx=10, pady=10, sticky="e")
l3 = Label(Home, text="Result: ", font=font_label, bg="lightblue").grid(row=2, column=0, padx=10, pady=10, sticky="e")

# Create Entry fields with styling
a = StringVar()
b = StringVar()
c = StringVar()
e1 = Entry(Home, textvariable=a, font=font_entry, width=20).grid(row=0, column=1, padx=10, pady=10)
e2 = Entry(Home, textvariable=b, font=font_entry, width=20).grid(row=1, column=1, padx=10, pady=10)
e3 = Entry(Home, textvariable=c, font=font_entry, width=20, state="readonly").grid(row=2, column=1, padx=10, pady=10)

# Function for addition
def add():
    try:
        x = int(a.get())
        y = int(b.get())
        z = x + y
        c.set(z)
    except ValueError:
        c.set("Invalid Input")

# Create Button with styling
b1 = Button(Home, text="Add", command=add, font=font_button, bg=bg_button, fg=fg_button).grid(row=4, column=1, padx=10, pady=20)

# Start the main loop
Home.mainloop()
