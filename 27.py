#WAP to display reverse of a number.
num = int(input("Enter your number : "))
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))

# output : 
# Enter your number : 788
# Reversed Number: 887