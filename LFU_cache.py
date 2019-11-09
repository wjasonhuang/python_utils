'''
LFU cache (Least frequently used, use LRU as tiebreaker)
https://en.wikipedia.org/wiki/Least_frequently_used

O(1) read and write using two dimensional double linked list and hash
'''


# Leetcode 460

class Node:
    def __init__(self, key, value):
        self.prev = None            # prev is more recent node
        self.next = None            # next is less recent node
        self.key = key
        self.value = value

class LRUCache:
    def __init__(self):
        self.head = None            # tail = self.head.prev
        self.len = 0

    def insert(self, node):
        if not self.head:
            node.prev = node.next = node
        else:
            node.prev, self.head.prev.next = self.head.prev, node
            node.next, self.head.prev = self.head, node
        self.head = node
        self.len += 1

    def remove(self, node):
        self.len -= 1
        if not self.len:
            self.head = None
        else:
            p, n = node.prev, node.next
            p.next, n.prev = n, p
            if self.head == node: self.head = n

class Freq_Node:
    def __init__(self, freq):
        self.prev = None            # prev is more recent node
        self.next = None            # next is less recent node
        self.freq = freq
        self.cache = LRUCache()

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = None            # tail = self.head.prev
        self.freq_loc = dict()      # freq_node location for given key
        self.key_loc = dict()       # node location for given key

    def get(self, key: int) -> int:
        if key not in self.key_loc: return -1
        
        freq_node, node = self.freq_loc[key], self.key_loc[key]
        freq_node.cache.remove(node)
        
        p, n = freq_node.prev, freq_node.next
        if p.freq == freq_node.freq + 1:
            p.cache.insert(node)
            self.freq_loc[key] = p
            if freq_node.cache.len == 0: p.next, n.prev = n, p
        else:
            new = Freq_Node(freq_node.freq + 1)
            new.cache.insert(node)
            self.freq_loc[key] = new
            
            if freq_node.cache.len == 0:
                if p == n:
                    new.prev = new.next = new
                else:
                    p.next, new.prev = new, p
                    new.next, n.prev = n, new
            else:
                p.next, new.prev = new, p
                new.next, freq_node.prev = freq_node, new
            
            if self.head == freq_node: self.head = new
        
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.cap == 0: return
        
        if key in self.key_loc:
            self.get(key)
            self.key_loc[key].value = value
            return
        
        if len(self.key_loc) >= self.cap:
            freq_node_to_del = self.head.prev
            node_to_del = freq_node_to_del.cache.head.prev
            key_to_del = node_to_del.key
            freq_node_to_del.cache.remove(node_to_del)
            del self.freq_loc[key_to_del]
            del self.key_loc[key_to_del]
            
            if freq_node_to_del.cache.len == 0:
                if self.head == freq_node_to_del:
                    self.head = None
                else:
                    p, n = freq_node_to_del.prev, freq_node_to_del.next
                    p.next, n.prev = n, p
        
        node = Node(key, value)
        self.key_loc[key] = node
        if not self.head or self.head.prev.freq != 1:
            freq_node = Freq_Node(1)
            freq_node.cache.insert(node)
            self.freq_loc[key] = freq_node
            
            if not self.head:
                self.head = freq_node.next = freq_node.prev = freq_node
            else:
                p, n = self.head.prev, self.head
                p.next, freq_node.prev = freq_node, p
                freq_node.next, n.prev = n, freq_node
        else:
            self.head.prev.cache.insert(node)
            self.freq_loc[key] = self.head.prev
