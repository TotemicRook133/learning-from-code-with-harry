myDict={
    "fast": "In a quick Manner",
    "harry": "A coder",#here it is a string
    "marks": 20, #--> int
    "table":[20,30,40,50],#--> list/array
    "anotherDict":{
        "hello":"fuchhe"
    },#--> nested Disctionary
}
print(myDict['harry'])
print(myDict['table'])
print(myDict['anotherDict']["hello"])

#dictionary are mutable
myDict['table']=[20,40,30,50]
print(myDict["table"])

