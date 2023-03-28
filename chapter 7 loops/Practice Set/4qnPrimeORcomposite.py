#wapp to find whether a given number is prime or not
num=int(input("Enter a number"))
c=0
for i in range(2,num):
    if(num%i==0):
        c=c+1
if c==0 and num!=1 and num!=0:
    print("it is prime")
elif(num==1 or num==1):
    print("neither prime nor composite")
else:
    print("composite")
    
# code with harry's approach
