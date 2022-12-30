#WAF to input a string and replace the first latter of each word with its capital latter
str = input("Enter your String : ").split(' ')
for i in str:
    # index=0
    i=i[0].capitalize()+i[1:]
    print(i,end=' ')
print(" ")
# output:
# Enter your String : vikas sharma
# Vikas Sharma  