import re
from day7 import Tree

file = open("input.txt","r")
lines = file.readlines()
nodes = []
removelist = []
for line in lines:
    words = [val.strip() for val in re.split('contains|contain| |,',line)]
    words2 = words.copy()
    cover = ""
    for w in words2:
        if w=='':
            words.remove(w)
            continue
        elif w=="bag" or w=="bags":
            words.remove(w)
            break
        else:
            cover += w
            words.remove(w)
    covernode = None
    #if cover == "stripedblack":
    #    print("d")
    for node in nodes:
        covernode = node.findnode(cover)
        if covernode:
            break
    if covernode == None:
        covernode = Tree.Tree(cover,1)
        nodes.append(covernode)
    content = ""
    numcontents = []
    contents = []
    for w in words:
        if w=='':
            continue
        elif w.isdigit():
            numcontents += [int(w)]
            content = ""
        elif w == "bag." or w == "bags.":
            contents += [content]
            break
        elif w=="bag" or w=="bags":
            contents += [content]
            content = ""
        else:
            content += w
    for idx, content in enumerate(contents):
        if content == "noother":
            continue
        contentnode = None
        #if content == "stripedblack":
        #    print("d")
        for node in nodes:
            contentnode = node.findnode(content)
            if contentnode:
                break
        if contentnode is not None and contentnode.level == 1:
            nodes.remove(contentnode)
        elif contentnode == None:
            contentnode = Tree.Tree(content,numcontents[idx])
        else:
            pass
        contentnode.updatelevel(covernode.level)
        covernode.insert(contentnode, numcontents[idx])
""""
coverbags = []
for node in nodes:
    print(node.name)
    paths = node.getnodepath("shinygold")
    for path in paths:
        for bag in path:
            if bag == "shinygold":
                continue
            else:
                if not coverbags.__contains__(bag):
                    coverbags += [bag]
print(coverbags)
print(len(coverbags))
"""
shinygold = None
for node in nodes:
    shinygold = node.findnode("shinygold")
    if shinygold:
        break
print(shinygold.getnestedchildcount()-1)