#Calculate the sum of ASCII code of character of given range of capital later by displaying respected ASCII code of later
sum=0
a=input("Enter characters :").split(',')
i=0
while i<len(a):
    sum=sum+ord(a[i])
    i=i+1
print(sum)
# output:
# Enter characters :v,i,k,a,s
# 542