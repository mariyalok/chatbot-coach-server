"""Sentence Parsing code"""

#Defining of lists, strength & conditioning.

conditioningList = ['treadmill','bike','cross trainer','rowing machine','skipping']

strengthList = ['core','back','shoulder','arm','glute','calve','quadracep','chest','deltoid','delt','ab','abdominal','lat','oblique']


#~~~~~~~~~~# identification of input #~~~~~~~~~~#

keyWords = {}

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

#~~~~~functions for chris' side~~~~~#

def getCardioList():
    return getKeyWords('Cardio')
                                       #returns words from user input string based on cateogry
def getStrengthList():
    return getKeyWords('Strength')

def clearKeyWords():                   #resets list from previous entries
    keyWords = {}

def setKeyWords(key, value):           
    keyWords[key] = [value]
                                       #assigns keys and values to words in defined lists and adds them to a dictionary
def addKeyWords(key, value):
    keyWords[key].append(value)
    
def getKeyWords():
    return keyWords
                                       #polymorphic function, can be returned
def getKeyWords(key):
    return keyWords[key]

            