#WAP to print all the letters from word one that also appearing word two.
str1 = 'one'
str2 = 'two'
for i in str1:
    for j in str2:
        if i == j:
            print(i,end=', ')

# output :
# o