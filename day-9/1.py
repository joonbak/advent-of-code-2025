with open("input.txt", "r") as file:
    lines = [list(map(int, line.split(","))) for line in file]

max_area = 0
for i in lines[:-1]:
    for j in lines[1:]:
        area = abs(i[0] - j[0] + 1) * abs(i[1] - j[1] + 1)
        max_area = max(max_area, area)

print(max_area)
