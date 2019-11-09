'''
Union Find Set O(alpha(N)) per operation
alpha(N) inverse Ackermann function ~ O(1)
https://en.wikipedia.org/wiki/Disjoint-set_data_structure
'''


class UnionFindSet():
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.rk = [0] * n
    
    def find(self, v):
        if self.p[v] != v: self.p[v] = self.find(self.p[v])
        return self.p[v]
    
    def union(self, v1, v2):
        p1 = self.find(v1)
        p2 = self.find(v2)
        if p1 == p2: return True
        if self.rk[p1] < self.rk[p2]: p1, p2 = p2, p1
        self.p[p2] = p1
        self.rk[p1] += self.rk[p1] == self.rk[p2]
        return False
