# WAP to find Fibonacci series up to n term where n>2.
n=int(input("Enter your term : "))
i=2
f=0
l=1
print(f)
while i < n:
    print(l)
    tem = f
    f=l
    l=l+tem
    i=i+1
# output : 
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89
# 144
# 233
# 377
# 610
# 987
# 1597
# 2584