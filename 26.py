#WAP to find the sum of digit of no.
def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
n = int(input("Enter the your number :"))
print(f"Result : {getSum(n)}")
# output :
# Enter the your number :6797
# Result : 29