'''
Minimum Spanning Tree Prim's Algorithm O(|E|log|V|)
https://en.wikipedia.org/wiki/Prim%27s_algorithm
'''

class Heap():
    def __init__(self, n):
        self.array = []
        self.size = -1
        self.pos = [-1] * n
        self.inf = 99999999
    
    def swap(self, pos1, pos2):
        self.array[pos1], self.array[pos2] = (self.array[pos2], self.array[pos1])
        self.pos[self.array[pos1][1]] = pos1
        self.pos[self.array[pos2][1]] = pos2
    
    def ascend(self, pos):
        if pos > self.size: return
        
        left = pos * 2 + 1
        lv = self.inf if left > self.size else self.array[left][0]
        right = pos * 2 + 2
        rv = self.inf if right > self.size else self.array[right][0]
        
        if self.array[pos][0] <= lv and self.array[pos][0] <= rv: return
        if lv < rv:
            self.swap(pos, left)
            self.ascend(left)
        else:
            self.swap(pos, right)
            self.ascend(right)
        
    def descend(self, pos):
        if pos <= 0: return
        parent = (pos - 1) // 2
        if self.array[pos][0] < self.array[parent][0]:
            self.swap(pos, parent)
            self.descend(parent)
    
    def push(self, c, v):
        self.array.append((c, v))
        self.size += 1
        self.pos[v] = self.size
        self.descend(self.size)
    
    def pop(self):
        if self.size < 0: return
        temp = self.array[0]
        self.swap(0, self.size)
        del self.array[self.size]
        self.size -= 1
        self.pos[temp[1]] = -1
        if self.size >= 0: self.ascend(0)
        return temp

    def update(self, c, v):
        if self.pos[v] == -1:
            self.push(c, v)
        elif self.array[self.pos[v]][0] > c:
            self.array[self.pos[v]] = (c, v)
            self.ascend(self.pos[v])
            self.descend(self.pos[v])

def MSTPrim(n, edges):
    # vertex: 0..n-1, e: list of [v1, v2, c] edge between v1 and v2 at cost c

    e = [[] for _ in range(n)]
    for v1, v2, c in edges:
        e[v1].append((v2, c))
        e[v2].append((v1, c))

    minHeap = Heap(n)
    minHeap.push(0, 0)
    nodes = [True] * n
    MST = 0
    
    while minHeap.size >= 0:
        c, v = minHeap.pop()
        nodes[v] = False
        MST += c
        for vi, ci in e[v]:
            if nodes[vi]: minHeap.update(ci, vi)
    return MST
