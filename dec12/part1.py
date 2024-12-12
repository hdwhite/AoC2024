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
            newPerimeter += 1
    return (newArea, newPerimeter)

plot = []
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
        (a, p) = findRegion((x, y))
        total += a * p

print(total)
