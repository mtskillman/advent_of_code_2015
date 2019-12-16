stuff = open('shit2.txt', 'r').read()

xcoord = 0
ycoord = 0

robot_xcoord = 0
robot_ycoord = 0

log = {
    (0,0): 1
}

robo_log = {
    (0,0): 1
}
robo_flag = 0
for char in stuff:
    if robo_flag == 0:
        if char == '^':
            ycoord += 1
        elif char == '<':
            xcoord -= 1
        elif char == '>':
            xcoord += 1
        elif char == 'v':
            ycoord -= 1
        if (xcoord, ycoord) not in log:
            log[(xcoord, ycoord)] = 1
        else:
            log[(xcoord,ycoord)] += 1
        robo_flag = 1
    elif robo_flag == 1:
        if char == '^':
            robot_ycoord += 1
        elif char == '<':
            robot_xcoord -= 1
        elif char == '>':
            robot_xcoord += 1
        elif char == 'v':
            robot_ycoord -= 1
        if (robot_xcoord, robot_ycoord) not in robo_log:
            robo_log[(robot_xcoord, robot_ycoord)] = 1
        else:
            robo_log[(robot_xcoord,robot_ycoord)] += 1
        robo_flag = 0
count = 0

log.update(robo_log)
for v in log.values():
    if v >= 1:
        count += 1

print(count)    
