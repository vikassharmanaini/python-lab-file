#Read the cost and selling price of an object and write a program to find the profit or loss earned by seller.
cost,sell=eval(input("Enter the cost and sell price : "))
result= cost-sell
if result<0:
    print(f"Your Profit is {abs(result)}")
else :
    print(f"Your Loss is {abs(result)}")

# output :
# Enter the cost and sell price : 136,263
# Your Profit is 127