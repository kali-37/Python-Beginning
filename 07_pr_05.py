
# to identify if the given n.b is prime or not
num=int(input("Enter a n.b : \n"))

prime=True

for i in range(2,num):
    if (num%i)==0: # if on division gives decimal 0 then it's not prime
        prime=False
        break # it will break the line for given if statment and take downard
if prime:
    print("The provided number is prime")
else:
    print("The provided number is not prime")
