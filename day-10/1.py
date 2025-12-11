import itertools

with open("input.txt", "r") as file:
    lines = [line.split() for line in file]


total = 0

for line in lines:
    target = ""
    buttons = []
    for i in line:
        if i[0] == "[":
            target = i.strip("[]")
            target = {index for index, light in enumerate(target) if light == "#"}
        if i[0] == "(":
            buttons.append(set(map(int, i.strip("()").split(","))))

    for count in range(1, len(buttons) + 1):
        for attempt in itertools.combinations(buttons, r=count):
            lights = set()
            for button in attempt:
                lights ^= button
            if lights == target:
                total += count
                break
        else:
            continue
        break

print(total)
