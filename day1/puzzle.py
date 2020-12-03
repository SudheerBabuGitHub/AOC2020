file = open("input1.txt","r")
lines = file.readlines()
entries = [int(line) for line in lines]
numEntries = len(entries)

entryFound = False
for idx,val in enumerate(entries):
    entry1 = val
    for i in range(numEntries-idx-1):
        entry2 = entries[idx+i+1]
        for j in range(numEntries-idx-1-i-1):
            if entry1 + entry2 + entries[idx+i+1+j+1] == 2020:
                print(entry1*entry2*entries[idx+i+1+j+1])
                entryFound = True
                break
        if entryFound:
            break
    if entryFound:
        break