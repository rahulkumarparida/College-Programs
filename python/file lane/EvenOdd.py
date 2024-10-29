fp = open("num.txt","w")
for i in range(26):
    fp.write("he")

fp.close()
fp = open("num.txt","r")
fpt = open("odd.txt" , "w")
fptr = open("even.txt" , "w")
fp.read()
for i in range(fp):
    if(fp.read()%2== 0):
        fpt.write(fp.read())
    
    else:
        fptr.write(fp.read())

print(fpt.read())
print(fptr.read())
fp.close()
fpt.close()
fptr.close()

# content = fp.read()
# fpt.write(content)
# fp.close()
# fpt.close()
# fpt = open("two.txt" , "r")
# print(fpt.read())
# fpt.close()