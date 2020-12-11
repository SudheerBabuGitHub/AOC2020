import numpy as np

file = open("input.txt","r")
lines = file.readlines()
lines = [line.strip() for line in lines]
numrows = len(lines)
numcols = len(lines[0])
occupancy = np.ones((numrows+2,numcols+2))*-1
for row,line in enumerate(lines):
    for col,c in enumerate(line):
        if c=='L':
            occupancy[row+1,col+1] = 0
        elif c=='#':
            occupancy[row+1,col+1] = 1
newoccupancy = occupancy.copy()

def GetFirstVisible(array, crow, ccol, dir):
    if dir==0: #search left in same row
        for i in range(ccol):
            if array[crow,ccol-1-i] >=0:
                return crow,ccol-1-i,array[crow,ccol-1-i]
        return 0,0,0
    elif dir==1: #search right in same row
        for i in range(numcols-ccol):
            if array[crow,ccol+1+i] >=0:
                return crow,ccol+1+i,array[crow,ccol+1+i]
        return 0,0,0
    elif dir==2: #search up in same col
        for i in range(crow):
            if array[crow-1-i,ccol] >=0:
                return crow-1-i,ccol,array[crow-1-i,ccol]
        return 0,0,0
    elif dir==3: #search down in same col
        for i in range(numrows-crow):
            if array[crow+1+i,ccol] >=0:
                return crow+1+i,ccol,array[crow+1+i,ccol]
        return 0,0,0
    elif dir==4: #search left up diagonal
        for i in range(min(ccol,crow)):
            if array[crow-1-i,ccol-1-i] >=0:
                return crow-1-i,ccol-1-i,array[crow-1-i,ccol-1-i]
        return 0,0,0
    elif dir==5: #search right in same row
        for i in range(min(numcols-ccol,numrows-crow)):
            if array[crow+1+i,ccol+1+i] >=0:
                return crow+1+i,ccol+1+i,array[crow+1+i,ccol+1+i]
        return 0,0,0
    elif dir==6: #search up in same col
        for i in range(min(crow,numcols-ccol)):
            if array[crow-1-i,ccol+i+1] >=0:
                return crow-1-i,ccol+i+1,array[crow-1-i,ccol+i+1]
        return 0,0,0
    else: #search down in same col
        for i in range(min(numrows-crow,ccol)):
            if array[crow+1+i,ccol-i-1] >=0:
                return crow+1+i,ccol-i-1,array[crow+1+i,ccol-i-1]
        return 0,0,0

itr=0
while True:
    for i in range(numrows+2):
        if i==0 or i==numrows+1:
            continue
        for j in range(numcols+2):
            if j == 0 or j == numcols+1:
                continue
            #submatrix = occupancy[i-1:i+2,j-1:j+2]
            #neighbours = sum(submatrix[submatrix==1])
            neighbours = 0
            _,_,l = GetFirstVisible(occupancy,i,j,0)
            _, _, r = GetFirstVisible(occupancy, i, j, 1)
            _, _, u = GetFirstVisible(occupancy, i, j, 2)
            _, _, d = GetFirstVisible(occupancy, i, j, 3)
            _, _, lu = GetFirstVisible(occupancy, i, j, 4)
            _, _, rd = GetFirstVisible(occupancy, i, j, 5)
            _, _, ru = GetFirstVisible(occupancy, i, j, 6)
            _, _, ld = GetFirstVisible(occupancy, i, j, 7)
            neighbours = l+r+u+d+lu+ld+ru+rd
            if occupancy[i,j]==0 and neighbours == 0:
                newoccupancy[i,j] = 1
            elif occupancy[i,j]==1 and neighbours >= 5:
                newoccupancy[i, j] = 0
    change = occupancy-newoccupancy
    if len(change[change==0]) == (numrows+2)*(numcols+2):
        break
    else:
        occupancy = newoccupancy.copy()
    print(itr)
    itr+=1
#print(occupancy)
print(sum(occupancy[occupancy==1]))
