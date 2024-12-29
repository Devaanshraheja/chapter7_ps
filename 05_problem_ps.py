
num=int(input("Enter The Number: "))


for i in range(2,num,1):
    if(num%i==0):
        print("The given number isn't prime")
        break

else:
    print("The number is prime")

              