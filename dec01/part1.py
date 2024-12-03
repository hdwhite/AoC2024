#Starting late because of a late Thanksgiving vacation, but here we are
leftlist = []
rightlist = []
with open ("part1.txt") as file:
    for line in file:
        splitline = line.split()
        leftlist.append(int(splitline[0]))
        rightlist.append(int(splitline[1]))
leftlist.sort()
rightlist.sort()

distance = 0
for i in range(len(leftlist)):
    distance = distance + abs(leftlist[i] - rightlist[i])
print(distance)
