# write a programme to find the greatest n.b entered by the user
num1=int(input("Enter the 1 n.b : \n"))
num2=int(input("Enter the 2 n.b : \n"))
num3=int(input("Enter the 3 n.b : \n"))
num4=int(input("Enter the 4 n.b : \n"))

if(num1>num2):
    f1=num1
else:
    f1=num2
if(num3>num4):
    f2=num3
else:
    f2=num4
if f1>f2:
    print("The greatest n.b is : ",str(f1))

    
else:
    print("The greatest n.b is ",str(f2))

