#WAP to find roots of equation ax^2+bx+c and check the nature of roots
a,b,c = eval(input("In equation ax^2+bx+c enter a,b and c : "))
print(f"eq : {a}x^2+{b}x+{c}")
D=(b**2)-4*a*c
alfa = (-b+(D**1/2))/2*a
beta = (-b-(D**1/2))/2*a
if(D>0):
    print(f"Roots are {alfa}, {beta}")
    print(f'Nature= Real and Unique')
elif(D==0):
    print(f"Roots are {alfa}, {beta}")
    print(f'Nature= Real and equal')
elif(D<0):
    print(f"Roots are {alfa}, {beta}")
    print(f'Nature= Imagnary and Unique')

# output:
# In equation ax^2+bx+c enter a,b and c : 2,4,5
# eq : 2x^2+4x+5
# Roots are -16.0, 8.0
# Nature= Imagnary and Unique