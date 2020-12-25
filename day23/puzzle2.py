class CircularQueue():
    def __init__(self, values, max_val):
        self.next_value = {}
        self.max_val = max_val
        self.top = values[0]
        for idx, value in enumerate(values):
            if idx == len(values)-1:
                self.next_value[value] = values[0]
            else:
                self.next_value[value] = values[idx+1]

    def single_step(self):
        val1 = self.next_value[self.top]
        val2 = self.next_value[val1]
        val3 = self.next_value[val2]
        val4 = self.next_value[val3]
        self.next_value.update({self.top:val4})
        dest_val = self.top
        found_dest = False
        while not found_dest:
            dest_val -= 1
            if dest_val==0:
                dest_val = self.max_val
            if not [val1,val2,val3].__contains__(dest_val):
                found_dest = True
        self.next_value.update({val3:self.next_value[dest_val]})
        self.next_value.update({dest_val:val1})
        self.top = self.next_value[self.top]

    def getstring(self,start_idx = -1):
        curr_val = start_idx
        if start_idx == -1:
            curr_val = self.top
        start_val = curr_val
        queue_string = str(curr_val)
        curr_val = self.next_value[curr_val]
        while curr_val != start_val:
            queue_string += str(curr_val)
            curr_val = self.next_value[curr_val]
        return queue_string


#cups = [3,8,9,1,2,5,4,6,7]
cups = [3,9,8,2,5,4,7,1,6]
for num in range(10,1000001):
    cups += [num]
CUPS = CircularQueue(cups,1000000)
itr = 0
while itr<10000000:
    #print(CUPS.getstring())
    CUPS.single_step()
    if itr%10000 == 0:
        print(itr)
    itr+=1
#print(CUPS.getstring(1))
val1 = CUPS.next_value[1]
val2 = CUPS.next_value[val1]
print(val1,val2)