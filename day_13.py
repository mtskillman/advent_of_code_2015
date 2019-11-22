from itertools import permutations

from graff import MyGraph



def find_util_of_arrangement(seatchart, graph):
    #return util value
    sum = 0
    for i, person in enumerate(seatchart):
        sum += graph.find_distance(person, seatchart[i - 1])
        if i == 8:
            sum += graph.find_distance(person, seatchart[0])
        else:
            sum += graph.find_distance(person, seatchart[i + 1])
    return sum


with open('data.txt', 'r') as shit:
    a_graph = MyGraph()
    x = shit.readlines()
    for line in x:
        line = line.strip('.\n')
        line = line.split(" ")
        value = int(line[3])
        if line[2] == 'lose':
            value *= -1
        a_graph.add_pair(line[0], line[10], value)
    y = ['Alice', 'Bob', 'Carol', 'David', 'Eric', 'Frank', 'George', 'Mallory']
    for person in y:
        a_graph.add_pair('me', person, 0)
    y.append('me')
    z = a_graph.contents.keys()
    for person in z:
        a_graph.contents[person]['me'] = 0

    possible_arrangements = permutations(y,9)
    nums = [find_util_of_arrangement(x, a_graph) for x in possible_arrangements]
    print(max(nums))
