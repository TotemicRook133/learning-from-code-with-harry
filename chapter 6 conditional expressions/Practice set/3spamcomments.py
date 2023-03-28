"""A spam comment is defined as a text containing following keywords:
    "make a lot of money", "buy now", "submit this", "click this". 
    Wapp to detect these spams"""

com=input("Enter your comment")
if(com=="make a lot of money" or com=="buy now"or com== "submit this"or com== "click this"):
    print("spam comment so not print")
else:
    print(com)
if(com.find("make a lot of money")!=-1 or com.find("buy now")!=-1 or com.find("submit this")!=-1 or com.find("click this")!=-1):
    print("spam comment so not print")
else:
    print(com)

#codewithHarry Approach
if("make a lot of money" in com):
    spam=True
elif("buy now" in com):
    spam=True
elif("click this" in com):
    spam=True
elif("subscibe this" in com):
    spam=True
else:
    spam = False

if(spam):
    print("spam so not print")
else:
    print(com)


