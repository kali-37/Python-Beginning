import time # time module is inputed
a=0
for i in range(9):
        f=open(f"{a}.txt",'w')
        print(f"{a}.txt ")
        f.write(f"{a}.txt") # tyo file ma teasaiko name lekhene...
        a=a+1
        f.close() # yeha close garena vane last wala write gareyako file background ma run vaye rakheyako huncha
                  # So, it's necessary to close bcoz tala delete garda kheari file 8.txt is opened in another process vanxa
                 
# Above programme helps to make new files as 0.txt,1.txt,2.txt and so on....


time.sleep(5) # delay for 5 seconds and for 5 second look after if those files are made bcoz after 5 sec the below commands are going to delete it.

import os # os module is imported for os ko kehe file add subs and edit garna lai
a=0
for i in range(9):

    if os.path.exists(f"{a}.txt"):
        print(f"{a}.txt found")
        os.remove(f"{a}.txt") # helps to remove {a}.txt file 
        print(f"The file is '{a}.txt' is removed")
    else:
        print("The file does not exist")
    a=a+1
f.close()
