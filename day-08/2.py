with open("input.txt", "r") as file:
    points = [list(map(int, line.split(","))) for line in file]

distances = []

for i, (x1, y1, z1) in enumerate(points):
    for j, (x2, y2, z2) in enumerate(points):
        if i > j:
            dist = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
            distances.append((i, j, dist))

distances.sort(key=lambda x: x[-1])

parent = {i: i for i in range(len(points))}


def find(v: int) -> int:
    if parent[v] == v:
        return v
    parent[v] = find(parent[v])
    return parent[v]


def merge(a: int, b: int):
    parent[find(a)] = find(b)


circuits = len(points)

for a, b, _ in distances:
    if find(a) == find(b):
        continue

    merge(a, b)

    circuits -= 1
    if circuits == 1:
        print(points[a][0] * points[b][0])
        break
