from functools import cache

with open("input.txt", "r") as file:
    points = [list(map(int, line.split(","))) for line in file]


@cache
def point_in_poly(x: int, y: int) -> bool:
    inside = False

    for (x1, y1), (x2, y2) in zip(points, points[1:] + points[:1]):
        if (
            x == x1 == x2
            and min(y1, y2) <= y <= max(y1, y2)
            or y == y1 == y2
            and min(x1, x2) <= x <= max(x1, x2)
        ):
            return True
        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
            inside = not inside
    return inside


def edge_intersect(x1, y1, x2, y2, rx1, ry1, rx2, ry2):
    if y1 == y2:
        if ry1 < y1 < ry2:
            if max(x1, x2) > rx1 and min(x1, x2) < rx2:
                return True
    else:
        if rx1 < x1 < rx2:
            if max(y1, y2) > ry1 and min(y1, y2) < ry2:
                return True

    return False


def square_valid(x1: int, x2: int, y1: int, y2: int) -> bool:
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])

    for x, y in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
        if not point_in_poly(x, y):
            return False
    for (ex1, ey1), (ex2, ey2) in zip(points, points[1:] + points[:1]):
        if edge_intersect(ex1, ey1, ex2, ey2, x1, y1, x2, y2):
            return False

    return True


max_area = 0
for i, (x1, y1) in enumerate(points):
    for j, (x2, y2) in enumerate(points):
        if i < j:
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if area > max_area and square_valid(x1, x2, y1, y2):
                max_area = area

print(max_area)
