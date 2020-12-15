import re
import math

file = open("input.txt","r")
lines = file.readlines()
"""
# PART1
set = 0
reset = 0
memory = {}
for i in range(len(lines)):
    location = 0
    value = 0
    if str(lines[i][0:4]) == "mask":
        maskstr = lines[i][7:].strip()
        set = int(maskstr.replace("X","0"),2)
        reset = int(maskstr.replace("X","1"),2)
        #print(set)
        #print(reset)
    else:
        location = int(re.split('mem|\[|\]| |=',lines[i])[2].strip())
        value = int(re.split('mem|\[|\]| |=',lines[i])[6].strip())
        value |= set
        value &= reset
        if memory.get(location) == None:
            memory[location] = value
        else:
            memory.update({location:value})
sum = 0
for key in memory.keys():
    sum += memory.get(key)
print(sum)
"""

#PART 2
def IsMatching(str1,str2):
    match = []
    matchcnt = 0
    singlematch = ""
    for i,c in enumerate(str1):
        if c==str2[i] and c != 'X':
            singlematch += c
        elif c==str2[i]:
            match += [i]
            matchcnt += 1
        elif c=='X' and str2[i] != 'X':
            singlematch += str2[i]
        elif str2[i] == 'X' and c != 'X':
            singlematch += c
        else:
            return False,0,0
    if matchcnt>=1:
        return True,match,matchcnt
    else:
        return  True,"".join(singlematch),0

def CountFloating(mask):
    count = 0
    for c in mask:
        if c=='X':
            count += 1
    return count

def decimalToBinary(n,w):
    binstr = bin(n).replace("0b", "")
    length = len(binstr)
    while length<w:
        binstr = '0'+binstr
        length += 1
    return binstr
memory = {}
maskstrs = []
values = []
maskstr = ""
for i in range(len(lines)):
    if str(lines[i][0:4]) == "mask":
        maskstr = lines[i][7:].strip()
    elif str(lines[i][0:3]) == "mem":
        location = int(re.split('mem|\[|\]| |=',lines[i])[2].strip())
        value = int(re.split('mem|\[|\]| |=', lines[i])[6].strip())
        locationstr = list(decimalToBinary(location,36))
        for i,c in enumerate(maskstr):
            if c != '0':
                locationstr[i] = c
        maskstrs += ["".join(locationstr)]
        values += [value]
for i, mask in enumerate(maskstrs):
    count = CountFloating(mask)
    if count>=1:
        for num in range(int(math.pow(2,count))):
            binstr = decimalToBinary(num,count)
            address = []
            xcnt = 0
            for c in mask:
                if c == 'X':
                    address += [binstr[xcnt]]
                    xcnt+=1
                else:
                    address += [c]
            address = "".join(address)
            if memory.get(address) == None:
                memory[address] = values[i]
            else:
                memory.update({address: values[i]})
    else:
        if memory.get(mask) == None:
            memory[mask] = values[i]
        else:
            memory.update({mask: values[i]})
sum = 0
for key in memory.keys():
    sum += memory.get(key)
print(sum)
"""
sum = 0
for i, mask in enumerate(maskstrs):
    count = CountFloating(mask)
    matchsets = []
    matchids = []
    matchstrs = []
    for j in range(i + 1, len(maskstrs)):
        matchflag, match, matchcnt = IsMatching(mask, maskstrs[j])
        if matchflag:
            if matchcnt == 0:
                matchstrs += [match]
            else:
                matchids += [j]
                matchset = set(match)
                matchsets += [matchset]
    #check if the single strings are already accounted for
    for singlestr in matchstrs:
        present = False
        for idx in matchids:
            matchflag, match, matchcnt = IsMatching(singlestr, maskstrs[idx])
            if matchflag:
                present = True
                break
        if not present:
            count -= 1
    #tackle the sets
    numcommon = 0
    if len(matchsets)>1:
        common = set.intersection(*matchsets)
        numcommon = len(common)
    for s in matchsets:
        n = len(s) - numcommon
        if n>0:
            count -= math.pow(2,n)
    if numcommon>0:
        count -= math.pow(2,numcommon)
    if count<0:
        print(count)
    sum += (count*values[i])
print(sum)
"""