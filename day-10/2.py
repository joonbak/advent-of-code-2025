import z3

with open("input.txt", "r") as file:
    lines = [line.split() for line in file]

total = 0

for line in lines:
    buttons = []
    joltages = []

    for i in line:
        if i[0] == "(":
            buttons.append(set(map(int, i.strip("()").split(","))))
        if i[0] == "{":
            joltages = list(map(int, i.strip("{}").split(",")))
    o = z3.Optimize()
    vars = z3.Ints(f"n{i}" for i in range(len(buttons)))

    for var in vars:
        o.add(var >= 0)

    for i, joltage in enumerate(joltages):
        equation = 0
        for b, button in enumerate(buttons):
            if i in button:
                equation += vars[b]
        o.add(equation == joltage)

    o.minimize(z3.Sum(vars))
    o.check()
    total += o.model().eval(z3.Sum(vars)).as_long()
print(total)
