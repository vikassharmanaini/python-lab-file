#WAF to print the duplicate elements in the list.
arr=list(map(int,input("Enter elements ' ' sapprated : ").strip().split(' ')))

print("Duplicate elements in given array: ");        
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] == arr[j]):    
            print(arr[j],end=',')
print("")    
# output:
# Enter elements ' ' sapprated : 6 7 8 9 5 78 65 7 9 87 9
# Duplicate elements in given array: 
# 7,9,9,9,