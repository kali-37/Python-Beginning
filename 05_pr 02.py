s={12, "12",12.4} # all will be printted as all are identical as, 12 and "12 " are integer and strings
print(s)
print(len(s))

b=set()
b.add(23)
b.add(23.0)
b.add("23")
print(b) # here 23 and "23" as output coz 23 and 23.0 are same 
