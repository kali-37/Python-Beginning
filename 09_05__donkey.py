
# you can check the code replacing:
#  "#######" to 'doneky' and "balatkar" to "chamatkar"

# for multiple words
words=["ma_sale","kaddu","aape","sale","donkey","balatkar"]


with open("donkey.txt","r") as f:
    worp=f.read()
for word in words:
     # here for i in words jasti ho jaha word will have words value serially.

    worp=worp.replace(word,"#$#%@!$#")
    print(worp)
    with open("donkey.txt",'w') as f:
        f.write(worp)


     