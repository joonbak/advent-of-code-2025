with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]

sum = 0

for line in lines:
    best = 0
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            curr = int(line[i] + line[j])
            best = max(best, curr)
    sum += best

print(sum)
