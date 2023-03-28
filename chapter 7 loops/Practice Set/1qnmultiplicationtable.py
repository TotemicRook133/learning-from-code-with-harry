#wapp to print multiplication table of a given number using for loop

x=int(input("Enter the number "))
for i in range(1,11):
    print(x,"x",i,"=",(x*i))
    print(f"{x}x{i}={i*x}")