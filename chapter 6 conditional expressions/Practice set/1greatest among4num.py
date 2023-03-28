x1=int(input("enter number 1 "))
x2=int(input("enter number 2 "))
x3=int(input("enter number 3 "))
x4=int(input("enter number 4 "))
print(max(x1,x2,x3,x4))# directly finds the greatest
#another approach taught by Ribenz Rizal
g=x1
if (g<x2):
    g=x2
if(g<x3):
    g=x3
if(g<x4):
    g=x4

print(g)

#world cup approach from code with harry
if (x1>x2):
    f1=x1
else:
    f1=x2
if(x3>x4):
    f2=x3
else:
    f2=x4
if (f1>f2):
    print(f1,"is the greatest number")
else:
    print(f2,"is the greatest number")