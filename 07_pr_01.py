
# It's for Table multiplication
num=float(input("Enter a n.b :\n"))
# yeha float is used instead of int to print greater than base 10 i.e in decimals.

for i in range(1,1001):
    print(str(num)+"*"+str(i)+"="+(str(num*i)))
# now it will print up to 5*10000 becoz 1 is used to 1001 
#line 7 ko thau ma we can use ; f walla string as follow for same table calculation
    print(f"{num}*{i}={num*i}")

'''line 7 or 10 is same to print where f string rakhepaxi
we can type string simply and variables in set wala bracket simply to make code easy
'''