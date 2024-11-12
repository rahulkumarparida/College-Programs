fp = open("num.txt","w")
for i in range(26):
    fp.write("he")
fp.close()
fp = open("num.txt","r")
fpt = open("odd.txt" , "w")
ptr = open("even.txt" , "w")
fp.read()
for i in range(fp):
    if(fp.read()%2== 0):
        ptr.write(fp.read())
    
    else:
        fpt.write(fp.read())

print(fpt.read())
print(ptr.read())
fp.close()
fpt.close()
ptr.close()

