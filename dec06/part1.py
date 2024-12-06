with open("part1.txt") as file:
    room = file.readlines()

xmax = len(room[0]) - 1
ymax = len(room)

dx, dy = 0, -1
for y in range(len(room)):
    if '^' in room[y]:
        x = room[y].index('^')
        break

visited = 0
while x >= 0 and x < xmax and y >= 0 and y < ymax:
    newx, newy = x + dx, y + dy
    if newx < 0 or newx >= xmax or newy < 0 or newy >= ymax:
        if room[y][x] != 'X':
            visited += 1
        x, y = newx, newy
    elif room[newy][newx] == '#':
        dx, dy = -1 * dy, dx
    else:
        if room[y][x] != 'X':
            visited += 1
            room[y] = room[y][:x] + 'X' + room[y][x+1:]
        x, y = newx, newy

print(visited)
