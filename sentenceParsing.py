


highList = ['treadmill','bike','cross trainer','rowing machine']
medList = ['treadmill','bike','cross trainer','rowing machine']
lowList = ['treadmill','bike','cross trainer']
intervalList = ['bike','cross trainer','rowing machine']

cardioDictionary = {'high intensity': highList,'medium intensity':medList,'low intensity':lowList,'interval training':intervalList}



definitionList = ['muscular definition','vascular definition']
sizeList = []
shapeList = []

aestheticsList = [definition, size, shape]



staticList = []
explosiveList = []
dynamicList = []

strengthList = [static, explosive, dynamic]



globalDictionary = {'cardio':cardioDictionary, 'aesthetics':aestheticsList, 'strength':strengthList}


for target in cardioList:
    print(target)
    for x in target:
        print(x)
        if 'head' in x:
            print("good")