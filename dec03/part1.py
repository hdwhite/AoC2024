#Finally am doing it on the correct day
import re

with open("part1.txt") as file:
    fileString = "do()" + file.read() + "don't()"

#Regex is fun!
#Search for "mul(###,###)" snippits and compute!
multList = re.findall("mul\((\d{1,3}),(\d{1,3})\)", fileString)

productSum = 0
for curTuple in multList:
    productSum += int(curTuple[0]) * int(curTuple[1])
print(productSum)
