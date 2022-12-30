#WAP to check whether a no is Armstrong or not.
def check(n):
    t=len(str(n))
    sum=0
    for i in range(t):
        sum=sum+int(str(n)[i])**t
    if n==sum:
        return True
    else:
        return False
num=int(input("Please Input your number : "))
print(f"given number is Armsttrong : {check(num)}")
# output : 
# Please Input your number : 565
# given number is Armsttrong : False