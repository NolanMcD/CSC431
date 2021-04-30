fileName = input("Enter file name: ")
file = open(fileName)
count = 0
thedict = {}
statList = []
listOfDicts = []
for x in file:
    y = x.split()
    if count == 0:
        for title in y:
            statList.append(title)
    else:
    #print(len(y))
    #print(len(statList))
        thedict[statList[0]] = (y[0] + " " + y[1])
        for num in range(1, len(statList)):
            thedict[statList[num]] = y[num + 1]
        copyDict = thedict.copy()
        listOfDicts.append(copyDict)
    count = count + 1

page = open("yourStats.txt", "w")
statKeys = thedict.keys()
for key in statKeys:
    page.write(key + "     ")
page.write("\n")
for dicts in listOfDicts:
    statValues = dicts.values()
    for val in statValues:
        page.write(val + "     ")
    page.write("\n")
    

    
    
    