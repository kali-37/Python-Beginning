
import colorama # for color change
from colorama import Fore 



print(Fore.LIGHTMAGENTA_EX+"Enter the table you want as follow levels:\n")
# The above text will be written in lightmagenta_ex colors

a=int(input(" Enter the n.b of tables you want:grade less than 2,3,4,...10th , 11th , .... Ramanujan level: \n"))
c=int(input("Enter the times the tables should go,  for like up to 10 basically:\n"))

def tabule():
    for i in range (0,c+1):
        print(f"{b}*{i}={b*i}")

        with open("Tables for desired grade planted by the user.txt",'a') as f:
            f.write((f"{b}*{i}={b*i}\n"))

p=0
with open("Tables for desired grade planted by the user.txt",'w') as f:
    f.close
for b in range(0,a+1):
    with open("Tables for desired grade planted by the user.txt",'a') as f:    
        f.write(f"\nThe multiplication table of {p} is :\n\n")
    tabule()
    p=p+1

