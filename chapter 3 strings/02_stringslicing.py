greeting="Good Morning, "
name="Harry"
s=greeting + name
print(type(name))
# Concatenating two string
print(greeting + name) # adds string--> good morning Harry
print(name[-1])
# slicing strings
#name[3]="d" --> does not work it can be accessed but not changed
print(name[:5])# is same as [0:5] where 0 is the first value
print(name[0:])# is same as [0:5] where 5 is the length
print(name[-4:-1])# is same as [1:4]
#slicing with skip value
d=s[1::3]# it adds 3 to 1 and cumulatively adds it until len(s)
print(d)
