#wapp to calculate the grade of  a student from his marks from the following scheme

marks=int(input("enter your marks "))

if(marks<=100 and marks >=90):
    print("Your grade is Ex")
elif(marks >=80):
    print("Your grade is A")
elif(marks >=70):
    print("Your grade is B")
elif(marks >=60):
    print("Your grade is C")
elif(marks >=50):
    print("Your grade is D")
elif(marks >=0):
    print("Your grade is F")
else:
    print("Your input is invalid")