import re

size = (101, 103)
halfway = ((size[0] - 1)/2, (size[1] - 1)/2)
robots = []
with open("part1.txt") as file:
    for line in file:
        robots.append(re.findall("=(\d+),(\d+).+=(-?\d+),(-?\d+)", line)[0])

quadtotals = [0, 0, 0, 0]
for curbot in robots:
    finalx = (int(curbot[0]) + 100*int(curbot[2])) % size[0]
    finaly = (int(curbot[1]) + 100*int(curbot[3])) % size[1]
    if finalx < halfway[0] and finaly < halfway[1]:
        quadtotals[0] += 1
    elif finalx < halfway[0] and finaly > halfway[1]:
        quadtotals[1] += 1
    elif finalx > halfway[0] and finaly < halfway[1]:
        quadtotals[2] += 1
    elif finalx > halfway[0] and finaly > halfway[1]:
        quadtotals[3] += 1
print(quadtotals[0] * quadtotals[1] * quadtotals[2] * quadtotals[3])
