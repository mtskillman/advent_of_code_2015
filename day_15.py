from itertools import permutations
spr = (2, 0, -2, 0, 3)
but = (0, 5, -3, 0, 3)
choc = (0, 0, 5, -1, 8)
candy = (0, -1, 0, 5, 8)
ingreds = [spr, but, choc, candy]
one = [x for x in range(101)]
z = permutations(one, 4)
output = []
for thing in z:
    if sum(thing) == 100:
        output.append(thing)

def find_total(item):
    #return value of cookie
    # item will be percentage values of each ingredient
    props = [0, 0, 0, 0]
    cals = 0
    for i, percentage in enumerate(item):
        values = ingreds[i]
        for y, prop in enumerate(values[0:4]):
            props[y] += percentage * prop
        cals += percentage * values[4]
    new_shit = []
    for thing in props:
        if thing > 0:
            new_shit.append(thing)
        else:
            new_shit.append(0)
    total = new_shit.pop()
    for thing2 in new_shit:
        total *= thing2
    return (total, cals)

output = list(map(find_total, output))
newshit = [x[0] for x in output if x[1] == 500]
with open('day15answer.txt', 'w') as shit:
    shit.write(max(newshit))

