f=open('poems.txt','r')
a=f.read()
if 'twinkle' in a :

    print("Twinkle is present")
else:
    print("Twinkle is not present ")
f.close