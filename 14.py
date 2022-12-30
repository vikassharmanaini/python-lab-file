#WAP to reverse a 4-digit number using mathematical operator.
a=int(input("Enter your number :"))
rev=0
while(a>0):
    rem=a%10
    rev=(rev*10)+rem
    a=a//10
print(f"Reverse Number : {rev}")
# output :- 
# Enter your number :6777
# Reverse Number : 7776