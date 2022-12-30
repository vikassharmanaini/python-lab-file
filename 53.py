#WAF to make a list of cubes of the elements of existing list by passing the existing list as argument to the function and return the list as output.
def cube(n):
    l=[]
    for i in n :
        l.append(i**3)
    return l
l=list(map(int,input("Enter numbers ' ' sapprated : ").strip().split(' ')))
print(f"result = {cube(l)}")
# output:
# Enter numbers ' ' sapprated : 5 8 7 6 5 46 9
# result = [125, 512, 343, 216, 125, 97336, 729]