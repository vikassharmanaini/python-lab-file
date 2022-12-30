#WAP to find the three given points are colinear if not find the area of triangle made by the three points.
x1,y1=eval(input("Enter first point : "))
x2,y2=eval(input("Enter first point : "))
x3,y3=eval(input("Enter first point : "))
A= ((x1-x2)**2+(y1-y2)**2)**1/2
B= ((x2-x3)**2+(y2-y3)**2)**1/2
C= ((x3-x1)**2+(y3-y1)**2)**1/2
if(((A+B)==C) or ((A+C)==B) or ((C+B)==A)):
    print("Given points are colinear")
else:
    s=(A+B+C)/2
    print(f"Area of triangle : {abs((s*(s-A)*(s-B)*(s-C))**1/2)}")
# output:-
# Enter first point : 4,5
# Enter first point : 6,8
# Enter first point : 8,10
# Area of triangle : 4010.625