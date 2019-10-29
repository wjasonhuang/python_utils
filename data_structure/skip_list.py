'''
https://en.wikipedia.org/wiki/Skip_list
search/insert/delete ~ O(log N)
space ~ O(N)
'''

# Leetcode 1206

import random

class Node:
    def __init__(self, lvl, val=None):
        self.lvl = lvl
        self.next = [None] * lvl
        self.val = val

class Skiplist:
    def __init__(self):
        self.head = Node(1)

    def randlevel(self):
        lvl = 1
        while lvl <= self.head.lvl and random.randint(0, 1): lvl += 1
        return lvl

    def search(self, target: int) -> bool:
        cur = self.head
        for i in reversed(range(self.head.lvl)):
            while cur.next[i] and cur.next[i].val <= target: cur = cur.next[i]
            if cur.val == target: return True
        return False

    def add(self, num: int) -> None:
        lvl = self.randlevel()
        new = Node(lvl, num)
        cur = self.head
        if lvl > cur.lvl:
            cur.next.append(None)
            cur.lvl = lvl
        for i in reversed(range(self.head.lvl)):
            while cur.next[i] and cur.next[i].val < num: cur = cur.next[i]
            if i < lvl:
                new.next[i] = cur.next[i]
                cur.next[i] = new

    def erase(self, num: int) -> bool:
        prev = [None] * self.head.lvl + [self.head]
        for i in reversed(range(self.head.lvl)):
            cur = prev[i + 1]
            while cur.next[i] and cur.next[i].val < num: cur = cur.next[i]
            prev[i] = cur
        if not cur.next[i] or cur.next[i].val != num: return False
        
        cur = cur.next[i]
        for i in reversed(range(cur.lvl)):
            prev[i].next[i] = cur.next[i]
        while self.head.lvl > 1 and not self.head.next[-1]:
            self.head.lvl -= 1
            del self.head.next[-1]
        return True