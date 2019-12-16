# use this one

def and_gate(value_1=None, value_2=None):
    return value_1 & value_2

def or_gate(value_1=None, value_2=None):
    return value_1 | value_2

def not_gate(value_1=None):
    return 65535 - value_1

def lshift_gate(value_1=None, value_2=None):
    return (value_1 << value_2) & 0b1111111111111111

def rshift_gate(value_1=None, value_2=None):
    return value_1 >> value_2


def compute_for_wire(target_wire, connection_table, memo={'b': 956}):
    """
    :param target_wire: string representing a particular wire in the 16 bit unsigned machine
    :param connection_table: parsed representation of instructions provided.
    :param memo: default to 'b':956 in order to satisfy requirements for part 2 of assignment
    :return: signal value of 'target wire'
    """
    if target_wire in memo.keys():
        return memo[target_wire]
    if isinstance(target_wire, int):
        return target_wire
    possibles = ['and','or','not','lshift','rshift']
    lookup = connection_table[target_wire]

    if isinstance(lookup, int):
        return lookup
    else:
        flag = 0
        for item in possibles:
            if item in lookup:
                if item == 'and':
                    memo[target_wire] = and_gate(compute_for_wire(lookup[0], connection_table, memo), compute_for_wire(lookup[2], connection_table, memo))
                    flag = 1
                elif item == 'or':
                    flag = 1
                    memo[target_wire] = or_gate(compute_for_wire(lookup[0], connection_table,memo), compute_for_wire(lookup[2], connection_table,memo))
                elif item == 'not':
                    flag = 1
                    memo[target_wire] = not_gate(compute_for_wire(lookup[1], connection_table, memo))
                elif item == 'lshift':
                    flag = 1
                    memo[target_wire] = lshift_gate(compute_for_wire(lookup[0], connection_table, memo), lookup[2])
                elif item == 'rshift':
                    flag = 1
                    memo[target_wire] = rshift_gate(compute_for_wire(lookup[0], connection_table,memo), lookup[2])
        if flag == 0:
            memo[target_wire] = compute_for_wire(lookup[0],connection_table,memo)
    return memo[target_wire]


def parse_a_line(line):
    line = line.strip('\n')
    line = line.split("->")
    line[1] = line[1].strip(' ')
    try:
        line[0] = int(line[0])
    except:
        temp = line[0].split(' ')
        temp2 = []
        for each in temp:
            try:
                temp2.append(int(each))
            except:
                temp2.append(each.lower())
        line[0] = temp2
        line[0].remove('')
    return line


def build_connection_table(full_input):
    output = {}
    for entry in full_input:
        temp = parse_a_line(entry)
        output[temp[1]] = temp[0]
    return output
if __name__ == '__main__':
    with open('data_day7.txt','r') as data:
        mytable = build_connection_table(data.readlines())
        print(compute_for_wire('a', mytable))
