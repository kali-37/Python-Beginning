# Programme to write if a student is pass or fail and percentage secuerd if passed

sub1=int(input("Enter the marks secured in first subject : \n"))
sub2=int(input("Enter the marks secured in second subject : \n"))
sub3=int(input("Enter the marks secured in third subject : \n"))

f2=(sub1+sub2+sub3)/3
if (sub1 or sub2 or sub3 )<33 :
    print( "You are fail due to less than 33 marks in one of the three subjects")
elif int(f2) < 40:
    print("You are fail due to percentile less than 40% i.e :",(f2),"%")
else:
    print("Your are passed with  :",(f2),"%")
