import copy

file = open("input.txt","r")
lines = file.readlines()
valid_count = 0
for line in lines:
    char_array = list(line)
    char_array2 = char_array.copy()
    llimit = ""
    ulimit = ""
    symbol = 'a'
    # find lower limit
    for c in char_array:
        if c != '-':
            llimit += c
            char_array2.remove(c)
        else:
            char_array2.remove(c)
            break
    # find upper limit
    char_array = char_array2.copy()
    for c in char_array:
        if c != ' ':
            ulimit += c
            char_array2.remove(c)
        else:
            char_array2.remove(c)
            break
    symbol = char_array2[0]
    char_array2.remove(symbol)
    char_array2.remove(':')
    char_array2.remove(' ')
    # check
    char_array = char_array2.copy()
    #count = 0
    #for c in char_array:
    #    if c == symbol:
    #        count += 1
    #if count >= int(llimit) and count <= int(ulimit):
    #    valid_count += 1
    char_pos1 = char_array[int(llimit)-1]
    char_pos2 = char_array[int(ulimit) - 1]
    if char_pos1 == symbol and char_pos2 != symbol:
        valid_count += 1
    elif char_pos2 == symbol and char_pos1 != symbol:
        valid_count += 1
    else:
        pass

print(valid_count)