with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]

beams = set()
count = 1

for line in lines:
    for j, val in enumerate(line):
        if val == "^":
            beams.add(j - 1)
            beams.add(j + 1)
        if val == "^" and j in beams:
            count += 1
            beams.remove(j)

print(count)
