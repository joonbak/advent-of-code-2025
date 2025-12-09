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


for a, b, _ in distances[:1000]:
    merge(a, b)

sizes = [0] * len(points)

for box in range(len(points)):
    sizes[find(box)] += 1

sizes.sort(reverse=True)

print(sizes[0] * sizes[1] * sizes[2])


"""
conn = {}
for i, (x1, y1, z1) in enumerate(coords[:-1]):
    for j, (x2, y2, z2) in enumerate(coords[i + 1 :], start=i + 1):
        sum = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
        distance = sum**0.5
        conn_coords = str(coords[i]) + ":" + str(coords[j])
        conn[conn_coords] = distance
        # print(conn_coords)

sorted_dist = sorted(conn.items(), key=lambda item: item[1])
# for i in range(10):
#    print(sorted_dist[i])
res = []
cnt = 0
for k, v in sorted_dist:
    co1, co2 = k.split(":")
    set1 = {co1, co2}
    if len(res) == 0:
        res.append(set1)
    for i in range(len(res)):
        if res[i].intersection(set1):
            res[i] = res[i].union(set1)
        else:
            res.append(set1)
        break
    if cnt == 10:
        break
    cnt += 1

for i in res:
    print(i)
"""
