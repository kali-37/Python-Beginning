def split_string(string, word):
    newstr=string.replace(word, "") # .replace will help to replace the given word to desired own

    return newstr.strip() # yeha hamle return newstr matra gareyako vaye teha bata subash replace hunthyo
    # tara newstr.strip use gareaxi paxi aagadi ko rw paxi ko space hataunxa 

word="subash is good boy"
n=split_string(word,"subash")
print(n)