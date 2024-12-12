def findPaths(coord, height):
    if height == 9:
        return 1
    numPaths = 0
    deltas = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    for direction in deltas:
        newcoord = (coord[0] + direction[0], coord[1] + direction[1])
        if (newcoord[0] >= 0 and newcoord[0] < xmax
          and newcoord[1] >= 0 and newcoord[1] < ymax
          and heights[newcoord[1]][newcoord[0]] == height + 1):
            if newcoord in visited:
                numPaths += visited[newcoord]
            else:
                numPaths += findPaths(newcoord, height + 1)
    visited[coord] = numPaths
    return numPaths

visited = {}
heights = []
with open("part1.txt") as file:
    for line in file:
        heights.append(list(map(int, list(line[:-1]))))
xmax, ymax = len(heights[0]), len(heights[1])

numPaths = 0
for starty in range(ymax):
    for startx in range(xmax):
        if heights[starty][startx] > 0:
            continue
        visited = {}
        numPaths += findPaths((startx, starty), 0)
print(numPaths)
