import random

muscle_exercises = {}

def greeting() :
	greeting=["Hi!","Hello!"]
	howAre=["How are you today?","Are you ready to achieve your best?"]
	print(random.choice(greeting))
	print(random.choice(howAre))

def exercisesToDict():
	"""Reads in a file, returns dictionary
	with muscles as key and exercises as 
	values"""
	f=open("exercises.txt","r")
	file_string = f.read()
	file_list = file_string.splitlines()
	for line in file_list:
		temp_list = line.split(",") 
		exercise, muscle = temp_list[0], temp_list[1]
		muscle = muscle[1:] # Remove space at beginning
		if muscle in muscle_exercises:
		# If it exists add to already existing list
			muscle_exercises[muscle].append(exercise)
		else:
		# Create new list and assign first exercise
			muscle_exercises[muscle] = [exercise]

def generateReply(muscle):
        reply = muscle #input("What part of the body would you like to train?")
        found = False
        replyLower = reply.lower()

        for k in muscle_exercises.keys():
                if(replyLower == k):
                        found = True
                        temp_list = []
                        while len(temp_list) < 5:
                                choice = random.choice(muscle_exercises[replyLower])
                                if choice in temp_list:
                                        continue
                                else: 
                                        temp_list.append(choice)
                

                        print("You could try these exercises for {}:".format(reply))

                        for x in temp_list:
                                print ('{}'.format(x))
                                
                        break
##                else:
##                        found = False
                        
        if found == False:
                print("I'm sorry. I do not have any exercises for: {}".format(reply)

