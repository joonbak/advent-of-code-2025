with open("input.txt", "r") as f:
    devices = {}
    for line in f:
        line = line.strip()
        key, values = line.split(":", 1)
        devices[key.strip()] = values.strip().split()


def dfs(node, devices, visited=None):
    if visited is None:
        visited = set()

    if node == "out":
        return 1

    if node in visited:
        return 0

    if node not in devices:
        return 0

    visited.add(node)
    count = 0

    for neighbor in devices[node]:
        count += dfs(neighbor, devices, visited.copy())

    return count


total = dfs("you", devices)
print(total)
