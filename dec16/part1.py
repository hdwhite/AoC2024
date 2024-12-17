import math

def insert_score(x, y, r, val):
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
    print(scores[endy][endx])
print(min(scores[endy][endx]))
