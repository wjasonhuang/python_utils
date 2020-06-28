'''
Heap with remove by value operation via heapq + dict
'''

import heapq


class MinHeap:
    def __init__(self, heap):
        self.heap = heap
        self.size = len(heap)
        heapq.heapify(self.heap)
        self.to_remove = dict()

    def heappush(self, val):
        heapq.heappush(self.heap, val)
        self.size += 1

    def heappop(self):  # only return when heap not empty
        assert (self.size > 0)
        self.__update()
        self.size -= 1
        return heapq.heappop(self.heap)

    def heapmin(self):
        assert (self.size > 0)
        self.__update()
        return self.heap[0]

    def remove(self, val):
        self.to_remove[val] = self.to_remove.get(val, 0) + 1
        self.size -= 1

    def empty(self):
        return self.size == 0

    def __update(self):
        while self.heap and self.to_remove.get(self.heap[0], 0) > 0:
            self.to_remove[heapq.heappop(self.heap)] -= 1
