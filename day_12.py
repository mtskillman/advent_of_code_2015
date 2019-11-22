import json
import flatten_json

sum = 0
def find_sum(cont):
    global sum
    if isinstance(cont, dict):
        if 'red' not in cont.values():
            for v in cont.values():
                if isinstance(v, dict):
                    find_sum(v)
                elif isinstance(v, list):
                    for thing in v:
                        find_sum(thing)
                elif isinstance(v, int):
                    sum += v
                else:
                    pass
    elif isinstance(cont, int):
        sum += cont
    elif isinstance(cont, list):
        for entry in cont:
            find_sum(entry)
    else:
        pass


with open('data.json', 'r') as shit:
    x = json.load(shit)
    find_sum(x)
    print(sum)
    '''
    
    x = flatten_json.flatten(x)
    sum = 0
    for value in x.values():
        try:
            sum += int(value)
        except:
            pass
    print(sum)
    '''


