#wapp to make equilateral triangle
x=input("Enter a number")
n=len(x)
for i in range(0,len(x)+1,2):
    print(" " * (n-i-1),end="")
    print(x[:i], end="")
    print(" " * (n-i-1))