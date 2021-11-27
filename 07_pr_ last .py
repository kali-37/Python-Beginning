# The programme to print multiplication table in reverse order.
# using , while loop
n=1
num1=int(input("Enter a n.b for multiplication :\n"))
num2=int(input("Enter a n.b to where the table goes:\n"))
n1=num2
print("Your multiplication table goes in reverse order as :\n")
while n<=n1:
    print((num1),"*",(num2),"=",(num2*num1))
    n=n+1
    num2=num2-1
    