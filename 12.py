#WAP to read the weight of an object in gram and display its weight in Kg and Gram.
w = int(input("Enter weight of object in gram : "))
print(f"Weight of object {w//1000}kg and {w%1000}g")
# output:-
# Enter weight of object in gram : 5887
# Weight of object 5kg and 887g