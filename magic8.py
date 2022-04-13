import random
from urllib import response

#?create a magic 8 ball
#!have it pick a random number

'''
Variables
'''

name = ""

while(name == ""):
    name = input('What is your name?')
    if(name == ""):
        print('Put in your name to carry one')
    else:
        print('hello ' + name)

answers = ["tis not so", "ask agian later", "I don't know", "it seems like the odds are in your favor", "Very Well"]

bob = ["yes", "yea", "y", "Yes", "Yea", "Y" , "YES", "YEA", "yEs", "YeS", "yES", "YEs"]
frank = ["Nope", "No", "nope", "no", "NOPE", "NO", "nopE","NopE","nOPE", "NoPE"]

'''
Main code
'''

def Magic8Ball():
    input("Ask a quetion go ahaed:")
    print(random.choice(answers))
    print('I hope that helped!')
    print ('Do you have another question? [Y/N] ')
    reply = input()
    if reply in bob:
        Magic8Ball()
    elif reply in frank:
        exit()
    else:
        print('I apologies, I did not catch that. Please repeat.')

Magic8Ball()