letter=''' Dear <Name>, 
I am happy to announce that you are selected on 
coding competion.
 Have a great day
 Your regards , 
 Subash Rimal 
 <Date>'''
name=input("Enter your Name \n")
date =input("Enter the date \n")
letter=letter.replace("<Name>",name)
letter=letter.replace("<Date>",date)
print (letter)