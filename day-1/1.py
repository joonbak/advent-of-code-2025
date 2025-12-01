with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line.strip()


def split_rotation(line: str) -> tuple[str, int]:
    direction, number = line[0], line[1:]
    return direction, int(number)


dial = 50
count = 0

for line in lines:
    direction, number = split_rotation(line)
    if direction == "L":
        dial = (dial - number) % 100
    else:
        dial = (dial + number) % 100
    if dial == 0:
        count += 1

print(count)
