#wapp to find the sum of first n natural numbers using while loop.
sum=0
num=int(input("Enter a number"))
for i in range(1,num+1):
    sum=sum+i
print("the sum upto",num, "is", sum)
