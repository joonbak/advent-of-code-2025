with open("input.txt", "r") as file:
    sections = file.read().strip().split("\n\n")
    ranges = sections[0].splitlines()
    ids = sections[1].splitlines()

ranges = [list(map(int, r.split("-"))) for r in ranges]
ranges.sort()

combined_ranges = [ranges[0]]

for i in range(1, len(ranges)):
    c_start, c_end = combined_ranges[-1]
    start, end = ranges[i]
    if c_start <= start <= c_end:
        combined_ranges[-1][1] = max(end, c_end)
    else:
        combined_ranges.append(ranges[i])

count = 0

for i in combined_ranges:
    difference = i[1] - i[0]
    count += difference + 1

print(count)
