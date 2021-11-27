#  Spam detector

text=input("Enter every copyable  text from the website you wanna check for spam authentation. \n")
spam=False


if ("Make a Lot of Money" in text):# if text we entered have these sorts of sentences then they will gonna be scam
    spam=True            # And, these sentences may be any where in the text 
elif("buy now "in text):
    spam=True
elif ("Click this " in text):
    spam=True
elif("Subscribe this" in text):
    spam=True
else:
    spam=False
if (spam):
    print("The text is spam ")
else:
    print("This is not spam")
