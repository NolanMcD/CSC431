def wOBA(oneb,twob,threeb,HR,uBB,AB,BB,IBB,SF,HBP):
    return (.67 * uBB + .72 * HBP + .89 * oneb + 1.27 * twob + 1.62 * threeb + 2.1 * HR)/(AB + BB - IBB + SF + HBP)

print("wOBA Calculator")
print("-------------------")
playerName = input("Enter a player: ")

file = open("2020stats.py")
for x in file:
    y = x.split()
    if(playerName == y[0] + " " + y[1]):
        res = wOBA(int(y[7]), int(y[8]), int(y[9]), int(y[10]), (int(y[13]) - int(y[14])), int(y[4]), int(y[13]), int(y[14]), int(y[17]), int(y[16]))
        print(playerName + "'s un league adjusted wOBA is:")
        print(res)
        if len(y) != 24:
            print("Problem with " + y[0] + y[1])
