with open("input.txt", "r") as file:
    sections = file.read().strip().split("\n\n")
    ranges = sections[0].splitlines()
    ids = sections[1].splitlines()

seen = set()
count = 0

for id in ids:
    for i in range(len(ranges)):
        if id in seen:
            continue
        start, end = ranges[i].split("-")
        if int(start) <= int(id) <= int(end):
            seen.add(id)
            count += 1
            break

print(count)
