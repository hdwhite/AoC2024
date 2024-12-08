curLine = []

def testEquation(val, index, target):
    if val > target:
        return False
    if index == len(curLine) - 1:
        return (val + curLine[index] == target
             or val * curLine[index] == target
             or int(str(val) + str(curLine[index])) == target)
    return (testEquation(val + curLine[index], index + 1, target)
         or testEquation(val * curLine[index], index + 1, target)
         or testEquation(int(str(val) + str(curLine[index])), index + 1, target))

totalValid = 0
with open("part1.txt") as file:
    for line in file:
        [target, numberStr] = line.split(": ")
        target = int(target)
        curLine = list(map(int, numberStr.split()))
        if testEquation(curLine[0], 1, target):
            totalValid += target

print(totalValid)