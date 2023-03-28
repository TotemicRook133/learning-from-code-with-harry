#Creating an empty set
b=set()
print(type(b))

#adding values to an empty set
b.add(4)
b.add(5)
b.add(5)#no effect
# b.add([6,7,8])# cannot take place as list cannot be added
#but
b.add((4,5,6))# tuples can be added
print (b)
# b.add({4:5})#cannot add list or dictionary as they are hashable ie can be modified.

#methods
print(len(b))#--> tells how many items are there in the set
b.remove(5)#removes 5 from set
# b.remove(15)#error since 15 is not in the set
print(b)


print(b.pop()) #removes the first element and returns its value
print(b)

# b.clear()# empties the set
print(b)

b.add(1)
b.add(5)
s={1,5,8}
#intersection of b and s
print(b.intersection(s))
#union of b and s
print(b.union(s))