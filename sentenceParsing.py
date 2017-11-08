"""Sentence Parsing code"""

#Defining of lists and dictionaries, strength & conditioning.

highList = ['treadmill','bike','cross trainer','rowing machine']
medList = ['treadmill','bike','cross trainer','rowing machine']
lowList = ['treadmill','bike','cross trainer']
intervalList = ['bike','cross trainer','rowing machine']

cardioDictionary = {'high intensity':highList,'medium intensity':medList,'low intensity':lowList,'interval training':intervalList}




staticList = ['core','back','shoulders','arms','glutes','calves','quadraceps','chest']
explosiveList = ['core','back','shoulders','arms','glutes','calves','quadraceps','chest']
dynamicList = ['core','back','shoulders','arms','glutes','calves','quadraceps','chest']
enduranceList = ['core','back','shoulders','arms','glutes','calves','quadraceps','chest']

strengthDictionary = {'static':staticList,'explosive':explosiveList,'dynamic':dynamicList,'endurance':enduranceList}




globalDictionary = {'cardio':cardioDictionary,'strength':strengthList}



#~~~~~~~~~~# identification of input #~~~~~~~~~~#


#Cardio identification

if 'cardio' in Input:
    print("What type of Cardiovascular training would you like to do, your options are:\n ")
    print("High intensity training\n ")
    print("Medium intensity training\n ")   
    print("Low intensity training\n ")
    print("interval training\n ")
if ('cardio' and 'high intensity') or 