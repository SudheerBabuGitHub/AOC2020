class CircularQueue():
    def __init__(self,vals):
        self.queue = vals
        self.top = 0
        self.length = len(vals)

    def leftIdx(self,idx):
        left = idx-1
        if left<0:
            left += self.length
        return left

    def rightIdx(self,idx):
        return (idx+1)%self.length

    def popRight(self,idx):
        right = self.rightIdx(idx)
        val = self.queue.pop(right)
        self.length -= 1
        if right<self.top:
            self.top -= 1
        return val

    def insertRight(self,idx,value):
        right = self.rightIdx(idx)
        self.queue.insert(right,value)
        self.length += 1
        if right<=self.top:
            self.top += 1

    def getQueue(self):
        return self.queue

    def shiftRight(self):
        newTop = self.rightIdx(self.top)
        self.top = newTop

    def findIdx(self,val):
        if self.queue.__contains__(val):
            return self.queue.index(val)
        else:
            return -1

    def getTop(self):
        return self.queue[self.top]

    def getString(self):
        idx = self.top
        queuestring = ""
        for i in range(self.length):
            queuestring += str(self.queue[idx])
            idx = self.rightIdx(idx)
        return queuestring

history = []
CUPS = CircularQueue([3,8,9,1,2,5,4,6,7])
#CUPS = CircularQueue([3,9,8,2,5,4,7,1,6])
min_val = 1
max_val = 9
for i in range(max_val+1,100+1):
    CUPS.insertRight(CUPS.leftIdx(CUPS.top),i)
    max_val = i
#print(CUPS.getQueue())
history += [CUPS.getString()]
itr = 0
while itr<100:
    cup1 = CUPS.popRight(CUPS.top)
    cup2 = CUPS.popRight(CUPS.top)
    cup3 = CUPS.popRight(CUPS.top)
    curr_val = CUPS.getTop()
    dest_idx = 0
    i = 1
    while i<(max_val-1):
        val = curr_val-i
        if val <= 0:
            val+=max_val
        idx = CUPS.findIdx(val)
        if idx == -1:
            i+=1
        else:
            dest_idx = idx
            break
    CUPS.insertRight(dest_idx,cup1)
    idx = CUPS.findIdx(cup1)
    CUPS.insertRight(idx, cup2)
    idx = CUPS.findIdx(cup2)
    CUPS.insertRight(idx, cup3)
    currstr = CUPS.getString()
    CUPS.shiftRight()
    if itr==40:
        print('d')
    if itr%100 == 0:
        print("iteration:",itr)
    itr += 1
#list = CUPS.getQueue()
#liststr = ""
#idx = list.index(1)
#i = 0
#while i<max_val-1:
#    idx = CUPS.rightIdx(idx)
#    liststr += str(list[idx])
#    i+=1
#print(liststr)

