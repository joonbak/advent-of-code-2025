with open("input.txt", "r") as file:
    lines = [[int(x) for x in line.strip()] for line in file]

sum = 0

for line in lines:
    best_list = []
    best_idx = 0

    for i in range(11, -1, -1):
        for j in range(best_idx, len(line) - i):
            if line[j] > line[best_idx]:
                best_idx = j
        best_list.append(line[best_idx])
        best_idx += 1

    joined = "".join(map(str, best_list))
    sum += int(joined)

print(sum)
