
# intervals = [[1,3],[2,6],[8,10],[15,18]]

# intervals = [[1,4],[4,5]]

intervals = [[1,4]]

listOfSets = [set(range(intervals[i][0], intervals[i][1] + 1)) for i in range(len(intervals))]

listOfMergedSets = []

setOfIndices = set()

for i in range(len(listOfSets)):
    for j in range(i+1, len(listOfSets)):
        if min(listOfSets[i]) in listOfSets[j] or max(listOfSets[i]) in listOfSets[j]:
            listOfMergedSets.append((listOfSets[i] | listOfSets[j]))
            setOfIndices |= {i, j}

intervals_output = []
for i in range(len(intervals)):
    if i not in setOfIndices:
        intervals_output.append(intervals[i])

for i in range(len(listOfMergedSets)):
    intervals_output.append([min(listOfMergedSets[i]), max(listOfMergedSets[i])])

print(sorted(intervals_output))
