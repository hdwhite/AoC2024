import math

def insert_score(x, y, r, val):
    if maze[y][x] == '#':
        return
    if newscores[y][x][r] > val:
        newscores[y][x][r] = val

with open("part1.txt") as file:
    maze = file.readlines()

for y in range(len(maze)):
    if 'S' in maze[y]:
        x = maze[y].index('S')
        break

for endy in range(len(maze)):
    if 'E' in maze[endy]:
        endx = maze[endy].index('E')
        break

scores = [[[math.inf, math.inf, math.inf, math.inf] for i in maze[0]] for j in maze]
scores[y][x][3] = 0
newscores = []
while True:
    newscores = [[j[:] for j in i] for i in scores]
    for y in range(len(scores)):
        for x in range(len(scores[y])):
            if maze[y][x] == '#' or maze[y][x] == '\n':
                continue
            for r in range(-1, 3):
                if r == -1:
                    dx, dy = 1, 0
                elif r == 0:
                    dx, dy = 0, 1
                elif r == 1:
                    dx, dy = -1, 0
                else:
                    dx, dy = 0, -1
                curScore = scores[y][x][r]
                insert_score(x + dx, y + dy, r, curScore + 1)
                insert_score(x, y, r - 1, curScore + 1000)
                insert_score(x, y, r + 1, curScore + 1000)
    if newscores == scores:
        break
    scores = newscores
minScore = min(scores[endy][endx])
print(minScore)

for y in range(len(scores)):
    for x in range(len(scores[y])):
        for r in range(4):
            if maze[y][x] == '#' or maze[y][x] == '\n':
                scores[y][x][r] = -math.inf
            if scores[y][x][r] > minScore:
                scores[y][x][r] = -math.inf

hasChanged = True
while hasChanged:
    hasChanged = False
    for y in range(len(scores)):
        for x in range(len(scores[y])):
            if (scores[y][x][0] > 0 and
                scores[y][x][0] > scores[y+1][x][0] and
                scores[y][x][0] > scores[y][x][1] - 1000 and
                scores[y][x][0] > scores[y][x][3] - 1000 and
                maze[y][x] != "E"):
                scores[y][x][0] = -math.inf
                hasChanged = True
            if (scores[y][x][1] > 0 and
                scores[y][x][1] > scores[y][x-1][1] and
                scores[y][x][1] > scores[y][x][0] - 1000 and
                scores[y][x][1] > scores[y][x][2] - 1000 and
                maze[y][x] != "E"):
                scores[y][x][1] = -math.inf
                hasChanged = True
            if (scores[y][x][2] > 0 and
                scores[y][x][2] > scores[y-1][x][2] and
                scores[y][x][2] > scores[y][x][1] - 1000 and
                scores[y][x][2] > scores[y][x][3] - 1000 and
                maze[y][x] != "E"):
                scores[y][x][2] = -math.inf
                hasChanged = True
            if (scores[y][x][3] > 0 and
                scores[y][x][3] > scores[y][x+1][3] and
                scores[y][x][3] > scores[y][x][0] - 1000 and
                scores[y][x][3] > scores[y][x][2] - 1000 and
                maze[y][x] != "E"):
                scores[y][x][3] = -math.inf
                hasChanged = True

numVisited = 0
for row in scores:
    output = ""
    for col in row:
        if max(col) >= 0:
            numVisited += 1
            output += "O"
        else:
            output += "."
    print(output[:-1])
print(numVisited)
