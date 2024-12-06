#I'm sure there are much more optimised ways of doing this, as this run took
#several seconds to complete
with open("part1.txt") as file:
    room = file.readlines()

xmax = len(room[0]) - 1
ymax = len(room)

dx, dy = 0, -1
for y in range(ymax):
    if '^' in room[y]:
        x = room[y].index('^')
        break

startx, starty = x, y
while x >= 0 and x < xmax and y >= 0 and y < ymax:
    newx, newy = x + dx, y + dy
    if newx < 0 or newx >= xmax or newy < 0 or newy >= ymax:
        if room[y][x] != 'X':
            room[y] = room[y][:x] + 'X' + room[y][x+1:]
        x, y = newx, newy
    elif room[newy][newx] == '#':
        dx, dy = -1 * dy, dx
    else:
        if room[y][x] != 'X':
            room[y] = room[y][:x] + 'X' + room[y][x+1:]
        x, y = newx, newy

loops = 0
for j in range(ymax):
    for i in range(xmax):
        if room[j][i] != 'X' or (i == startx and j == starty):
            continue
        visited = [[0 for col in range(xmax)] for row in range(ymax)]
        x, y = startx, starty
        dx, dy = 0, -1
        
        while x >= 0 and x < xmax and y >= 0 and y < ymax:
            if visited[y][x] == 2*dx+dy:
                loops += 1
                break
            newx, newy = x + dx, y + dy
            if newx < 0 or newx >= xmax or newy < 0 or newy >= ymax:
                x, y = newx, newy
            elif room[newy][newx] == '#' or (newx == i and newy == j):
                dx, dy = -1 * dy, dx
            else:
                visited[y][x] = 2*dx+dy
                x, y = newx, newy
print(loops)
