class Sue(object):
    def __init__(self):
        self.data = {
            "Sue": None,
            'children': None,
            'cats': None,
            'samoyeds': None,
            'pomeranians': None,
            'akitas': None,
            'vizslas': None,
            'goldfish': None,
            'trees': None,
            'cars': None,
            'perfumes': None
        }
mysue = Sue()
mysue.data = {
            "Sue": None,
            'children': 3,
            'cats': 7,
            'samoyeds': 2,
            'pomeranians': 3,
            'akitas': 0,
            'vizslas': 0,
            'goldfish': 5,
            'trees': 3,
            'cars': 2,
            'perfumes': 1
        }


list_of_sues = []
with open('data.txt', 'r') as shit:
    mydata = shit.readlines()
    for line in mydata:
        newsue = Sue()
        line = line.split(" ")
        line[-1] = line[-1].strip("\n")
        for i, value in enumerate(line):
            if i % 2 == 1:
                continue
            else:
                value = value.strip(":")
                newsue.data[value] = int(line[i+1].strip(':,'))
        list_of_sues.append(newsue)
    for target in list_of_sues:
        flag = 1
        for k,v in target.data.items():
            if v is None or k == "Sue":
                continue
            else:
                dat = mysue.data[k]
                if dat is None:
                    continue
                else:
                    if k == "cats" or k == "trees":
                        if v <= dat:
                            flag = 0
                    elif k == 'goldfish' or k == 'pomeranians':
                        if v >= dat:
                            flag = 0
                    elif dat != v:
                        flag = 0
        if flag:
            print(target.data['Sue'])

