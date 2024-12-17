def combo(op):
    if op < 4:
        return op
    if op == 4:
        return a
    if op == 5:
        return b
    if op == 6:
        return c

with open("part1.txt") as file:
    a = int(file.readline()[12:-1])
    b = int(file.readline()[12:-1])
    c = int(file.readline()[12:-1])
    file.readline()
    instructions = list(map(int, file.readline()[9:-1].split(',')))

pointer = 0
outlist = []
while pointer < len(instructions):
    print(a, b, c, pointer)
    if instructions[pointer] == 0:
        a = a >> combo(instructions[pointer+1])
    elif instructions[pointer] == 1:
        b = b ^ instructions[pointer+1]
    elif instructions[pointer] == 2:
        b = combo(instructions[pointer+1]) & 7
    elif instructions[pointer] == 3:
        if a != 0:
            pointer = instructions[pointer + 1] - 2
    elif instructions[pointer] == 4:
        b = b ^ c
    elif instructions[pointer] == 5:
        outlist.append(str(combo(instructions[pointer + 1]) & 7))
    elif instructions[pointer] == 6:
        b = a >> combo(instructions[pointer+1])
    elif instructions[pointer] == 7:
        c = a >> combo(instructions[pointer+1])
    pointer += 2
print(','.join(outlist))
