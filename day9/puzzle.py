PREAMBLE_LENGTH = 25

def IsDataValid(preamble, num):
    FoundPair = False
    for i,num1 in enumerate(preamble):
        for j, num2 in enumerate(preamble[i+1:]):
            if num1+num2 == num:
                FoundPair = True
                break
        if FoundPair:
            break
    return FoundPair

def FindContiguousSet(set, num):
    stidx = 0
    endidx = 1
    FoundSum = False
    while True:
        setsum = sum(set[stidx:endidx+1])
        if setsum == num:
            FoundSum = True
            break
        elif setsum < num:
            endidx += 1
        elif setsum > num:
            stidx += 1
        if stidx == endidx:
            endidx += 1
    return stidx, endidx

file = open("input.txt","r")
lines = file.readlines()
data = [int(line.strip()) for line in lines]
numdata = len(data)
weakness = 0
for i in range(numdata-PREAMBLE_LENGTH):
    preamble = data[i:i+PREAMBLE_LENGTH]
    if IsDataValid(preamble,data[i+PREAMBLE_LENGTH]):
        continue
    else:
        print(data[i+PREAMBLE_LENGTH])
        weakness = data[i+PREAMBLE_LENGTH]
        break
stidx,endidx = FindContiguousSet(data, weakness)
print(stidx,endidx)
print(max(data[stidx:endidx+1])+min(data[stidx:endidx+1]))