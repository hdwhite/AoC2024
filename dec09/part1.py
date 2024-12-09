#There's definitely ways to do this where you only iterate once, but this still
#does the trick in O(n) time
with open("part1.txt") as file:
    inputStr = file.readline()

file = []
for i in range(len(inputStr) - 1):
    if i % 2 == 0:
        file += [i/2] * int(inputStr[i])
    else:
        file += [None] * int(inputStr[i])

i = 0
while i < len(file):
    if file[i] is not None:
        i += 1
        continue
    if file[-1] is None:
        file.pop()
        continue
    file[i] = file.pop()

total = 0
for i, val in enumerate(file):
    total += i * val
print(total)
