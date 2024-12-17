def move(x, y, dx, dy):
    if newroom[y + dy][x + dx] == '#':
        return False
    if newroom[y + dy][x + dx] == '.':
        newroom[y + dy][x + dx] = newroom[y][x]
        newroom[y][x] = '.'
        return True

    if dy == 0:
        if move(x + dx, y + dy, dx, dy):
            newroom[y + dy][x + dx] = newroom[y][x]
            newroom[y][x] = '.'
            return True
        return False

    over = 1 if newroom[y + dy][x + dx] == '[' else -1
    if move(x + dx, y + dy, dx, dy) and move (x + dx + over, y + dy, dx, dy):
        newroom[y + dy][x + dx] = newroom[y][x]
        newroom[y][x] = '.'
        return True
    return False

room = []
newroom = []
x, y = 0, 0
with open("part1.txt") as file:
    for line in file:
        room.append([])
        if len(line) < 2:
            break
        for c in line:
            if c == '#':
                room[-1] += ['#', '#']
            elif c == 'O':
                room[-1] += ['[', ']']
            elif c == '.':
                room[-1] += ['.', '.']
            elif c == '@':
                room[-1] += ['@', '.']
                x = line.index(c) * 2
        if x == 0:
            y += 1

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
            
            newroom = [i[:] for i in room]
            if move(x, y, dx, dy):
                room = newroom
                x += dx
                y += dy

for j in room:
    print(''.join(j))
total = 0
for j in range(len(room)):
    for i in range(len(room[j])):
        if room[j][i] == '[':
            total += 100*j + i
print(total)
