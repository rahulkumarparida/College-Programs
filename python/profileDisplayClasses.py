class Profile:
    def __init__(self, n, r, a, g):
        self.nm = n
        self.roll = r
        self.age = a
        self.gender = g

    def display(self):
        print("Your Name is:", self.nm)
        print("Roll number:", self.roll)
        print("Your Age is:", self.age)
        print("You are a", self.gender)

n = input("Enter your Name: ")
r = input("Enter Your Roll Number: ")
a = input("Enter your age: ")
g = input("What is your Gender: ")

obj = Profile(n, r, a, g)
obj.display()
