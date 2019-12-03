from copy import deepcopy

#  1, on. 0, off.
initial = [[0 for x in range(100)] for x in range(100)]  # this needs to reflect data.txt, not all zeroes.

with open('data.txt', 'r') as my_data:
    y_val = 0
    for line in my_data.readlines():
        line.strip("\n")
        for index, value in enumerate(line):
            if value == "#":
                initial[y_val][index] = 1
        y_val += 1

always_on_coords = [(0, 0), (99, 0), (0, 99), (99, 99)]
for coord in always_on_coords:
    initial[coord[0]][coord[1]] = 1
def update(old, bound1, bound2):
    new = deepcopy(old)
    to_evaluate = list()
    for y_coord, item in enumerate(old):
        for x_coord, value in enumerate(item):
            to_evaluate.append((y_coord, x_coord, value))  # take note of the formatting here.
    for item in to_evaluate:
        modifiers = (-1, 0, 1)
        count = 0
        coords = (item[0], item[1])
        for ymod in modifiers:
            for xmod in modifiers:
                to_check = (coords[0] + ymod, coords[1] + xmod)
                if to_check[0] > bound1 or to_check[0] < bound2 or to_check[1] > bound1 or to_check[1] < bound2:
                    continue
                elif ymod == 0 and xmod == 0:
                    continue
                else:
                    if old[to_check[0]][to_check[1]] == 1:
                        count += 1
        if old[coords[0]][coords[1]] == 1:
            if count in (2, 3) or coords in always_on_coords:
                pass
            else:
                new[coords[0]][coords[1]] = 0
        else:
            if count == 3:
                new[coords[0]][coords[1]] = 1
    return new

for _ in range(100):
    initial = update(initial, 99, 0)

count = 0
for line in initial:
    for val in line:
        count += val
print(count)