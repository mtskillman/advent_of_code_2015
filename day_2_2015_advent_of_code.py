stuff = open('shit.txt', 'r').read()

box_dimensions = []
pointer = 0
x = 0
y = 0
z = 0
flag = 0
while 1:
    if pointer >= len(stuff):
        box_dimensions.append((x,y,z))
        break
    target = stuff[pointer]
    if target == '\n':
        box_dimensions.append((x,y,z))
        flag *= 0
        x *= 0
        y *= 0
        z *= 0
    elif target != 'x' and x == 0:
        x = int(target)
    elif target != 'x' and x > 0 and flag < 1:
        x *= 10
        x += int(target)
    elif target != 'x' and x > 0 and y == 0:
        y = int(target)
    elif target != 'x' and y < 10 and z == 0 and flag != 2:
        y *= 10
        y += int(target)
    elif target != 'x' and z == 0 and x > 0 and y > 0 and target != '\n':
        z = int(target)
    elif target != 'x' and z < 10 and target != '\n':
        z *= 10
        z += int(target)
    elif target == 'x':
        flag += 1
    pointer += 1

total_wp = 0
total_ribbon = 0
for box in box_dimensions:
    length = box[0]
    width = box[1]
    height = box[2]
    side1 = 2 * length * width
    side2 = 2 * width * height
    side3 = 2 * height * length
    smallest_side_area = min(side1, side2, side3) / 2
    total_wp += smallest_side_area + side1 + side2 + side3

    dims = [length, width, height]
    dims.sort()
    total_ribbon += 2*dims[0] + 2 * dims[1]
    total_ribbon += length * width * height

print(box_dimensions)
print(total_wp)
print(total_ribbon)