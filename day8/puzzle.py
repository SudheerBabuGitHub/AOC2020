class BootCode:
    def __init__(self):
        self.accumulator = 0
        self.pcntr = 0
        self.iset = ["nop","acc","jmp"]

    def reset(self):
        self.accumulator = 0
        self.pcntr = 0

    def execute(self, instruction, args):
        if instruction == "nop":
            self.pcntr += 1
            return
        elif instruction == "acc":
            self.accumulator += args[0]
            self.pcntr += 1
            return
        elif instruction == "jmp":
            self.pcntr += args[0]
            return
        else:
            return

file = open("input.txt","r")
lines = file.readlines()
"""
bootcode = BootCode()
addrhistory = []
while True:
    currptr = bootcode.pcntr
    line = lines[currptr]
    if addrhistory.__contains__(currptr):
        print(bootcode.accumulator)
        break
    else:
        addrhistory += [currptr]
        instruction = line[0:3]
        sign = line[4]
        argument = int(line[5:].strip())
        if sign=='-':
            argument *= -1
        #print(instruction,argument)
        bootcode.execute(instruction,[argument])
"""
def RunCode(bootcode, code):
    addrhistory = []
    numlines = len(code)
    while True:
        line = ""
        currptr = bootcode.pcntr
        if currptr >= numlines or line == '\n':
            print(bootcode.accumulator)
            return 0
        else:
            line = code[currptr]
        if addrhistory.__contains__(currptr):
            print(bootcode.accumulator)
            return -1
        else:
            addrhistory += [currptr]
            instruction = line[0:3]
            sign = line[4]
            argument = int(line[5:].strip())
            if sign == '-':
                argument *= -1
            # print(instruction,argument)
            bootcode.execute(instruction, [argument])

bootcode = BootCode()
for idx,line in enumerate(lines):
    bootcode.reset()
    if line[0:3] == "nop":
        code = lines.copy()
        code[idx] = code[idx].replace("nop","jmp")
        #print(code)
        retval = RunCode(bootcode, code)
        if retval == 0:
            print("Bug patched")
            break;
    elif line[0:3] == "jmp":
        code = lines.copy()
        code[idx] = code[idx].replace("jmp","nop")
        #print(code)
        retval = RunCode(bootcode, code)
        if retval == 0:
            print("Bug patched")
            break;
    else:
        pass
