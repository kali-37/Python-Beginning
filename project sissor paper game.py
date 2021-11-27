# playing sissor, paper , rock game with computer made by own

import random

def referee(comp,you):
    if comp=='s':
        if you=='p':
            return False
        elif you=='s':
            return None
        else:
            return True
    elif comp=='p':
        if you=='r':
            return False
        elif you=='p':
            return None
        else:
            return True
    elif comp=='r':
        if you=='s':   
            return False
        elif you=='r':
            return None
        else:
            return True
    else:
        return None
        

def uservalue():
    if you=='r' or you=='p' or you=='s':
        return True
    else:
        print("\n")
        print("choose among Rock(r) , Paper(p) , Sissors(s)")
        return False


print("computer has chossen :Now your Turn,")
rand=random.randint(1,3)
if rand==1:
    comp='s'
elif rand==2:
    comp='p'
else:
    comp='r'

p=0

while p==0 or p==1:
    you=input("Enter for your turn # Rock(r) , Paper(p) , Sissors(s) :")
    b=uservalue()
    if b:
        print("Done")
        break
    else:
        p=1


if comp=='r':
    com="Rock"
elif comp=='s':
    com="Sissor"
else:
    com="Paper"


if you=='r':
    yo="Rock"
elif you=='s':
    yo="you"
else:
    yo="Paper"

print(" The computer has chosen:",com + " And you have chosen: "+ yo)

    
a=referee(comp,you)

if a:
    print("You Won! ")
elif a==None:
    print("Tie both same ")
else:
    print("Computer wins! ")

