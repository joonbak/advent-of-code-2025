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
    for _ in range(number):
        if direction == "L":
            dial = (dial - 1 + 100) % 100
        else:
            dial = (dial + 1) % 100
        if dial == 0:
            count += 1

print(count)
