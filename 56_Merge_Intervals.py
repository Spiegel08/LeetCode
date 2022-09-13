
intervals = [[1,3],[2,6],[8,10],[15,18],[17,24]]

listOfSets = [set(range(intervals[i][0], intervals[i][1] + 1)) for i in range(len(intervals))]

theList = []

for i in range(len(listOfSets)):
    for j in range(i+1, len(listOfSets)):
        if min(listOfSets[i]) in listOfSets[j] or max(listOfSets[i]) in listOfSets[j]:
            print(min(listOfSets[i]), max(listOfSets[i]), listOfSets[j])
            theList.append(listOfSets[i] | listOfSets[j])
        else:
            theList.append(listOfSets[j])


s = set(theList)

[{1, 2, 3}, {2, 3, 4, 5, 6}, {8, 9, 10}, {16, 17, 18, 15}]

print(listOfSets)

print(theList)

print(s)
