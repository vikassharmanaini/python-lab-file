# WAF to print the digit in reverse order of a given no using function.
numstr=input("Enter your number : ")
newnum=0
for i in range(len(numstr)):
    newnum=newnum+(int(numstr[i])*(10**i))
print(f"Reversed number : {newnum}")
# output:
# Enter your number : 765576          
# Reversed number : 675567