highList = ['butt', 'head']
medList = ['side', 'inter']
lowList = ['work', 'twat', 'chris']
#intervalList = [high intensity, medium instensity, low intensity]
cardioList = {"high" : highList, "med" : medList, "low" :lowList}

#aestheticsList = [definition, size, shape]
#definitionList = []
#sizeList = []
#shapeList = []


#strengthList = [static, explosive, dynamic]
#staticList = []
#explosiveList = []
#dynamicList = []


for target in cardioList:
    print(target)
    for x in target:
        print(x)
        if 'head' in x:
            print("good")