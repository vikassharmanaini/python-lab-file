#WAF to check whether a list is Palindrome or not.
l=list(map(int,input("Enter elements ' ' sapprated : ").strip().split(' ')))
for i in range(len(l)//2):
    if l[i]!=l[-(i+1)]:
        print("Given number is not palendrom")
        break
    if (i+1) == len(l)//2:
        print("Given number is palendrom")
# output:
# Enter elements ' ' sapprated : 1 2 3 4 4 3 2 1
# Given number is palendrom