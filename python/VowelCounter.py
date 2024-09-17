#WAP to get a sentence and find the number of vowels present in it
def countvowels(s):  
    vowels = 'aeiouAEIOU'
    vowelcount = 0
    for char in s:
        if char in vowels:
            vowelcount += 1    
    return vowelcount
s = input("write the sentence: ")
numberofvowels = countvowels(s)
print(f"The number of vowels in the sentence are: {numberofvowels}")
