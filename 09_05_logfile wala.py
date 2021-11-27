# we have to find if python is present in logfile.txt in any alphabetical class ie. upper or lower and locate it's line n.b too 
# where it's present 
# logfile are those which contains detailed information about particular file ,databases and any problem status..
line=True
ln=1
# to search for name python in log file and find it's line number too....
with open("logfile.txt") as f:
    while line:
        line=f.readline()
        print(line)
        if 'python' in line.lower():
                print(f"Python is present in line n.b {ln}")
                line=False
        else:
                print(f"python is not present in line {ln}")
        if line=="":
            line=False
        ln+=1
