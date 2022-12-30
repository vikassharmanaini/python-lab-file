#WAP to perform basic arithmetic operation on two number by choice.
num1 = input('Enter first number: ')  
num2 = input('Enter second number: ')  
choice = int(input('choice :-\nsum : 1 \tsub : 2\nmul : 3 \tdiv : 4\n'))
sum = float(num1) + float(num2)
min = float(num1) - float(num2) 
mul = float(num1) * float(num2) 
div = float(num1) / float(num2) 
if choice == 1 :
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))  
elif choice ==2:
    print('The subtraction of {0} and {1} is {2}'.format(num1, num2, min))
elif choice ==3:
    print('The multiplication of {0} and {1} is {2}'.format(num1, num2, mul)) 
elif choice ==4 : 
    print('The division of {0} and {1} is {2}'.format(num1, num2, div))  
# Output:
# Enter first number: 56
# Enter second number: 87 
# choice :-
# sum : 1         sub : 2
# mul : 3         div : 4
# 4
# The division of 56 and 87 is 0.6436781609195402
