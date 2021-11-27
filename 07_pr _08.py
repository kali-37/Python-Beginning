# programme to print stars in given deduced format  . The programme is self made.
'''
*
**
***
'''

for i in range (4):
    # first, value of i is 0 then 1,2,3
    print("*"*i)

# Again, another format and let, make the below pyramid size as user want:


num=int(input("Enter the height of pyramid to be formed remember the pyramid shape goes: \n"))
z=num
y=1
for i in range(1,num):
    print(" "*z+"*"*y)
    y=y+2
    z=z-1


    