# To input and access the Roll no. and Name of the given numbers
d = {};
n=int(input("Enter the number of Students : "));
for i in range(n):
    roll = input('Enter Roll Number: ');
    name = input('Enter the Name: ');
    d[roll]=name;
print(d);
for i,j in d.items():
    print(i," : ",j);
for k in d.keys():
    print(k);
for i in d.values():
    print(i);
    
