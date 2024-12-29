# 5!=1 X 2 X 3 X 4  X  5

n=int(input("Enter the number for the factorial:"))
product=1
i=1
while(i<=n):
    product=product*i
    i+=1


print(f"The factorial for {n} is ", product)    