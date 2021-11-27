# sum of first n natural n.b using while loop
# own Done by self , 

num=(int(input("Enter the number to where you want your sum to be: \n ")))
p=0
s=0
while p<=num:
    s=s+p
    p = p+1
print("The sum is :",s)
