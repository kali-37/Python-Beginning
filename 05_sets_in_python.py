# lists brackets are [] , and tuples are () , where as, for sets they are{}
# sets are same as  that of sets we study in maths


a={} # remember it's not empty sets but it's empty dictionary
print(type(a)) # output will be dict
# but for empty sets we gonna' do is
b=set() # now it's considered as empty sets 
print(type(b))

b.add(4) # it adds 4 to set b
b.add(5)
print(b)



# b.add([4,5,6])
# b.add({ 4:4 })
 
# lists and dictionary can't be added in list bcoz they are 
#  hasable i.e their values can be changed . but as tuples are not hasable their value can be added

# Removal of sets contains

b.add((3,53,66,6))
print(b)
#now tuples will be added manualy in set

# To remove particular containt from the sets 
b.remove(5)
print(b)



print(len(b)) # prints length of the set b
print(b)
print(b.pop()) # yeha pop le* kunai pani euta element lai remove garxa might be random

print(b.intersection())
print(set.clear(b))# set is cleared and on printing it its become null so output is None






