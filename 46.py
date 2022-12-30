#WAF to count space which takes string as argument and return the no of blank space in string
str = input("Enter your string :")

print(f"number of space in string : {len(str.split(' '))-1}")
for i in str.split(' '):
    print(i,end='')
# output:
# Enter your string :my name is vikas
# number of space in string : 3
# mynameisvikas