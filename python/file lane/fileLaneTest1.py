def reading(filename):
    fptr = open(filename)
    print(fptr.read())
    fptr.close();
fptr = open("myfile.txt" , "w")
fptr.write("Hello World\n")
fptr.write("Good morning")
fptr.write("Everyone")
fptr.close()
reading("myfile.txt")


