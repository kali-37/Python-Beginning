# To make a dictionary to convert nepali word in nepali

from typing import MutableSequence


mydict ={
    "Panka":"Fan",
    "masu": "Meat"
}

print("Words available to convert are ", mydict.keys())
a=input("Enter a word you want to translate :\n")
print("The meaning of the word is : \n",mydict[a])
print("The meaning of the word is : \n",mydict.get(a)) 
# .get donot throws any error if we mis type key of dictionary too 
# where as the mydict[a] does throw error if misplaced
