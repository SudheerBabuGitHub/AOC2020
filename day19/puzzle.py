import re

def RuleToList(rule):
    parts = re.split(' \| ',rule)
    rulelist = []
    for part in parts:
        partlist = part.split(' ')
        rulelist += [partlist]
    return rulelist

def GetNestedRules(rules_dict, rulenum, max_len, total_len = 0):
    rule = rules_dict.get(rulenum)
    subrules = RuleToList(rule)
    if not subrules[0][0].isdigit():
        return subrules[0]
    else:
        allrules = []
        for subrule in subrules:
            rulestr = [""]
            rulestrcopy = []
            curr_len = 0
            for idx,num in enumerate(subrule):
                curr_len = total_len+len(rulestr[0])
                #print(curr_len)
                if curr_len >= max_len:
                    continue
                rulestr_1 = GetNestedRules(rules_dict, num, max_len, curr_len)
                for s in rulestr:
                    for ss in rulestr_1:
                        rulestrcopy += [s+ss]
                if rulestrcopy != []:
                    rulestr = rulestrcopy.copy()
                rulestrcopy = []
            allrules += rulestr
        return allrules

file = open("input.txt","r")
lines = file.readlines()
RULES = {}
messages = []
for line in lines:
    if line[0].isdigit():
        [rulenum, rule] = re.split(': ',line)
        if rule[0] == '"':
            rule = rule[1]
        RULES[rulenum] = rule.strip()
    elif line!='\n':
        messages += [line.strip()]
max_seq_len = max([len(message) for message in messages if message != ''])

SEQUENCES = {}
sequences = GetNestedRules(RULES, '8', max_len=max_seq_len)
len_8 = len(sequences[0])
SEQUENCES[8] = set(sequences)

sequences = GetNestedRules(RULES, '11', max_len=max_seq_len)
len_11 = len(sequences[0])
SEQUENCES[11] = set(sequences)

sequences = GetNestedRules(RULES, '42', max_len=max_seq_len)
len_42 = len(sequences[0])
SEQUENCES[42] = set(sequences)

sequences = GetNestedRules(RULES, '31', max_len=max_seq_len)
len_31 = len(sequences[0])
SEQUENCES[31] = set(sequences)

def Check_42(seq):
    if SEQUENCES.get(42).__contains__(seq):
        return True
    else:
        return False

def Check_31(seq):
    if SEQUENCES.get(31).__contains__(seq):
        return True
    else:
        return False

#PART 2
#RULES.update({'8':"42 | 42 8"})
#RULES.update({'11':"42 31 | 42 11 31"})

match = 0
#0: 8 11
for msgnum,message in enumerate(messages):
    #if message == "aaabbbbbbaaaabaababaabababbabaaabbababababaaa":
    #    print("a")
    msglen = len(message)
    valid = True
    curridx = 0
    seq_8_11 = []
    cnt_42 = 0
    cnt_31 = 0
    match_42 = Check_42(message[curridx:curridx + len_42])
    if not match_42:
        continue
    else:
        cnt_42 += 1
        curridx += len_42
        seq_8_11 += [42]
    prev_match = 42
    while curridx != msglen:
        match_42 = Check_42(message[curridx:curridx+len_42])
        match_31 = Check_31(message[curridx:curridx+len_31])
        if prev_match == 42 and match_42:
            cnt_42 += 1
            curridx += len_42
            seq_8_11 += [42]
            prev_match = 42
        elif match_31:
            cnt_31 += 1
            curridx += len_31
            seq_8_11 += [31]
            prev_match = 31
        elif curridx != msglen:
            valid = False
            break
    if prev_match == 42 or cnt_31>=cnt_42:
        valid = False
    if valid:
        match += 1
        print(message,seq_8_11)
print(match)
