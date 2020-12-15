import re
import numpy as np

file = open("input.txt","r")
lines = file.readlines()
timestamp = int(lines[0].strip())
"""
#PART 1
ids = [int(val.strip()) for val in re.split(',',lines[1]) if val != 'x']
#print(timestamp)
#print(ids)
wait = []
for id in ids:
    if id<=timestamp:
        rem = timestamp%id
        if rem>0:
            wait += [id-rem]
        else:
            wait += [0]
    else:
        wait += [id-timestamp]
minwait = min(wait)
print(minwait*ids[np.argmin(wait)])
"""
#PART 2
ids = [int(val.strip()) for val in re.split(',',lines[1]) if val != 'x']
idx = [idx for idx,val in enumerate(re.split(',',lines[1])) if val != 'x']
i = 0
st = ids[0]
period = ids[0]
curr_idx = 0
print(st,period)
while True:
    candidate = st+i*period
    i+=1
    if (candidate+idx[curr_idx+1])%ids[curr_idx+1] == 0:
        curr_idx+=1
        if curr_idx == len(ids)-1:
            print(candidate)
            break
        else:
            period*=ids[curr_idx]
            st = candidate
            i=0
            print(st, period)