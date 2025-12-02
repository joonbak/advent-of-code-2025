with open("input.txt", "r") as file:
    line = file.readline()
    codes = line.split(",")

count = 0

for code in codes:
    id_ranges = code.split("-")
    for id in range(int(id_ranges[0]), int(id_ranges[1]) + 1):
        mid = len(str(id)) // 2
        first_half = str(id)[0:mid]
        sec_half = str(id)[mid:]
        if first_half == sec_half:
            count += id

print(count)
