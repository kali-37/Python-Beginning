''' As, Dictonary have their meanings for particular words , likewise 
the below mydict function is too used to assign particular functions for 
given words to clarify its meaning to depth
'''

myDict ={
    "fast":"In a Quick Manner", # here, fast is assigned as a word with meaning 'In a ...'
    "Subash":"A Coder",
    "Marks ":[1,2,5] ,
    "anotherdict":{'subash':'player'}
    ,1:5
}
print(myDict['fast'])
print(myDict['Subash'])

myDict['Marks']=[45,78] # mutable as lists, bcoz as their value can be changed

print(myDict['Marks'])  # now printed value will be changed as above changed confugration
print(myDict['anotherdict'])


print(myDict.keys()) #keys vaneyako aagadi ko print garxa
print(list(myDict.keys()))  # print in list format and we already knew that we can change it to lists
print(myDict.values()) # yeasle keys ko assigned values print garxa
print(myDict.items()) # yeasle keys rw values duati nai display garxa

print(myDict)
# we can update dict too as follows 
updateDict = {  #  yo updateDict ko thau ma j lekhe ni huncha hai coz real update is downard
    "lovis":"friend", # now lovis as key and friend as value is added in dict
    "Subash":"A Dancer" # as we already have Subash in dict now again updating value will be changed
     # Now, A coder is changed to A dancer
}
myDict.update(updateDict)
print(myDict)


print(myDict.get("Subash"))
print(myDict["Subash"])
# mathi ko duati line of code prints the same then why we use .get?


print(myDict.get("skfsfs"))
print(myDict["skfsfs"])
''' Has, mathi ko 2 lines ko barema , i.e the diff between [] and .get syntax

yeha .get wala le output throws none value as 'skfsfs' is not in
dictonary , where as hamle hearne ho vane line n.b 44' is throwing error
so .get rw normal print out ma tehe farak huncha as they did response in
different manner

'''

# for more dictionary methods go google for search
