file = open("input.txt","r")
lines = file.readlines()
stnums = [int(val) for val in lines[0].split(',')]
print(stnums)
history = {}
for i,num in enumerate(stnums):
    history[num] = i+1
idx = len(stnums)+1
lastnum = 0
while idx<30000000:
    #print(idx,lastnum)
    #print(history.items())
    if history.get(lastnum) == None:
        history[lastnum] = idx
        lastnum = 0
    else:
        temp = idx-history.get(lastnum)
        history.update({lastnum:idx})
        lastnum = temp
    idx+=1
print(lastnum)