with open("input.txt", "r") as file:
    block = file.read()
    parts = block.split("\n\n")
    presents = parts[:-1]

sizes = {}

for present in presents:
    lines = present.splitlines()
    key, val = lines[0][0], lines[1:]
    cnt = 0
    for r in val:
        for c in r:
            if c == "#":
                cnt += 1
    sizes[int(key)] = cnt

regions = parts[-1].splitlines()
res = 0

for region in regions:
    size, indexes = region.split(":")
    x, y = size.split("x")
    region_size = int(x) * int(y)
    indexes = list(map(int, indexes.split()))
    total_present_size = sum(n * sizes[i] for i, n in enumerate(indexes))
    if region_size > total_present_size * 1.2:
        res += 1

print(res)
