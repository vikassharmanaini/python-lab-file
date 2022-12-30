#WAP to print the sum of no from 1 to 20 that is not divisible by 2,3 or 5.
i=0
sum =0
while i<20:
    if i%2 != 0 or i%3 != 0 or i%5 != 0 :
        sum = sum + i
    i=i+1
print(sum)
# output:
# 190