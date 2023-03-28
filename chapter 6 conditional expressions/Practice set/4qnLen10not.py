# wapp to find whether a fiven username contains less than 10 characters or not.
usern=input("Enter a username name ")
if (len(usern)<10):
    print(usern,"has less than 10 characters")
elif(len(usern)>10):
    print(usern,"contains more than 10 characters")
else:
    print(usern,"contains exactly 10 characters")
