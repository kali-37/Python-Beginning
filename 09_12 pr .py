import os 
# paile vayeako appex.txt ko name change garnu paryo aarko ma copy garera delete garne method

with open("appex.txt",'r') as f:
    fnew1=f.read()
with open("appex by python.txt","w") as f:
    fnew2=f.write(fnew1)
os.remove("appex.txt")