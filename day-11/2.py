with open("input.txt", "r") as f:
    devices = {}
    for line in f:
        line = line.strip()
        key, values = line.split(":", 1)
        devices[key.strip()] = values.strip().split()


def dfs(node, devices, visited_dac=False, visited_fft=False, cache=None):
    if cache is None:
        cache = {}

    if node == "dac":
        visited_dac = True

    if node == "fft":
        visited_fft = True

    if node == "out":
        if visited_dac and visited_fft:
            return 1
        else:
            return 0

    if node not in devices:
        return 0

    cache_key = (node, visited_dac, visited_fft)
    if cache_key in cache:
        return cache[cache_key]

    count = 0

    for neighbor in devices[node]:
        count += dfs(neighbor, devices, visited_dac, visited_fft, cache)

    cache[cache_key] = count
    return count


total = dfs("svr", devices)
print(total)
