#wapp to find out whther a student is pass or fail, if it requires total 40% and at least 33% in eatch subject. Assume 3 subjects and take marks as an inpur from the user.
math=int(input("Enter the marks of Math "))
science=int(input("Enter the marks of Science "))
computer=int(input("Enter the marks of computer "))
total=(math+science+computer)/3
if(total >=40 and science>=33 and math>=33 and computer>=33):
    print("pass")
else:
    print("fail")