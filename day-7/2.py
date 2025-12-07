with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]

beams = set()
split = [0] * len(lines[0])

for line in lines:
    splitter = 0

    for j, val in enumerate(line):
        if val == "S":
            beams.add(j)
            split[j] = 1
        if val == "^" and j in beams:
            beams.remove(j)
            beams.add(j - 1)
            beams.add(j + 1)
            split[j - 1] += split[j]
            split[j + 1] += split[j]
            split[j] = 0

print(sum(split))
