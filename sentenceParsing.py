"""Sentence Parsing code"""

#Defining of lists, strength & conditioning.

conditioningList = ['treadmill','bike','cross trainer','rowing machine','skipping']

strengthList = ['core','back','shoulder','arm','glute','calve','quadracep','chest','deltoid','delt','ab','abdominal','lat','oblique']


#~~~~~~~~~~# identification of input #~~~~~~~~~~#

keywords = {}

def matchCategory(word):
    """User string is input, string searched for specific words, outputs categories words associated with"""

    if word[-1] == "s":
        for x in conditioningList:      #removes plural 's' from input
            if word[0:-2] == x:
                return "Cardio"

        for x in strengthList:
            if word[0:-2] == x:
                return "Strength"

    else:
        for x in conditioningList:      #no plural then it is returned anyway
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
        if matchCategory(word) in keyWords:
            addKeyWords(matchCategory(word), word)
        else:
            setKeyWords(matchCategory(word), word)
    return keyWords
        
def getCardioList():
    return getKeyWords('Cardio')

def getStrengthList():
    return getKeyWords('Strength')

def clearKeyWords():
    keyWords = {}

def setKeyWords(key, value):
    keyWords[key] = [value]
    
def addKeyWords(key, value):
    keyWords[key].append(value)
    
def getKeyWords():
    return keyWords

def getKeyWords(key):
    return keyWords(key)

            