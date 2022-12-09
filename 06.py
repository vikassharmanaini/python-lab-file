# WAP to find the all-trigonometric ratio by input three sides of a right-angled triangle.
p,b,h=eval(input("Enter the value Parpendicular, Base and Hypotenous : "))
sin=p/h
cos=b/h
tan=p/b
print(f"sin\u03B8 = {sin} \ncos\u03B8 = {cos} \ntan\u03B8 = {tan} \ncot\u03B8 = {1/tan} \ncos\u03B8 = {1/cos} \ncosec\u03B8 = {1/sin}")
# output :-
# Enter the value Parpendicular, Base and Hypotenous : 3,4,5
# sinθ = 0.6 
# cosθ = 0.8 
# tanθ = 0.75 
# cotθ = 1.3333333333333333 
# cosθ = 1.25 
# cosecθ = 1.6666666666666667