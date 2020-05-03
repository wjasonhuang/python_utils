'''
Heap with remove operation via heapq + dict
'''

import heapq


class MinHeap():
    def __init__(self):
        self.heap = []
        self.to_remove = dict()
        self.size = 0

    def heappush(self, val):
        heapq.heappush(self.heap, val)
        self.size += 1

    def heappop(self):  # only return when heap not empty
        while self.heap:
            ret = heapq.heappop(self.heap)
            if self.to_remove.get(ret, 0) > 0:
                self.to_remove[ret] -= 1
                continue
            self.size -= 1
            return ret

    def remove(self, val):
        self.to_remove[val] = self.to_remove.get(val, 0) + 1
        self.size -= 1
