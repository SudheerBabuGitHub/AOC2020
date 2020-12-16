import re
import numpy as np

file = open("input.txt","r")
lines = file.readlines()
fields = {}
ticketnumslist = []
myticketnums = []
isticketnum = False
ismyticket = False
for line in lines:
    words = re.split(' |,|:|-|\n',line)
    if isticketnum:
        ticketnums = [int(val.strip()) for val in words if val != '']
        ticketnumslist += [ticketnums]
    if ismyticket:
        myticketnums = [int(val.strip()) for val in words if val != '']
        ismyticket = False
    elif words[0]+words[1] == "nearbytickets":
        isticketnum = True
    elif words[0]+words[1] == "yourticket":
        ismyticket = True
    elif words[0].isdigit() is False and words[0] != '':
        ranges = []
        name = ""
        for word in words:
            if word.isdigit():
                ranges += [int(word)]
            elif word != "or":
                name+=word
        fields[name] = ranges
#print(ticketnumslist)
#print(fields.items())
invalidcnt = 0
validtickets = [myticketnums]
for ticketnums in ticketnumslist:
    isvalidTicket = True
    for num in ticketnums:
        isvalid = False
        for key in fields.keys():
            ranges = fields.get(key)
            if num>=ranges[0] and num<=ranges[1]:
                isvalid = True
                break
            elif num>=ranges[2] and num<=ranges[3]:
                isvalid = True
                break
        if not isvalid:
            invalidcnt += num
            isvalidTicket = False
    if isvalidTicket:
        validtickets += [ticketnums]
print(invalidcnt)
validtickets = np.array(validtickets)
numfields = validtickets.shape[1]
for itr in range(20):
    orderedfields = []
    for i in range(numfields):
        if validtickets[0,i] == -1:
            orderedfields += [[]]
            continue
        labels = []
        values = validtickets[:,i]
        for key in fields.keys():
            ranges = fields.get(key)
            allvalid = True
            for value in values:
                if value<ranges[0]:
                    allvalid = False
                    break
                elif value>ranges[1] and value<ranges[2]:
                    allvalid = False
                    break
                elif value>ranges[3]:
                    allvalid = False
                    break
            if allvalid:
                labels += [key]
        orderedfields += [labels]
    for idx,labels in enumerate(orderedfields):
        if len(labels)==1:
            print(idx,labels[0])
            fields.pop(labels[0])
            validtickets[:,idx] = -1
print(myticketnums[6]*myticketnums[15]*myticketnums[17]*myticketnums[4]*myticketnums[5]*myticketnums[18])