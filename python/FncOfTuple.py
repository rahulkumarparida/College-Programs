l=[];
n = int(input("Enter the Length : "));
for i in range(n):
    p = int(input("Enter the Values : "))
    l.append(p);
print(l);
l.sort()
# we know that k is a list lets convert it tuple
k = tuple(l);
print(k);
# functions of tuple
length = len(k);
print(length , " is the length of the Tuple");
maxi =  max(k);
print(maxi , " is the Max element in the Tuple");
mini = min(k);
print(mini , " is the Min element of the Tuple");
idx = k.index(1);
print(idx , " is the index of 1 in Typle");
count = k.count(1);
print(count , " is the number 1's present in the Tuple");
summ = sum(k);
print(summ , " is the sum of all the elements present in the Tuple");
