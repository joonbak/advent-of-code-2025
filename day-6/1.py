with open("input.txt", "r") as file:
    lines = [[x for x in line.split()] for line in file]

cols = list(zip(*lines))

total = 0

for i in range(len(cols)):
    op = cols[i][-1]
    sum = int(cols[i][0])

    if op == "+":
        for j in range(1, len(cols[i]) - 1):
            sum += int(cols[i][j])
    else:
        for j in range(1, len(cols[i]) - 1):
            sum *= int(cols[i][j])

    total += sum

print(total)
