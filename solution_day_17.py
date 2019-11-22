from numpy import array
from numpy import sum as specialsum
from sympy.utilities.iterables import multiset_combinations, variations
from collections import deque


def find_all_perms_two(target):
    total = deque()

    for x in range(len(target)):
        for item in variations(target, x):
            total.append(item)
    return array(total)


def find_all_permutations_of_array(target_array):
    total = deque()

    for x in range(len(target_array)):
        for item in multiset_combinations(target_array, x):
            total.append(item)
    print(total)
    return array(total)



def find_count_of_matching_sequences(collection_of_sequences, goal):
    count = 0
    for sequence in collection_of_sequences:
        if specialsum(sequence) == goal:
            print (f'sum of {sequence} is {goal}')
            count += 1

    return count


with open('data.txt', 'r') as shit:
    conts = []
    for line in shit.readlines():
        line.strip('\n')
        conts.append(int(line))
    conts = array(conts)
    x = find_all_permutations_of_array(conts)
    y = find_count_of_matching_sequences(x, 150)
    print(len(conts))
    print(y)