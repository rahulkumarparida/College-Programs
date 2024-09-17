#WAP to input a sentence and count each letter how many times do the letter ocuur in it
d ={}
s = input("Write a Sentence : ")
for i in s:
    d[i]=d.get(i,0)+1
for k,v in d.items():
    print(k," ocuurs ", v, " times ")
