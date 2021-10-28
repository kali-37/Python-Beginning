a="345" # a is now as a string
print(type(a))
''' yeha comment ko thau ma if we had typed print(a+3) then syntax would have been wrong bcz
                                  yeha we cant add int to strg'''

a=int(a) # python will try to make string to integer , if it was a as hsk then it could,nt coz its alphabet
print(type(a))
print(a+3)
