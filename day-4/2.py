with open("input.txt", "r") as file:
    lines = [list(line.strip()) for line in file]


def is_in_bounds(i: int, j: int, m: int, n: int) -> bool:
    if i < 0 or j < 0 or i >= m or j >= n:
        return False
    return True


def get_adjacent(arr: list, i: int, j: int) -> list:
    res = []

    m = len(arr)
    n = len(arr[0])

    dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dx, dy in dir:
        x, y = i + dx, j + dy
        if is_in_bounds(x, y, m, n):
            res.append(arr[x][y])

    return res


removed = 0
count = 1
while count > 0:
    count = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "@":
                arr = get_adjacent(lines, i, j)
                roll_count = arr.count("@") + arr.count("X")
                if roll_count < 4:
                    count += 1
                    lines[i][j] = "X"

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "X":
                lines[i][j] = "."

    removed += count

print(removed)
