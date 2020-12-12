import math
import re

file = open("input.txt","r")
lines = file.readlines()
xtravel = 0
ytravel = 0
waypoint_x = 10
waypoint_y = 1
theta = 0
for line in lines:
    if line == '\n':
        continue
    dir = line[0]
    step = int(re.split('N|S|E|W|R|L|F',line)[1].strip())
    if dir=='L':
        #theta += step
        theta = step
        deltax = waypoint_x*math.cos(theta/180*math.pi) + waypoint_y*math.cos((theta+90)/180*math.pi)
        deltay = waypoint_x*math.sin(theta/180*math.pi) + waypoint_y*math.sin((theta+90)/180*math.pi)
        waypoint_x = deltax
        waypoint_y = deltay
    elif dir == 'R':
        #theta -= step
        theta = step
        deltax = waypoint_x*math.cos((-theta)/180*math.pi) + waypoint_y*math.cos((90-theta)/180*math.pi)
        deltay = waypoint_x*math.sin((-theta)/180*math.pi) + waypoint_y*math.sin((90-theta)/180*math.pi)
        waypoint_x = deltax
        waypoint_y = deltay
    elif dir == 'F':
        xtravel += step*waypoint_x
        ytravel += step*waypoint_y
    elif dir == 'E':
        waypoint_x += step
    elif dir == 'W':
        waypoint_x -= step
    elif dir == 'N':
        waypoint_y += step
    elif dir == 'S':
        waypoint_y -= step
    else:
        pass
print(xtravel,ytravel)
print(abs(xtravel)+abs(ytravel))