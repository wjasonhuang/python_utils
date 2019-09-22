'''
LRU cache (Least recently used)
https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)

O(1) read and write using double linked list and hash
https://www.geeksforgeeks.org/lru-cache-implementation/
'''

# Leetcode 146

class Node:
    def __init__(self, key, value):
        self.prev = None        # prev is more recent node
        self.next = None        # next is less recent node
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity):
        self.cap = capacity
        self.head = None
        self.key_loc = dict()

    def remove(self, node):     # number of elements has to be > 1
        p, n = node.prev, node.next
        p.next, n.prev = n, p
        
    def add(self, node):        # add node to head of queue
        node.prev, self.head.prev.next = self.head.prev, node
        node.next, self.head.prev = self.head, node
        self.head = node

    def get(self, key):
        if key not in self.key_loc: return -1
        node = self.key_loc[key]
        if node != self.head:
            self.remove(node)
            self.add(node)
        return node.value

    def put(self, key, value):
        if self.cap == 0: return
        
        if key in self.key_loc:
            self.get(key)
            self.head.value = value
            return
        
        if len(self.key_loc) >= self.cap:
            del self.key_loc[self.head.prev.key]
            if len(self.key_loc) > 0:
                self.remove(self.head.prev)
            else:
                self.head = None

        node = Node(key, value)
        self.key_loc[key] = node
        if len(self.key_loc) == 1:
            # LRU cache queue saved as a loop to avoid None in prev and next
            self.head = node.prev = node.next = node
        else:
            self.add(self.key_loc[key])
