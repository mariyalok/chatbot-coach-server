
import simplejson as json
data_dict = {} #dict
tempList=[] #Temporary lists where all the data will be saved in the txt file.

def generatePrimaryResponse(month,day): # Mariya & Antonio
    
    if month in data_dict:# If the month exists in the dict it checks if the day is in it too.
        if day in data_dict[month]:
            pass # If a day exsists in the dict it skips it.
        else:
            data_dict[month] = {str(day):0} #If not it adds it and adds hours as 0.
            
    else:
        data_dict[month] = {str(day):0} # If not, it appends it as a key to the dict, the variable day as a key to the value of month and hours as a value of day where it is initialized as 0.
        
        
    tempList.append(month) #Adds the month to the list to write it in the txt file.
    tempList.append(str(day)) #Adds the day to the list to write it in the txt file.
    hour= input("How many hours did you work on that day?")#Joao
    return generateSecondaryResponse(hour)#Joao
    depth += 1
    

def generateSecondaryResponse(hour):#Joao
    data_dict[tempList[0]][tempList[1]] += hour #Put the data(hours) in position data[0][1]
    depth = 0
    tempList.clear() #To cleat the tempList created
    
#Joao
f=open('log.txt','w') # Opens the file,converts the list into a json string, writes on it and closes it
f.write(json.dumps(data_dict))
f.close()





f=open('log.txt','r')# Opens the file, converts the string back into list, reads it, prints it and closes it.

print(json.loads(f.read()))

f.close()
