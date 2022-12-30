#WAP to print the factorial of number.

def facto(num):
    f=1
    for i in range(num+1):
        if i !=0:
            f=f*i
    return f
n=int(input("Enter your positive intiger : "))
print(f"factorial = {facto(n)}")
# output:
# Enter your positive intiger : 5
# factorial = 120