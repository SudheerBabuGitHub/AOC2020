def get_byr (record):
    #byr (Birth Year) - four digits; at least 1920 and at most 2002.
    chararray = list(record)
    recordlen = len(record)-1
    foundbyr = False
    byr = 0
    for idx,c in enumerate(chararray):
        if idx==recordlen-3-4:
            break
        elif chararray[idx]+chararray[idx+1]+chararray[idx+2] == "byr":
            idx += 4
            valid = True
            for i in range(4):
                if chararray[idx+i] < '0' or chararray[idx+i] > '9':
                    valid = False
                    break
                if not valid:
                    break
            if chararray[idx+4] != ' ' and chararray[idx+4] != '\n':
                break
            byr = int(chararray[idx] + chararray[idx+1] + chararray[idx+2] + chararray[idx+3])
            if byr >= 1920 and byr <= 2002:
                foundbyr = True
            break
        else:
            continue
    return foundbyr

def get_iyr (record):
    #iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    chararray = list(record)
    recordlen = len(record)-1
    foundbyr = False
    iyr = 0
    for idx,c in enumerate(chararray):
        if idx==recordlen-3-4:
            break
        elif chararray[idx]+chararray[idx+1]+chararray[idx+2] == "iyr":
            idx += 4
            valid = True
            for i in range(4):
                if chararray[idx+i] < '0' or chararray[idx+i] > '9':
                    valid = False
                    break
                if not valid:
                    break
            if chararray[idx+4] != ' ' and chararray[idx+4] != '\n':
                break
            iyr = int(chararray[idx] + chararray[idx+1] + chararray[idx+2] + chararray[idx+3])
            if iyr >= 2010 and iyr <= 2020:
                foundbyr = True
            break
        else:
            continue
    return foundbyr

def get_eyr (record):
    #eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    chararray = list(record)
    recordlen = len(record)-1
    foundbyr = False
    eyr = 0
    for idx,c in enumerate(chararray):
        if idx==recordlen-3-4:
            break
        elif chararray[idx]+chararray[idx+1]+chararray[idx+2] == "eyr":
            idx += 4
            valid = True
            for i in range(4):
                if chararray[idx+i] < '0' or chararray[idx+i] > '9':
                    valid = False
                    break
                if not valid:
                    break
            if chararray[idx+4] != ' ' and chararray[idx+4] != '\n':
                break
            eyr = int(chararray[idx] + chararray[idx+1] + chararray[idx+2] + chararray[idx+3])
            if eyr >= 2020 and eyr <= 2030:
                foundbyr = True
            break
        else:
            continue
    return foundbyr

def get_hgt (record):
    """"
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    """
    chararray = list(record)
    recordlen = len(record)-1
    foundbyr = False
    unit = ""
    value = ""
    hgt = 0
    for idx,c in enumerate(chararray):
        if idx==recordlen-3-4:
            break
        elif chararray[idx]+chararray[idx+1]+chararray[idx+2] == "hgt":
            idx += 4
            i = 0
            while chararray[idx+i] != ' ' and chararray[idx+i] != '\n':
                value += chararray[idx+i]
                i += 1
            unit = chararray[idx+i-2]+chararray[idx+i-1]
            if unit != "cm" and unit != "in":
                break
            if chararray[idx+i-2] == ':':
                break
            hgt = int(value[0:-2])
            if unit == "cm" and (hgt >= 150 and hgt<=193):
                foundbyr = True
            elif unit == "in" and (hgt >= 59 and hgt<=76):
                foundbyr = True
            break
        else:
            continue
    return foundbyr

def get_hcl (record):
    #hcl(HairColor) - a  # followed by exactly six characters 0-9 or a-f.
    chararray = list(record)
    recordlen = len(record)-1
    foundbyr = False
    for idx,c in enumerate(chararray):
        if idx==recordlen-3-7:
            break
        elif chararray[idx]+chararray[idx+1]+chararray[idx+2] == "hcl":
            idx += 4
            if chararray[idx] != '#':
                break
            idx += 1
            valid = True
            for i in range(6):
                if chararray[idx + i] < '0' or chararray[idx + i] > 'f':
                    valid = False
                    break
                if chararray[idx + i] > '9' and chararray[idx + i] < 'a':
                    valid = False
                    break
            if not valid:
                break
            if chararray[idx+6] != ' ' and chararray[idx+6] != '\n':
                break
            foundbyr = True
            break
        else:
            continue
    return foundbyr

def get_ecl (record):
    #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    chararray = list(record)
    recordlen = len(record)-1
    foundbyr = False
    ecl = ""
    colours = ["amb","blu","brn","gry","grn","hzl","oth"]
    for idx,c in enumerate(chararray):
        if idx==recordlen-3-3:
            break
        elif chararray[idx]+chararray[idx+1]+chararray[idx+2] == "ecl":
            idx += 4
            ecl = chararray[idx] + chararray[idx + 1] + chararray[idx + 2]
            if chararray[idx+3] != ' ' and chararray[idx+3] != '\n':
                break
            for colour in colours:
                if colour == ecl:
                    foundbyr = True
                    break
            break
        else:
            continue
    return foundbyr

def get_pid (record):
    #pid (Passport ID) - a nine-digit number, including leading zeroes.
    chararray = list(record)
    recordlen = len(record)-1
    foundbyr = False
    for idx,c in enumerate(chararray):
        if idx==recordlen-3-9:
            break
        elif chararray[idx]+chararray[idx+1]+chararray[idx+2] == "pid":
            idx += 4
            valid = True
            for i in range(9):
                if chararray[idx+i] <'0' or chararray[idx+i] > '9':
                    valid = False
                    break
            if not valid:
                break
            if chararray[idx+9] != ' ' and chararray[idx+9] != '\n':
                break
            foundbyr = True
            break
        else:
            continue
    return foundbyr

def get_cid (record):
    #cid (Country ID) - ignored, missing or not.
    chararray = list(record)
    recordlen = len(record)-1
    foundbyr = False
    for idx,c in enumerate(chararray):
        if idx==recordlen-3:
            break
        elif chararray[idx]+chararray[idx+1]+chararray[idx+2] == "cid":
            foundbyr = True
            break
        else:
            continue
    return foundbyr

file = open("input.txt","r")
lines = file.readlines()
validcnt = 0
record = ""
for line in lines:
    if line != "\n":
        record += line
        continue
    else:
        if get_byr(record) == False:
            #print("missing byr")
            record = ""
            continue
        if get_iyr(record) == False:
            #print("missing iyr")
            record = ""
            continue
        if get_eyr(record) == False:
            #print("missing eyr")
            record = ""
            continue
        if get_hgt(record) == False:
            #print("missing hgt")
            record = ""
            continue
        if get_hcl(record) == False:
            #print("missing hcl")
            record = ""
            continue
        if get_ecl(record) == False:
            #print("missing ecl")
            record = ""
            continue
        if get_pid(record) == False:
            #print("missing pid")
            record = ""
            continue
        #get_cid(record)
        record = ""
        validcnt += 1
print(validcnt)
