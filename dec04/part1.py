#I don't like how many nested for loops there are
#But it iterates over each square and each x and y direction
with open("part1.txt") as file:
    wordGrid = file.readlines()

xmax = len(wordGrid[0]) - 1
ymax = len(wordGrid)
word = "XMAS"

total = 9 * xmax * ymax
for y in range(ymax):
    for x in range(xmax):
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                for i in range(len(word)):
                    curx = x + i*dx
                    cury = y + i*dy
                    if curx < 0 or curx >= xmax or cury < 0 or cury >= ymax\
                       or wordGrid[cury][curx] != word[i]:
                        total -= 1
                        break

print(total)
