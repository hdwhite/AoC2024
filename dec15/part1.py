room = []
x, y = 0, 0
with open("part1.txt") as file:
    for line in file:
        if len(line) < 2:
            break
        if '@' in line:
            x = line.index('@')
        if x == 0:
            y += 1
        room.append([c for c in line.rstrip('\n')])

    for line in file:
        for char in line:
            if char == '<':
                dx, dy = -1, 0
            elif char == '^':
                dx, dy = 0, -1
            elif char == '>':
                dx, dy = 1, 0
            elif char == 'v':
                dx, dy = 0, 1
            else:
                continue
            
            i = 1
            while room[y + i*dy][x + i*dx] == 'O':
                i += 1
            if room[y + i*dy][x + i*dx] == '#':
                continue
            if i > 1:
                room[y + i*dy][x + i*dx] = 'O'
            room[y + dy][x + dx] = '@'
            room[y][x] = '.'
            x += dx
            y += dy

for j in room:
    print(''.join(j))
total = 0
for j in range(len(room)):
    for i in range(len(room[j])):
        if room[j][i] == 'O':
            total += 100*j + i
print(total)
