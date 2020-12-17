import numpy as np

file = open("input.txt","r")
lines = file.readlines()
lines = [line.strip() for line in lines]

active = set()
for row,line in enumerate(lines):
    for col,c in enumerate(line):
        if c=='#':
            active.add(tuple([row,col,0,0]))
print(len(active))
cyclecnt = 0
while cyclecnt<6:
    #cycle
    neighbours = set()
    makeinactive = set()
    for point in active:
        adjacency = 0
        for i in range(-1,2):
            for j in range(-1,2):
                for k in range(-1,2):
                    for w in range(-1, 2):
                        if i==0 and j==0 and k == 0 and w==0:
                            continue
                        neighbour = tuple([point[0]+i,point[1]+j,point[2]+k,point[3]+w])
                        if active.__contains__(neighbour):
                            adjacency += 1
                        else:
                            neighbours.add(neighbour)
        if adjacency==2 or adjacency==3:
            pass
        else:
            makeinactive.add(point)
    makeactive = set()
    for point in neighbours:
        adjacency = 0
        for i in range(-1,2):
            for j in range(-1,2):
                for k in range(-1,2):
                    for w in range(-1,2):
                        neighbour = tuple([point[0]+i,point[1]+j,point[2]+k,point[3]+w])
                        if active.__contains__(neighbour):
                            adjacency += 1
        if adjacency == 3:
            makeactive.add(point)
    for point in makeinactive:
        active.remove(point)
    for point in makeactive:
        active.add(point)
    print(len(active))
    cyclecnt += 1