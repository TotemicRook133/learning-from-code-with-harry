#wapp to accept marks of 6 students and display them in a sorted manner
f1=int(input("Enter marks of student 1: "))
f2=int(input("Enter marks of student 2: "))
f3=int(input("Enter marks of student 3: "))
f4=int(input("Enter marks of student 4: "))
f5=int(input("Enter marks of student 5: "))
f6=int(input("Enter marks of student 6: "))
myList=[f1,f2,f3,f4,f5,f6]
myList.sort()
print(myList)