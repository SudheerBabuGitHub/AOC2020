class Tree:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.children = []
        self.numchildren = []
        self.level = 1

    def insert(self, node, num):
        self.children.append(node)
        self.numchildren.append(num)

    def setvalue(self, value):
        self.value = value

    def updatelevel(self, parentlevel):
        if self.level <= parentlevel:
            self.level = parentlevel+1
        if len(self.children) > 0:
            for child in self.children:
                child.updatelevel(self.level)
        else:
            pass

    def getnestedchildcount(self):
        cnt = 0
        if len(self.children) > 0:
            for idx, child in enumerate(self.children):
                cnt += self.numchildren[idx] * child.getnestedchildcount()
            cnt += 1
        else:
            cnt = 1
        return cnt

    def findnode(self,name):
        if self.name == name:
            return self
        elif len(self.children) > 0:
            for child in self.children:
                node = child.findnode(name)
                if node:
                    return node
                else:
                    pass
        else:
            return None

    def getnodepath(self, name):
        if self.name == name:
            return [[self.name]]
        elif len(self.children) > 0:
            paths = []
            for child in self.children:
                childpaths = child.getnodepath(name)
                for p in childpaths:
                    temp = p
                    temp += [self.name]
                    paths += [temp]
            return paths
        else:
            return []
