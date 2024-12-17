#I discovered that the output follows a pattern that I could exploit
#The output length is basically equal to the length of a in base 8
#And the nth output value remains constant for 8**n values of a
#So basically we can jump pretty far until we get more and more matches
#Managed to get on the leaderboard (53rd), so I'm happy about it
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
    file.readline()
    startb = int(file.readline()[12:-1])
    startc = int(file.readline()[12:-1])
    file.readline()
    instructions = list(map(int, file.readline()[9:-1].split(',')))

starta = 1 << 3*(len(instructions) - 1)
while True:
    a, b, c = starta, startb, startc
    pointer = 0
    outlist = []
    while pointer < len(instructions):
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
            outlist.append(combo(instructions[pointer + 1]) & 7)
        elif instructions[pointer] == 6:
            b = a >> combo(instructions[pointer+1])
        elif instructions[pointer] == 7:
            c = a >> combo(instructions[pointer+1])
        pointer += 2

        if len(outlist) > len(instructions):
            exit
    if(outlist == instructions):
        print(starta, outlist)
        break
    for i in reversed(range(3, len(instructions))):
        if instructions[i] != outlist[i]:
            starta += 2 << 3*(i-1)
            break
    print(starta, outlist)
    starta += 1
