myDict={
    "1. पङ्खा":"Fan",
    "2. बट्टा":"box",
    "3. वस्तु":"item"
}
numDict={
    "1":"Fan",
    "2":"box",
    "3":"item"}
print(myDict.keys())
x=input("which number do you want to see the meaning. Enter the number")
print(numDict.get(x))