antennae = {}
ymax = 0

with open("part1.txt") as file:
    for line in file:
        for x in range(len(line) - 1):
            char = line[x]
            if char == '.':
                continue
            if char in antennae:
                antennae[char].append((x, ymax))
            else:
                antennae[char] = [(x, ymax)]
        xmax = len(line) - 1
        ymax += 1

antinodes = {}
for curFreq, freqNodes in antennae.items():
    for node1 in freqNodes:
        for node2 in freqNodes:
            if node1 == node2:
                continue
            antinode = (2 * node1[0] - node2[0], 2 * node1[1] - node2[1])
            print(antinode)
            if (antinode[0] >= 0 and antinode[0] < xmax
              and antinode[1] >= 0 and antinode[1] < ymax):
                antinodes[antinode] = curFreq

print(len(antinodes))
