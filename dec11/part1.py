#Works for Part 1 and Part 2
#I'm not sure if caching actually helps that much
#But it saved a ton of time before I realised there was a lot of duplicates
#And that having a frequency list was the way to go
#It took 0.05 seconds to run for Part 2
import math

with open("part1.txt") as file:
    inputStr = file.readline()
stones = {}
for curStone in inputStr[:-1].split():
    stones[int(curStone)] = 1

cachedValues = []
for i in range(10000):
    if i == 0:
        cachedValues.append([1])
    elif i < 10 or (i > 99 and i < 1000):
        cachedValues.append([i * 2024])
    elif i < 100:
        cachedValues.append([int(i / 10), int(i % 10)])
    else:
        cachedValues.append([int(i / 100), int(i % 100)])

for i in range(75):
    newStones = {}
    for curStone, numStones in stones.items():
        if curStone < 10000:
            newVal = cachedValues[curStone]
        else:
            numDigits = len(str(curStone))
            if numDigits % 2 == 0:
                divisor = int(10**(numDigits/2))
                newVal = [int(curStone / divisor), int(curStone % divisor)]
            else:
                shift3 = curStone << 3
                shift4 = shift3 << 1
                shift11 = shift4 << 7
                newVal = [shift11 - (shift3 + shift4)]
        for curVal in newVal:
            if curVal in newStones:
                newStones[curVal] += numStones
            else:
                newStones[curVal] = numStones
    stones = newStones

print(sum(stones.values()))
