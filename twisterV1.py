import random
from time import sleep

#dictionary
colors = ['Red','Blue','Green','Yellow']
bodyParts = ['Right Foot','Left Foot','Right Hand','Left Hand']



#user input
print('How many people are playing?\n')
numPlayers = int(input())
i=0

while i<10:
    j=1
    while j<=numPlayers:
        bodyRoll = random.randint(0,3)
        colorRoll = random.randint(0,3)
        outputString = "Player {}: {} on {}".format(j, bodyParts[bodyRoll],colors[colorRoll])
        print(outputString)
        
        j+=1
        sleep(.1)
        input()
    i+=1



