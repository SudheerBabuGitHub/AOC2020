import re

def EvaluateSimple1(expression):
    digits = [val for val in re.split('\+|\*|\(|\)',expression) if val != '']
    result = int(digits[0])
    digits.remove(digits[0])
    for c in list(expression):
        if c == '*':
            result *= int(digits[0])
            digits.remove(digits[0])
        elif c == '+':
            result += int(digits[0])
            digits.remove(digits[0])
        else:
            pass
    return result

def EvaluateSimple2(expression):
    digits = [val for val in re.split('\+|\*|\(|\)',expression) if val != '']
    """
    digitstr = "\(|\)|"
    for digit in digits:
        digitstr += digit
        digitstr += '|'
    digitstr = digitstr[0:-1]
    operations = [val for val in re.split(digitstr,expression) if val != '']
    """
    operations = []
    for c in expression:
        if c=='+' or c=='*':
            operations += [c]
    doAdd = True
    while doAdd:
        doAdd = False
        for idx,operation in enumerate(operations):
            if operation == '+':
                sum = int(digits[idx])+int(digits[idx+1])
                digits[idx] = str(sum)
                digits[idx+1] = -1
                digits.remove(-1)
                operations.remove('+')
                doAdd = True
                break
    result = 1
    for digit in digits:
        result *= int(digit)
    return result

def FindSimple(expression):
    parts = re.split(' |\n', expression)
    lastopen = -1
    firstclose = len(parts)
    for idx,part in enumerate(parts):
        if part == '\n':
            continue
        if len(part)>1 and part[0] == '(':
            lastopen = idx
            continue
        elif len(part)>1 and part[len(part)-1] == ')':
            firstclose = idx
            break
    if lastopen>-1:
        return True, lastopen, firstclose
    else:
        return False, lastopen, firstclose


file = open("input.txt","r")
lines = file.readlines()
sum = 0
for line in lines:
    isComplex = True
    line = line.strip()
    while isComplex:
        parts = re.split(' |\n', line)
        isComplex, stidx, endidx = FindSimple(line)
        if isComplex:
            result = EvaluateSimple2("".join(parts[stidx:endidx+1]))
        else:
            result = EvaluateSimple2("".join(parts[0:endidx]))
        if isComplex:
            characters = list(parts[stidx])
            simple = "("
            for c in characters:
                if c!='(':
                    simple += c
            simple += ' '
            for i in range(1,endidx-stidx):
                simple += parts[stidx+i]
                simple += " "
            characters = list(parts[endidx])
            for c in characters:
                if c != ')':
                    simple += c
            simple += ')'
            line = line.replace(simple, str(result))
        else:
            #print(result)
            sum += result
            line = str(result)
        #print(line)
print(sum)