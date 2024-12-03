#Using a frequency dictionary here, since that way we don't have to sort
#and therefore we can do this in O(n) time
leftlist = {}
rightlist = {}
with open ("part1.txt") as file:
    for line in file:
        splitline = line.split()
        leftnum = int(splitline[0])
        rightnum = int(splitline[1])
        leftlist[leftnum] = leftlist[leftnum] + 1 if leftnum in leftlist else 1
        rightlist[rightnum] = rightlist[rightnum] + 1 if rightnum in rightlist else 1

similarity = 0
for curnum in leftlist:
    if curnum in rightlist:
        similarity = similarity + curnum * leftlist[curnum] * rightlist[curnum]

print(similarity)
