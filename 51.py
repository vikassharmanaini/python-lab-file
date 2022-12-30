#WAP create a list from 1 t0 10 and generate other list containing squares of first list.
list=range(1,10)
list2=[]
for i in range(1,10):
   list2.append(i**2)
print(list2)
# output:
# [1, 4, 9, 16, 25, 36, 49, 64, 81]