with open("input.txt", "r") as file:
    lines = [[int(x) for x in line.strip()] for line in file]

sum = 0

for line in lines:
    best_idx = 0

    for i in range(len(line) - 1):
        if line[i] > line[best_idx]:
            best_idx = i

    sec_max = best_idx + 1

    for j in range(best_idx + 1, len(line)):
        if line[j] > line[sec_max]:
            sec_max = j

    joined = str(line[best_idx]) + str(line[sec_max])
    sum += int(joined)

print(sum)
