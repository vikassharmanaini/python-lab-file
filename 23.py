#WAP to enter a no to display the respective day of weeks. start day Sunday.
day= int(input("Enter a number 1-7 : "))

if (day==1):
    print(day," is Sunday")
elif (day==2):
    print(day," is Monday")
elif (day==3):
    print(day," is Tuesday")
elif (day==4):
    print(day," is Wednesday")
elif (day==5):
    print(day," is Thursday")
elif (day==6):
    print(day," is Friday")
elif (day==7):
    print(day," is Saturday")
else:
    print("Wrong Input!!!!!")
# output : 
# Enter a number 1-7 : 6
# 6  is Friday