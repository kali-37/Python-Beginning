def maximum(num1, num2, num3):
    if (num1>num2):
        if(num1>num3):
            return(num1)
        else:
            return(num3)
    elif(num2>num1):
        if(num2>num3):
            return(num2)
        else:
            return(num3)
    else:
        hdjfds  # yeha, maile hdjfds lekheyae kina vane yo else ma code kaile ni aauna
# so ,yeha j lekhae ni error aauna.

a=int(input())
b=int(input())
c=int(input())
m=maximum(a,b,c)
print("The maximum n.b is :"+str(m)) 
# yeha str(m) lekhnu ko karand As, The maximum n.b is string so, '+' garexapaxi teha string matra jodna milxa so, making 
# m string as str(m)


