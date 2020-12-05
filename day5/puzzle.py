def ParseStringToNum(ipstring):
    row = 0
    col = 0
    row_max = 128
    col_max = 8
    for i, c in enumerate(ipstring):
        if c=='\n':
            break
        if c=='B':
            row += row_max/2
            row_max /= 2
        if c== 'F':
            row_max /= 2
        if c=='R':
            col += col_max/2
            col_max /= 2
        if c=='L':
            col_max /= 2
    return int(row),int(col)


file = open("input.txt","r")
lines = file.readlines()

max_ID = 0
seat_ID = []
for line in lines:
    row, col = ParseStringToNum(line)
    seat_ID += [8*row+col]
    if 8*row+col > max_ID:
        max_ID = 8*row+col
#print(max_ID)
seat_ID.sort()
for i,_ in enumerate(seat_ID):
    if seat_ID[i+1]-seat_ID[i]==2:
        print(seat_ID[i],seat_ID[i+1])
        break
