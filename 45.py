#WAP to input a string of at least six words and split string using split() into list of word.
str=input("Enter your string : ")
a=str.split(' ')
if(len(a)>=6):
    print(a)
else:
    print("Please enter at least 6 word")
# output : 
# Enter your string : my name is vikas sharma from pryagraj
# ['my', 'name', 'is', 'vikas', 'sharma', 'from', 'pryagraj']