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
        for num in range(0, len(statList)):
            thedict[statList[num]] = y[num]
        copyDict = thedict.copy()
        listOfDicts.append(copyDict)
    count = count + 1
#print("Team     SB     CS     SB%")
for mydict in listOfDicts:
    sbper = int(mydict["SB"]) / (int(mydict["SB"]) + int(mydict["CS"]))
    #print(mydict["Team"] + "     " + mydict["SB"] + "     " + mydict["CS"] + "     ", end = " ")
    if sbper > .82:
        print(mydict["Team"])
        print(sbper)
        #print("^^")
    #else:
       # print(sbper)