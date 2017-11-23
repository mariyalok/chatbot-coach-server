
import simplejson as json
data_dict = {} #dict
tempList=[] #Temporary lists where all the data will be saved in the txt file. Listas temporarias onde se vai guardar os dados no ficheiro
def generatePrimaryResponse(month,day): # Mariya & Antonio
    
    if month in data_dict:# if the month is already in the dict it checks if the day is in it too
        if day in data_dict[month]:
            pass # if there is already a day in the dict it skips it. se ja existe no dicionario entao passa a frente
        else:
            data_dict[month] = {str(day):0} #If not it adds it and adds hours as 0. se o dia nao esta no dicionario , entao acrescenta
    else:
        data_dict[month] = {str(day):0} # if not, it adds it, ------------
        #if not in dict so append the variable month as a key and variable day as value is a key day abd 0 as hours as a value
        
    tempList.append(month) #Adds the month to the list to write it in the txt file. adiciona o mes a lista para escrever no ficheiro txt
    tempList.append(str(day)) #Adds the day to the lsit to write it in the txt file. adiciona o dia a lista para escrever no ficheiro txt
    hour= input("How many hours did you work on that day?")#Joao
    return generateSecondaryResponse(hour)#Joao
    depth += 1

def generateSecondaryResponse(hour):#Joao
    data_dict[tempList[0]][tempList[1]] += hour # put the data(hours) in position data[0][1]
    depth = 0
    tempList.clear() #clean the tempList created
    
    #print("jjj")
    
   
    

'''

generatePrimaryResponse("January",23)
generateSecondaryResponse(3)
print(data_dict)
generatePrimaryResponse("Feburary",9)
generateSecondaryResponse(6)
print(data_dict)
generatePrimaryResponse("January",23)
generateSecondaryResponse(5)
print(data_dict)

'''

#Joao
f=open('log.txt','w') # Opens the file,converts the list into a json string, writes on it and closes it
f.write(json.dumps(data_dict))
f.closed





f=open('log.txt','r')# Opens the file, converts the string back into list, reads it, prints it and closes it.

print(json.loads(f.read()))

f.closed

    
    