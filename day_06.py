storage = [[0 for i in range(1000)] for y in range(1000)]
instructionn = open('input.txt','r').read().split('\n')
#instructionn = ['turn on 0,0 through 999,999']
def main():
    for line in instructionn:
        line = line.split(" ")
        if line[0] == 'toggle':
            x,y = tuple(line[1].split(","))
            a,b = tuple(line[3].split(","))
            x = int(x)
            y = int(y)
            a = int(a)
            b = int(b)
            for ycoord in range(min(y,b),max(y,b)+1):
                for xcoord in range(min(x,a),max(x,a)+1):
                    storage[ycoord][xcoord] += 2
        elif line[1] == 'on':
            x,y = tuple(line[2].split(","))
            a,b = tuple(line[4].split(","))
            x = int(x)
            y = int(y)
            a = int(a)
            b = int(b)
            for ycoord in range(min(y,b),max(y,b)+1):
                for xcoord in range(min(x,a),max(x,a)+1):
                    storage[ycoord][xcoord] += 1
        elif line[1] == 'off':
            x,y = tuple(line[2].split(","))
            a,b = tuple(line[4].split(","))
            x = int(x)
            y = int(y)
            a = int(a)
            b = int(b)
            for ycoord in range(min(y,b),max(y,b)+1):
                for xcoord in range(min(x,a),max(x,a)+1):
                    if storage[ycoord][xcoord] > 0:
                        storage[ycoord][xcoord] -= 1
count = 0
main()

for thing in storage:
    count += sum(thing)
print(count)
