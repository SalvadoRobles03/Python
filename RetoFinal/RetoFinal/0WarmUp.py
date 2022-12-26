pokerFile = open(".\PokerFile.txt", 'r')
totalCount = 0

nothingCount = 0
pairCount = 0
threeOfaKindCount = 0
fullHouseCount = 0

for line in pokerFile:
    
    handRank = line.split(",")
    for i in range(len(handRank)):
        totalCount += 1
        if handRank[i] == 0 or handRank[i] == "0\n" or handRank[i] == "0":
            nothingCount += 1
        if handRank[i] == 1 or handRank[i] == "1\n" or handRank[i] == "1":
            pairCount += 1
        if handRank[i] == 3 or handRank[i] == "3\n" or handRank[i] == "3":
            threeOfaKindCount += 1
        if handRank[i] == 6 or handRank[i] == "6\n" or handRank[i] == "6":
            fullHouseCount += 1



print("Total hands in file: " , totalCount)
print("Count of pair hands", nothingCount,pairCount,"\n",threeOfaKindCount,fullHouseCount)
totalCountFP = float(totalCount)

print("Probability:")
print(" of nothingCount:       %5.2f %%." % (100* nothingCount/totalCountFP))
print(" of pairCount:          %5.2f %%." % (100* pairCount/totalCountFP))
print(" of threeOfaKindCount:  %5.2f %%." % (100* threeOfaKindCount/totalCountFP))
print(" of fullHouseCount:     %5.f %%." % (100* fullHouseCount/totalCountFP))

