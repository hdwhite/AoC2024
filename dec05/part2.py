#Turns out this was really simple to do, since all I had to do was swap
#the two out-of-order pages and backtrack to the earlier one
pageOrder = {}
total = 0
with open("part1.txt") as file:
    for line in file:
        if len(line) < 2:
            break
        (firstPage, lastPage) = line.split("|")
        if int(firstPage) in pageOrder:
            pageOrder[int(firstPage)].append(int(lastPage))
        else:
            pageOrder[int(firstPage)] = [int(lastPage)]

    for line in file:
        curLine = list(map(int, line.split(",")))
        isValid = True
        i = 1
        while i < len(curLine):
            curPage = int(curLine[i])
            for j in range(i):
                if curPage in pageOrder and int(curLine[j]) in pageOrder[curPage]:
                    isValid = False
                    curLine[i], curLine[j] = curLine[j], curLine[i]
                    i = j
                    break
            i += 1
        if not isValid:
            total += curLine[int(len(curLine) / 2)]
print(total)
