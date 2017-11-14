"""Sentence Parsing code"""

#Defining of lists, strength & conditioning.

conditioningList = ['treadmill','bike','cross trainer','rowing machine','skipping']

strengthList = ['core','back','shoulder','arm','glute','calve','quadracep','chest','deltoid','delt','ab','abdominal','lat','oblique']


#~~~~~~~~~~# identification of input #~~~~~~~~~~#


keyWords = {}

def matchCategory(word):
    """Users' string is input, string searched for specific words, those words are returned as output"""

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
    """input is output from 'matchCategory' function, input is analysed and sorted into lists based on strengthList & conditioningList"""
    msgList = msg.lower().split()
    for word in msgList:
        if matchCategory(word) in keyWords:
            keyWords[matchCategory(word)].append(word)
        else:
            keyWords[matchCategory(word)] = [word]
            return keyWords
            