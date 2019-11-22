def first_requirement(string, lookup_table):
    #return bool
    count = 1
    last_value = -10
    for char in string:
        if lookup_table[char] == last_value + 1:
            count += 1
        else:
            count = 1
        if count == 3:
            return True
        last_value = lookup_table[char]
    return False
def second_requirement(string):
    #return bool
    bad_chars = ['i', 'o', 'l']
    for char in bad_chars:
        for char2 in string:
            if char == char2:
                return False
    return True

def third_requirement(string):
    #return bool
    count = 0
    last_char = ""
    for char in string:
        if char == last_char:
            count += 1
            last_char = ""
            continue
        last_char = char
    if count >= 2:
        return True
    return False

def increment_string(string, lookup_table):
    newstring = ""
    carry = True
    for char in string[::-1]:
        current_value = lookup_table[char]
        if carry:
            current_value += 1
        if current_value == 27:
            newstring = 'a' + newstring
            carry = True
            continue
        for k,v in lookup_table.items():
            if v == current_value:
                to_add = k
                break
        newstring = to_add + newstring
        carry = False
    return newstring

alphabet = "abcdefghijklmnopqrstuvwxyz"
storage = {}

for i, char in enumerate(alphabet):
    storage[char] = i + 1


start = "cqjxxyzz"
while 1:
    start = increment_string(start, storage)
    if first_requirement(start, storage) and second_requirement(start) and third_requirement(start):
        print(start)
        break