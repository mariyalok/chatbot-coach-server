"""Sentence Parsing code"""

#Defining of lists, strength & conditioning.

conditioningList = ['treadmill','bike','cross trainer','rowing machine','skipping']

strenghtList = ['core','back','shoulders','arms','glutes','calves','quadraceps','chest','deltoids','delts','abs','abdominals','lats','obliques','']


#~~~~~~~~~~# identification of input #~~~~~~~~~~#

msg = input("Type a message: ")

keyWords = {}

msgList = msg.split()

def matchCategory(word):

# Check if word matches any in Lists
    if word[-1] == "s":
        for x in conditioningList:
		if word[0:-2] == x:
			return "Cardio"

	for x in strenghtList:
		if word[0:-2] == x:
			return "Strength"

    else:
	for x in conditioningList:
		if word == x:
			return "Cardio"

	for x in strenghtList:
		if word == x:
			return "Strength"
	return "N/a"

for word in msgList:
	if matchCategory(word) in keyWords:
		keyWords[matchCategory(word)].append(word)
	else:
		keyWords[matchCategory(word)] = [word]

print(keyWords)


