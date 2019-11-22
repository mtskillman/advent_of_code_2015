from my_graph import MyGraph
from itertools import permutations
a_graph = MyGraph()

with open('data.txt', 'r') as shit:
    to_input = shit.readlines()
    for line in to_input:
        line = line.replace("\n", "")
        line = line.split(" ")
        a_graph.add_pair(line[0], line[2], int(line[4]))

a_graph.mirror()
a_graph.print_contents()
all_locs = ['Tristram', 'AlphaCentauri', 'Snowdin', 'Tambi', 'Faerun', 'Norrath', 'Straylight', 'Arbre']
x = permutations(all_locs, 8)
possible_routes = []
for subset in x:
    possible_routes.append(subset)


def find_route_total_dist(items, graph):
    dist_count = 0
    pointer = 1
    while pointer < len(items):
        loc1 = items[pointer - 1]
        loc2 = items[pointer]
        dist_count += graph.find_distance(loc1,loc2)
        pointer += 1
    return dist_count


y = [find_route_total_dist(x, a_graph) for x in possible_routes]
print(max(y))
