#Alas, could not get to this one before midnight either
numsafe = 0
with open("part1.txt") as file:
    for line in file:
        numsafe = numsafe + 1
        report = list(map(int, line.split()))
        if len(report) < 2:
            continue
        sign = 1 if report[0] < report[1] else -1
        for i in range(len(report) - 1):
            diff = report[i+1] - report[i]
            if sign * diff < 1 or sign * diff > 3:
                numsafe = numsafe - 1
                break
print(numsafe)
