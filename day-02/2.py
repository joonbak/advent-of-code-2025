with open("input.txt", "r") as file:
    line = file.readline()
    codes = line.split(",")

count = 0

for code in codes:
    id_ranges = code.split("-")
    for id in range(int(id_ranges[0]), int(id_ranges[1]) + 1):
        if str(id) in (str(id) + str(id))[1:-1]:
            count += id

print(count)
