from day7 import Tree

file = open("input.txt","r")
lines = file.readlines()
data = [0]
data += [int(line.strip()) for line in lines]
data.sort()
numdata = len(data)
"""
PART1
"""
#cntdiff1 = 0
#cntdiff3 = 0
#for i,num in enumerate(data):
#    if i==numdata-1:
#        break
#    if data[i+1]-data[i] == 1:
#        cntdiff1 += 1
#    elif data[i+1]-data[i] == 3:
#        cntdiff3 += 1
#print(cntdiff1)
#print(cntdiff3+1)
#print(cntdiff1*(cntdiff3+1))
"""
PART2
"""
data += [data[-1]+3]
numdata += 1
#print(data)
"""
#bad solution
#create a node for each entry
nodes = []
for num in data:
    node = Tree.Tree(str(num),num)
    nodes += [node]
#construct tree
for i,num in enumerate(data):
    if i==numdata-1:
        break
    parent = nodes[i]
    for j in range(3):
        if i+j+1 >= numdata:
            break
        child = nodes[i+j+1]
        if data[i+j+1]-num <= 3:
            parent.insert(child,1)
        else:
            break
pathcnt = nodes[0].getnodepathcnt(str(data[-1]))
print(pathcnt)
"""
numpaths = 1
incoming = [1]*numdata
for idx,num in enumerate(data):
    numoutgoing = 1
    if idx - 2 >= 0 and num-data[idx-2]<=3:
        incoming[idx] += incoming[idx-2]
    if idx - 3 >= 0 and num - data[idx - 3] <= 3:
        incoming[idx] += incoming[idx - 3]
    if idx + 1 < numdata:
        incoming[idx+1] = incoming[idx]
    if idx + 2 < numdata and data[idx + 2] - num <= 3:
        numoutgoing += 1
    if idx + 3 < numdata and data[idx + 3] - num <= 3:
        numoutgoing += 1
    numpaths += incoming[idx]*(numoutgoing-1)
print(numpaths)
