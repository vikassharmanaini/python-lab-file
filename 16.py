# WAP to find largest no among three number
a,b,c=eval(input("enter your three number :"))
if a>b and a>c:
    print(f"Greatest number : {a}")
elif(b>a and b>c):
    print(f"Greatest number : {b}")
else:
    print(f"Greatest number : {c}")

# output:-
# enter your three number :5,6,3
# Greatest number : 6
