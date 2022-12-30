# Write a program to test whether a no is divisible by 2,3 or 6.
num = int(input("Enter num : "))
if(num//2==0 or num//3==0):
    print("your num is divisible by 2,3 or 6")
else:
    print("your num is not divisible by 2,3 or 6")
# output:
# Enter num : 67
# your num is not divisible by 2,3 or 6