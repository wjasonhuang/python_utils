'''
https://en.wikipedia.org/wiki/Trie
insert/search O(L = length of string)
'''

class Node:
    def __init__(self):
        self.children = {}
        self.value = False

class Trie:
    def __init__(self):
        self.trie = Node()

    def insert(self, word: str) -> None:
        cur = self.trie
        for c in word:
            if c not in cur.children: cur.children[c] = Node()
            cur = cur.children[c]
        cur.value = True
                    
    def search(self, word: str) -> bool:
        cur = self.trie
        for c in word:
            if c not in cur.children: return False
            cur = cur.children[c]
        return cur.value

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for c in prefix:
            if c not in cur.children: return False
            cur = cur.children[c]
        return True
