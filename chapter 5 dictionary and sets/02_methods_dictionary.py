from traceback import print_list


myDict={
    "fast": "In a quick Manner",
    "harry": "A coder",#here it is a string
    "marks": 20, #--> int
    "table":[20,30,40,50],#--> list/array
    "anotherDict":{
        "hello":"fuchhe"
    },#--> nested Disctionary
    1:2
}
#printing keys
print(myDict.keys())#--> print all the keys ie fast harry marks and anotherdict
print(type(myDict.keys()))#--> another datatype called dict_keys
#converting dict_keys to list
print(list(myDict.keys()))

#printing values
print(myDict.values())#--> prints all the values
print(type(myDict.values()))#--> datatype dict_values
print(list(myDict.values()))

#to iterate 
print(myDict.items())#--> print all the items inthe format (key,value) for all the contents of the dictionary

#updating the dictionary
UpdateDiction={
    2:5,
    "nice": "good",
}
myDict.update(UpdateDiction)
print(myDict)


#getting the values
print(myDict.get('harry2'))#doesnot show an error returns none
print(myDict['harry2'])#shows an error