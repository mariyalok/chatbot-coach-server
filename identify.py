# Take user input
msg = input("Type a message: ")

# Strength related exercises
#
strList = ["Arms","Legs"]

# Cardio related exercises
#
cardioList = ["Tread","Row"]

# Dict to deal with Categories and Words
keyWords = {}

# Array of words from user input
msgList = msg.split()

# Input: 	Word		-> String
# Output:	Category	-> String
#
def matchCategory(word):
# Check if word matches any in Cardio List
	for x in cardioList:
		if word == x:
			return "Cardio"

# Check if word matches any in Strength List
	for x in strList:
		if word == x:
			return "Strength"
	return "N/a"

# Run through all words user has input 
# Add to dict under categories
#
for word in msgList:
	if matchCategory(word) in keyWords:
		# Add word to dict under category
		#
		keyWords[matchCategory(word)].append(word)
	else:
		# Category doesnt exist so create it and assign first word
		#
		keyWords[matchCategory(word)] = [word]

print(keyWords)
