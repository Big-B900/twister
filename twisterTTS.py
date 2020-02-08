import random
from time import sleep
#import pyttsx
from gtts import gTTS
import os


#dictionary
colors = ['Red','Blue','Green','Yellow']
bodyParts = ['Right Foot','Left Foot','Right Hand','Left Hand']

#pyttsx = no bueno
#engine = pyttsx.init()
#engine.say('Hello world')
#engine.runAndWait()


#gTTS
text = "hello world"
language = 'en'

speech = gTTS(text = text, lang = language, slow = False)

speech.save("text.mp3"

os.system("start text.mp3")



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



