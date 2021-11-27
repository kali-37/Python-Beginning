marks=int(input("Enter your marks \n"))

if marks>90:
    grade="Excellent"
elif marks>80:
    grade="Good "
elif marks>70:
    grade="Normal"
elif marks>60:
    grade="Not Bad"
elif marks>40:
    grade="Poor"  

else:
    grade="less than 40 so you're fail. "

print("Your grade is",grade)



