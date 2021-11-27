def game():
    return 354

score=game()
with open("highscore.txt",'r') as f:
    highscore=(f.read())
    if str(highscore)=="": # yeti kehe pani xaina vane we must change highscore to zero 
        highscore=0

if str(score)>highscore: # AS, highscore is in int so we have to make score to str too.
    with open("highscore.txt", 'w') as f:
        
        f.write(str(score))