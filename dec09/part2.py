#Since we move files wholesale, it makes sense to keep them grouped and store
#their position, as well as the position of the gaps. We can also delete gaps
#of length 0
with open("part1.txt") as file:
    inputStr = file.readline()

vals = []
gaps =  []
index = 0
for i in range(len(inputStr) - 1):
    curLength = int(inputStr[i])
    if i % 2 == 0:
        vals.append((i/2, index, curLength))
    else:
        gaps.append((index, curLength))
    index += curLength

for b in reversed(range(len(vals))):
    length = vals[b][2]
    for g in range(len(gaps)):
        if gaps[g][0] > vals[b][1]:
            break
        if gaps[g][1] >= length:
            vals[b] = (vals[b][0], gaps[g][0], length)
            gaps[g] = (gaps[g][0] + length, gaps[g][1] - length)
            if gaps[g][1] == 0:
                gaps.pop(g)
            break

total = 0
for file in vals:
    total += file[0] * file[2] * (2 * file[1] + file[2] - 1) / 2
print(total)
