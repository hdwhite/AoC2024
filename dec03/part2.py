import re

with open("part1.txt") as file:
    fileString = "do()" + file.read() + "don't()"

#Regex is still fun!
#Split the program into do/don't blocks
doStrings = re.findall("do\(\)(.*?)don't\(\)", fileString, re.S)

productSum = 0
for curString in doStrings:
    #Now look for "mul(###,###)" and compute
    multList = re.findall("mul\((\d{1,3}),(\d{1,3})\)", curString)
    for curTuple in multList:
        productSum += int(curTuple[0]) * int(curTuple[1])
print(productSum)
