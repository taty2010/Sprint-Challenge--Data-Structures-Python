from collections import deque
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.current = 0
    def append(self, item):
        c = len(self.storage)
        if c is self.capacity:
            self.storage[self.current]= item
            if self.current + 1 is self.capacity:
                self.current = 0
            else:
                self.current +=1
        else: 
            self.storage.append(item)
            return item
        # if c < self.capacity:
        #     self.storage.append(item)
        # if c is self.capacity:
        #     current = self.storage[0]
        #     next_item = 0
        #     while next_item is not self.capacity:
        #         next_item = next_item + 1 
        #         print(next_item)
        #     self.storage.pop(next_item - 1)
        #     self.storage.insert(next_item, item)
        # if c is not self.capacity:
        #     self.storage.append(item)
        # elif c is self.capacity:
        #     self.storage.pop(0)
        #     self.storage.insert(0,item)
        # else:
        #     self.storage.pop(0)
        #     self.storage.append(item)
        

    def get(self):
        while self.storage is not None:
            return self.storage