def GetCount(line):
    chararray = list(line)
    lines = line.split('\n')
    lines.remove('')
    distinct = []
    common = []
    """
    for c in chararray:
        if c=='\n':
            continue
        elif distinct.__contains__(c):
            continue
        else:
            distinct += [c]
    return len(distinct)
    """
    for c in list("abcdefghijklmnopqrstuvwxyz"):
        notFound = False
        for l in lines:
            if not list(l).__contains__(c):
                notFound = True
                break
        if not notFound:
            common += [c]
    return len(common)

file = open("input.txt","r")
lines = file.readlines()

cnt = 0
group = ""
for line in lines:
    if line != '\n':
        group += line
    else:
       cnt += GetCount(group)
       group = ""
print(cnt)