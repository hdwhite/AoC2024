#We're just pretending the bad level never existed by popping it and moving on
numsafe = 0
with open("part1.txt") as file:
    for line in file:
        numsafe = numsafe + 1
        usedDampener = False
        report = list(map(int, line.split()))
        if len(report) < 2:
            continue

        #We look at the first three values to determine which direction the
        #levels are going, just in case the bad level is early on
        sign = 0
        for i in range(min(3, len(report))):
            sign += 1 if report[i] < report[i+1] else -1
        sign /= abs(sign)

        i = 0
        while i < len(report) - 1:
            diff = report[i+1] - report[i]
            #All good, keep moving on
            if sign * diff > 0 and sign * diff < 4:
                i += 1
                continue

            #We can only ignore mistakes once
            if usedDampener:
                numsafe -= 1
                break
            usedDampener = True

            #Final level is the only bad one, so we're good
            if i == len(report) - 2:
                break
            diff = report[i+2] - report[i]
            #Looks like if we treat the second level as bad, we can be fine
            #Else delete the first level and try again
            if sign * diff > 0 and sign * diff < 4:
                report.pop(i+1)
            else:
                report.pop(i)
                i = max(0, i - 1)
print(numsafe)
