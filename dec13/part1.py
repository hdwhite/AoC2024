import re

total = 0
with open("part1.txt") as file:
    while True:
        buttonA = file.readline()
        if not buttonA:
            break
        buttonB = file.readline()
        prize = file.readline()
        file.readline()

        a = re.findall("\+(\d+).+\+(\d+)", buttonA)[0]
        b = re.findall("\+(\d+).+\+(\d+)", buttonB)[0]
        p = re.findall("=(\d+).+=(\d+)", prize)[0]
        (a, b, p) = ((int(a[0]), int(a[1])), (int(b[0]), int(b[1])), (int(p[0]), int(p[1])))

        apress = (b[1] * p[0] - b[0] * p[1]) / (a[0] * b[1] - a[1] * b[0])
        bpress = (a[0] * p[1] - a[1] * p[0]) / (a[0] * b[1] - a[1] * b[0])

        if(apress.is_integer() and bpress.is_integer()):
            total += 3*apress + bpress

print(total)
