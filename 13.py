#WAP to calculate distance between two points using distance formula.
x1,y1=eval(input("Enter the first point coordinates : "))
x2,y2=eval(input("Enter the first point coordinates : "))
print(f"Distance between two points : {(((x2-x1)**2)+((y2-y1)**2))**(1/2)}")
# output:-
# Enter the first point coordinates : 3,4
# Enter the first point coordinates : 4,6
# Distance between two points : 2.23606797749979