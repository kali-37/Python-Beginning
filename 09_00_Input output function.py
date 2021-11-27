# Reading file in python and remember they are same as, qbasics

#    f=open("prg.txt","r") Here, r represent read.

f=open('prg.txt')  # by default it's "r" , so you don't have to write it.

# data=f.read() 
# print(data)
print("Now I gonna read first few n.b of character assigned by the user.")
a=int(input("Enter character \n",))
print(f.read(a)) # here , f.read(a) means to read upto a characters and print it.
# And , point to be remembered we cannot read the same file twice , that's why i am
# am commenting the the line n.b '7 and 8'

# readline command means to read the line thoroughly ....

print(f.readline()) #  It reads 1st line command 
print(f.readline()) # It reads 2nd line command 
print(f.readline()) # It now reads the third one
print(f.readline()) # And , so on .....
print(f.readline()) # ..............................

f.close


