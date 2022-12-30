#WAP to create a list with element 1 to 10 to display even element of list using list
list=range(1,10)
list2=[]
for i in range(1,10):
    if i%2==0:
        list2.append(i)
print(list2)
# output:
# [2, 4, 6, 8]