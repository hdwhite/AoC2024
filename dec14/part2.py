import re

size = (101, 103)
halfway = ((size[0] - 1)/2, (size[1] - 1)/2)
robots = []
with open("part1.txt") as file:
    for line in file:
        robots.append(re.findall("=(\d+),(\d+).+=(-?\d+),(-?\d+)", line)[0])

for i in range(101*103):
    #After manually looking at a bunch, it seemed like 23 mod 101 and 2 mod 103
    #had interesting patterns, so let's try to combine them
    if i % 101 != 23 or i % 103 != 2:
        continue
    positions = [[0 for x in range(size[0])] for y in range(size[1])]
    for curbot in robots:
        x = (int(curbot[0]) + i*int(curbot[2])) % size[0]
        y = (int(curbot[1]) + i*int(curbot[3])) % size[1]
        positions[y][x] += 1
    print(i)
    for row in positions:
        output = ""
        for col in row:
            output += ' ' if col == 0 else str(col)
        print(output)
