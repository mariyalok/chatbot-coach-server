"""Sentence Parsing code"""

#Defining of lists, strength & conditioning.

conditioningList = ['treadmill','bike','cross trainer','rowing machine','skipping','eliptical','step machine']

strengthList = ['core','back','shoulder','arm','tricep','bicep','glute','calve','calf','quadracep','quad','chest','deltoid','delt','ab','abdominal','lat','oblique','trap','trapezium']

#~~~~~~~~~~# identification of greetings #~~~~~~~~~~#

greetingList = ['hi','hello','sup','hey','chao','bonjour','whad up']

def parseGreeting(msg):
    for greeting in greetingList:
        if greeting in msg:
            return True
        else:
            return False

#~~~~~~~~~~# identification of input of exercises #~~~~~~~~~~#

keyWords = {}

def matchCategory(word):
    """User string is input, string searched for specific words, outputs categories words associated with"""

    if word[-1] == "s":
        for x in conditioningList:      #removes plural 's' from input
            if word[0:-1]== x:
                return "Cardio"

        for x in strengthList:
            if word[0:-1]== x:
                return "Strength"

    else:
        for x in conditioningList:      #no plural then it is returned to either strength or conditioning
            if word == x:
                return "Cardio"

        for x in strengthList:
            if word == x:
                return "Strength"
    return "N/a"

def identifyOutput(msg):
    """input is string, output is dictionary of words associated with categories"""
    clearKeyWords()
    msgList = msg.lower().split()
    for word in msgList:
        if matchCategory(word) in keyWords:              #adds the muscle group/training machine to a list
            addKeyWords(matchCategory(word), word)       # if it is in either strengthList or conditioningList
        else:
            setKeyWords(matchCategory(word), word)
    return keyWords

def returnOutput():
    output = []
    if "Cardio" in keyWords:                             #Gives lists induvidually as output for transfer to Replying.py
        output = output + getCardioList()
    if "Strength" in keyWords:
        output = output + getStrengthList()
    return parseGreeting(),

#~~~~~functions for chris' side~~~~~#

def getCardioList():
    return getKeyWord('Cardio')
                                       #returns words from user input string based on cateogry
def getStrengthList():
    return getKeyWord('Strength')

def clearKeyWords():                   #resets list from previous entries
    keyWords.clear()

def setKeyWords(key, value):
    keyWords[key] = [value]
                                       #assigns keys and values to words in defined lists and adds them to a dictionary
def addKeyWords(key, value):
    keyWords[key].append(value)

def getKeyWord():
    return keyWords
                                       #polymorphic function, can return all keyWords or specific based key
def getKeyWord(key):
    return keyWords[key]
