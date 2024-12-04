#We look for an A not on the edge, and then we check to see if there's a
#"MMSS" pattern on the adjacent diagonals
with open("part1.txt") as file:
    wordGrid = file.readlines()

xmax = len(wordGrid[0]) - 1
ymax = len(wordGrid)
diagonals = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
word = "MMSS"

total = 4 * (xmax - 2) * (ymax - 2)
for y in range(1, ymax - 1):
    for x in range(1, xmax - 1):
        if wordGrid[y][x] != "A":
            total -= 4
            continue
        for i in range(len(diagonals)):
            for j in range(len(word)):
                curx = x + diagonals[i-j][0]
                cury = y + diagonals[i-j][1]
                if wordGrid[cury][curx] != word[j]:
                    total -= 1
                    break

print(total)
