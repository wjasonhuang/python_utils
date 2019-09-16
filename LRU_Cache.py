'''
LRU cache (Least recently used)
https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)

O(1) read and write using queue (using a double linked list) and hash
https://www.geeksforgeeks.org/lru-cache-implementation/
'''

# Leetcode 146

class Node:
    def __init__(self, key, value):
        self.prev = None    # prev is more recent node
        self.next = None    # next is less recent node
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity):
        self.cap = capacity
        self.head = None
        self.map = dict()

    def remove(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p
        
    def add(self, node): # add node to head of queue
        node.prev, self.head.prev.next = self.head.prev, node
        node.next, self.head.prev = self.head, node
        self.head = node

    def get(self, key):
        if key not in self.map: return -1
        node = self.map[key]
        if node != self.head:
            self.remove(node)
            self.add(node)
        return node.value

    def put(self, key, value):
        if key in self.map:
            self.get(key)
            self.head.value = value
            return
        
        if len(self.map) >= self.cap:
            del self.map[self.head.prev.key]
            self.remove(self.head.prev)

        node = Node(key, value)
        self.map[key] = node
        if len(self.map) == 1: # LRU cache queue saved as a loop to avoid None in prev and next
            self.head = node.prev = node.next = node
        else:
            self.add(self.map[key])
