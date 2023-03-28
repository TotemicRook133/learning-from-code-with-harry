'''a=["guava",]
i=1
for i in range(1,7):
    x=input("enter fruits")
    a.append(x)

print (a)
'''
# wapp to store seven fruits in a list entered by the user
f0=input("Enter first fruit")
f1=input("Enter second fruit")
f2=input("Enter third fruit")
f3=input("Enter fourth fruit")
f4=input("Enter fifth fruit")
f5=input("Enter sixth fruit")
f6=input("Enter seventh fruit")
flist=[f0,f1,f2,f3,f4,f5,f6]#--> represents list
print("your list/array is",flist)
ftuple=(f0,f1,f2,f3,f4,f5,f6)#--> represents tuple
print("tuple of your input values is",ftuple)