with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]

sum = 0

for line in lines:
    best = 0
    stack = []

    for i in range(len(line)):
        while (len(stack) > 0 and stack[-1] < line[i] and len(stack) + (len(line) - i) > 12):
            stack.pop()
        stack.append(line[i])

        while len(stack) > 12:
            stack.pop()

    best = "".join(stack)
    sum += int(best)

print(sum)
