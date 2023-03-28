a=["harry","ramesh","suresh","anu","diya"]
xf=input("Enter a name you want to search ")
if (xf in a):
    res=True
else:
    res=False
if (res):
    print(xf,"is present in our list")
else:
    print(xf,"is not present in our list")