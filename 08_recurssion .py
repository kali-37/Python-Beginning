# recurssion calls by itself where function is to be called 
# recursion calls by itself directly using mathematical formulae

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1) 
a=int(input("Enter a n.b to calcualte factorial : \n"))

print(factorial(a))


