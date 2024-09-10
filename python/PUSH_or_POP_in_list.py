k =[];
n = int(input("Enter the number of elemnts you want to add in the stack : "))
for i in range(n):
    p= int(input("Enter the vlaue : "));
    k.append(p);
k.sort();
print(k);
print("Press 1 for Push/Add Element");
print("Press 2 for Pop/Delete Elements");
print("Enter the operation you want to perform ");
option = int(input(": - "))
if(option == 1):
    new = int(input("Enter the element : "));
    k.append(new);
    print(k);
elif(option == 2):
    k.del(k[0]);
    print(k);
else:
    print("Invalid Choice ^---^ ")
    
