from collections import defaultdict

conversion_table = defaultdict(list)
target_string = ""

with open('data.txt', 'r') as my_data:
    for line in my_data.readlines():
        line = line.strip('\n')
        if len(line) < 30:
            to_process = line.split(" ")
            conversion_table[to_process[0]].append(to_process[2])
        else:
            target_string = line
# possibles = set()
# for element in conversion_table.keys():
#     count_of_that_element = target_string.count(element)
#     if not count_of_that_element:
#         continue
#     val = -1
#     for i in range(0, count_of_that_element):
#         val = target_string.find(element, val + 1)
#         # element is at VAL
#         len_of_elemnent = len(element)
#         for possible_transformation in conversion_table[element]:
#             to_add = target_string[0:val] + possible_transformation + target_string[val + len_of_elemnent:]
#             possibles.add(to_add)
# print(len(possibles))


#  part two
if __name__ == "__main__":
    def transform(data):
        current = data[0]
        step_count = data[1]
        if step_count > 50:  #  might need to change this.
            return step_count
        if current == target_string:
            return step_count
        else:
            possibles = set()
            for element in conversion_table.keys():
                count_of_that_element = current.count(element)
                if not count_of_that_element:
                    continue
                val = -1
                for i in range(0, count_of_that_element):
                    val = current.find(element, val + 1)
                    # element is at VAL
                    len_of_elemnent = len(element)
                    for possible_transformation in conversion_table[element]:
                        to_add = current[0:val] + possible_transformation + current[val + len_of_elemnent:]
                        possibles.add((to_add, step_count + 1))
            return min(map(transform, possibles))


    print(transform(('e', 0)))
