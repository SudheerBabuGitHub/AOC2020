file = open("input.txt","r")
lines = file.readlines()

numLines = len(lines)
print(numLines)
lineLength = len(lines[0]) - 1 #line termination
print(lineLength)

JUMP_RIGHT_SIZE = [1, 3, 5, 7, 1]
JUMP_DOWN_SIZE = [1, 1, 1, 1, 2]

product = 1

for i, _ in enumerate(JUMP_RIGHT_SIZE):
    treeCount = 0
    right = JUMP_RIGHT_SIZE[i]
    down = JUMP_DOWN_SIZE[i]
    for idx, line in enumerate(lines):
        if idx % down != 0:
            continue
        pos = (int(idx/down)*right) % lineLength
        if line[pos] == '#':
            treeCount += 1
    #print(i, treeCount)
    product *= treeCount

print(product)