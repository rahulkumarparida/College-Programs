nm=input("Enter Your Name:--")
m=int(input("Enter the marks obtained in math:--"))
it=int(input("Enter the marks obtained in Information technology:--"))
c=int(input("Enter the marks obtained in Chemistry:--"))
p=int(input("Enter the marks obtained in Physics:--"))
b=int(input("Enter the marks obtained in Biology:--"))
sst=int(input("Enter the marks obtained in Social Science:--"))
sm=(m+it+c+p+b+sst)
per=(sm/600)*100
print("Name:--",nm)
print("Total Mark Secured:--",sm)
print("You have got ",per)
if per>=90:
    print("You have got grade O. Keep it up!!")
elif per>=80:
    print("You have got grade E. Veryy Good!!")
elif per>=70:
    print("You have got grade A. Good!!")
elif per>=60:
    print("You have got grade B. Keep Working!!")
elif per>=50:
    print("You have got grade C. Try Harder!!")
elif per>=40:
    print("You have got grade D. Try Harder!!")
else:
    print("You have Failed the Exam. Don't worry try Again")
