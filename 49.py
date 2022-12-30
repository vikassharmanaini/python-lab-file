#WAP to input hexadecimal number and convert it to its equivalent binary using string
str=input("Enter your hexadecimal number : ")
dec=0
for i in range(len(str)):
    dec=dec+int(str[i])*(16**(len(str)-i))
while(dec>1):
    dec=dec//2
    print(dec%2,end='')
print("")
# output:
# Enter your hexadecimal number : 343
# 0001100001011