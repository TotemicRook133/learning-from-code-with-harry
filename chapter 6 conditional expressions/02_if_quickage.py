age=int(input("Enter your age"))
if age>=18:
    print("yes")
else:
    print("no")
#and statement
year=int(input("Enter the year"))
if year % 4==0 and year %100!=0:
    print("leap year")
else:
    print("no")