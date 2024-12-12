#Basically we take the recursion in part 1, and then we check each edge to see
#if there's another edge one over and pointed in the same direction. If so, we
#get to subtract one since they're both counted as the same
def findRegion(coord):
    (letter, visited) = plot[coord[1]][coord[0]]
    if visited:
        return (0, 0)
    plot[coord[1]][coord[0]] = (letter, True)
    newArea, newPerimeter = 1, 0
    deltas = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    for direction in deltas:
        newcoord = (coord[0] + direction[0], coord[1] + direction[1])
        if (newcoord[0] >= 0 and newcoord[0] < xmax
          and newcoord[1] >= 0 and newcoord[1] < ymax
          and letter == plot[newcoord[1]][newcoord[0]][0]):
            (a, p) = findRegion(newcoord)
            newArea += a
            newPerimeter += p
        else:
            edges.append((coord, direction))
            newPerimeter += 1
    return (newArea, newPerimeter)

plot = []
edges = []
with open("part1.txt") as file:
    for line in file:
        plot.append([(x, False) for x in line[:-1]])
xmax, ymax = len(plot[0]), len(plot)

total = 0
for y in range(ymax):
    for x in range(xmax):
        tile = plot[y][x]
        if tile[1]:
            continue
        edges = []
        (a, p) = findRegion((x, y))
        for curEdge in edges:
            if ((curEdge[0][0] + curEdge[1][1], curEdge[0][1] - curEdge[1][0]),
                curEdge[1]) in edges:
                p -= 1
        total += a * p

print(total)
