# functions is used to call one statment many times and helps to disposal of any code calling with proper as qbqsics
# when , code becomes bigger and bigger it becomes difficult to run code at, that time fuctions helps to make easy.
def greet(name):
    print("Namaste, "+ name)

greet("subash")
greet("shyam")
greet("Harry ")

# yeha, aaba hamle jaile greet lekham ni taba teasle teha deyako statment leyare function ma jamxa rw kam garera  value return pane garxa.
# yeha greet hamle deyame so it's user defined functions '
# where as len(), range(), print() are some built in functions in python 

def mysum(a,b):
    print (a+b)

a=5
b=7
mysum(a,b)



a-48
b=488

mysum(a,b)

def greeti(name):
    gr="hello"+name 
    return gr  # or code can be simply return "hello"+ name without gr


a=greeti(" freak") # a, will now contain hello freak
print(a)

def greetii(name="stranger"): # yeha stranger is default  parameter if , user dosen't define any paremeter than stranger will be used automatically.
    print("hello "+name)


greetii("unique") # yeha, unique deyako vayera hello unique print garxa vane , 
greetii() # yeha kehe deyako xaina name ma so if there default parameter then it prints the default one
# so , hello stranger print huncha