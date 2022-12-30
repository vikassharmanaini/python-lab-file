#WAP to Display a result (nested if).
name = input("Enter your name : ")
m,ds,p,ph,j=eval(input("Enter Math,DS,Python,PHP,JAVA :"))
print(f"Student name : {name}")
p=(m+ds+p+ph+j)*100/500 
if(p<33):
    print(f"Better luck next time {p}")
elif(p>33 and p<61):
    print(f"Division : {p}")
elif(p>60 and p<71):
    print(f"division : {p}")
elif(p>70):
    print(f"you have clear this exam with first division")
else:
    print("please enter correct info")
# output:
# Enter your name : vikas       
# Enter Math,DS,Python,PHP,JAVA :78,78,68,98,58
# Student name : vikas
# you have clear this exam with first division