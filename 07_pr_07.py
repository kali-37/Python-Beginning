 # factorial for n=n*(n-1)*(n-2)....1
num=int(input("Enter a n.b for factorial you want to calculate :\n"))
p=1
for i in range(1,num+1):
    p=p*i

print("The factorial of given n.b is :",p)