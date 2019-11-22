class Reindeer(object):
    def __init__(self, speed, duration, cooldown):
        self.speed = speed
        self.duration = duration
        self.cooldown = cooldown

        self.restremaining = 0
        self.fatigue = 0
        self.pos = 0
    def increment(self):
        if self.fatigue == self.duration:
            self.restremaining = self.cooldown
            self.fatigue = 0
        elif self.restremaining > 1:
            self.restremaining -= 1
        else:
            self.pos += self.speed
            self.fatigue += 1

    def tell_current_pos(self):
        return self.pos

with open('data.txt', 'r') as shit:
    deers = []
    x = shit.readlines()
    for line in x:
         line = line.split(" ")
         deers.append(Reindeer(int(line[3]), int(line[6]), int(line[13])))
    count = 2503
    scores = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    while count > 0:
        for deer in deers:
            deer.increment()
        count -= 1
        distances = [x.tell_current_pos() for x in deers]

        maxval = max(distances)
        for i, dist in enumerate(distances):
            if dist == maxval:
                scores[i] += 1
    print(max(scores))



