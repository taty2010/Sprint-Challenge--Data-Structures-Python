from collections import deque
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
    def append(self, item):
        c = len(self.storage)
        if c < self.capacity:
            self.storage.append(item)
        if c is self.capacity:
            current = self.storage[0]
            next_item = 0
            self.storage.pop(0)
            self.storage.append(item)
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