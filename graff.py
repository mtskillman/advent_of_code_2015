class MyGraph(object):
    def __init__(self):
        self.contents = {}

    def find_distance(self, loc1, loc2):
        return self.contents[loc1][loc2]


    def add_pair(self, loc1, loc2, distance):
        if loc1 not in self.contents.keys():
            self.contents[loc1] = {
                loc2: distance
            }
        else:
            self.contents[loc1][loc2] = distance

    def mirror(self):
        copy = {}
        for k, v in self.contents.items():
            for k2, v2 in v.items():
                if k not in copy.keys():
                    copy[k] = {k2:v2}
                else:
                    copy[k][k2] = v2
        for k1, v1 in copy.items():
            for k2, v2 in v1.items():
                self.add_pair(k2,k1, v2)

    def print_contents(self):
        for k1, v1 in self.contents.items():
            for k2, v2 in v1.items():
                print(f'from {k1} to {k2} is {v2} !')
