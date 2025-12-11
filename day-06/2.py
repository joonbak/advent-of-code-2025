with open("input.txt", "r") as file:
    lines = [line for line in file]

cols = list(zip(*lines))

total = 0
groups = []
group = []
for col in cols:
    col = "".join(col).replace(" ", "").strip()
    if col != "":
        group.append(col)
    else:
        groups.append(group)
        group = []

for group in groups:
    op = group[0][-1]
    group[0] = group[0][:-1]
    expression = op.join(group)
    sum = eval(expression)
    total += sum


print(total)
