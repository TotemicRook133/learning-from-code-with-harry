#wapp to calculate the factorial of a given number using for loop.
num=int(input("Enter a number"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("the factorial of", num, "is", fact)