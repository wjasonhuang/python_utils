'''
https://en.wikipedia.org/wiki/Segment_tree
https://codeforces.com/blog/entry/18051
space Complexity 2N, build tree O(N)
single element update and interval query O(log N)
'''

#Leetcode 307
class SegTree():
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * self.n + nums
        for i in reversed(range(1, self.n)): self.tree[i] = self.tree[i*2]+self.tree[i*2+1]

    def update(self, i, val): #update element i to val
        cur = i + self.n
        self.tree[cur] = val
        while cur > 1:
            cur //= 2
            self.tree[cur] = self.tree[cur*2] + self.tree[cur*2+1]

    def sumRange(self, i, j): #sum elements in range [i, j)
        i += self.n
        j += self.n
        tot = 0
        while i < j:
            if i & 1:
                tot += self.tree[i]
                i += 1
            if j & 1:
                j -= 1
                tot += self.tree[j]
            i //= 2
            j //= 2
        return tot

'''
interval update and query with lazy propagation O(log N) (example Leetcode 699_List)
key facts: modification on internval [l, r) only affects
    1) parents of border leaves l+n and r+n-1
    2) values that compose the interval itself
'''

import math

class SegTreeLazy():
    def __init__(self, arr):
        self.n = len(arr)
        self.h = max(math.ceil(math.log2(self.n)), 1) + 1
        self.tree = [0] * self.n + arr
        for i in reversed(range(1, self.n)): self.tree[i] = max(self.tree[i*2], self.tree[i*2+1])
        self.lazy = [0] * self.n
        #lazy is a delayed operation to be propagated to the children of node i 
        #lazy size is only N because we don't have to store this information for leaves
    
    def apply(self, p, val):
        self.tree[p] = val
        if p < self.n: self.lazy[p] = val
    
    def push_from_root(self, p):
        for i in reversed(range(1, self.h)):
            k = p >> i
            if self.lazy[k] != 0:
                self.apply(k*2, self.lazy[k])
                self.apply(k*2+1, self.lazy[k])
                self.lazy[k] = 0
                
    def push_to_root(self, p):
        while p > 1:
            p //= 2
            self.tree[p] = max(self.tree[p*2], self.tree[p*2+1], self.lazy[p])

    def update_range(self, l, r, val): #update range [l, r)
        l += self.n
        r += self.n
        l0, r0 = l, r
        while l < r:
            if l & 1:
                self.apply(l, val)
                l += 1
            if r & 1:
                r -= 1
                self.apply(r, val)
            l //= 2
            r //= 2
        self.push_to_root(l0)
        self.push_to_root(r0-1)

    def compute_range(self, l, r): #compute range [l, r)
        l += self.n
        r += self.n
        self.push_from_root(l)
        self.push_from_root(r-1)
        ret = 0
        while l < r:
            if l & 1:
                ret = max(ret, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                ret = max(ret, self.tree[r])
            l //= 2
            r //= 2
        return ret

'''
lazy propagation using tree instead of list (example Leetcode 699_Tree)
to set range to a value instead of add a value: (example Leetcode 307_Lazy)
    1) add a timestamp to store latest timestamp of ret udpate
    2) only propagate lazy to children if parent's timestamp is later than children's
'''

def calc(a, b):
    return max(a, b)

class Node():
    def __init__(self, lb, rb, ret=0, lazy=0):
        self.lb = lb
        self.rb = rb
        self.ret = ret
        self.lazy = lazy #lazy is a delayed operation to be propagated to the children
        self.left = None
        self.right = None

    def update_lazy(self):
        if self.left:
            self.left.ret = calc(self.left.ret, self.lazy)
            self.left.lazy = calc(self.left.lazy, self.lazy)
        if self.right:
            self.right.ret = calc(self.right.ret, self.lazy)
            self.right.lazy = calc(self.right.lazy, self.lazy)
        self.lazy = 0

class SegmentTree():
    def __init__(self, arr):
        def build(lb, rb): #build [lb, rb)
            if lb >= rb: return None
            if lb + 1 == rb: return Node(lb, rb, arr[lb])
            root = Node(lb, rb)
            mid = (lb + rb) // 2
            root.left = build(lb, mid)
            root.right = build(mid, rb)
            root.ret = calc(root.left.ret, root.right.ret)
            return root
        self.root = build(0, len(arr))

    def update_range(self, lb, rb, val): #update [lb, rb) to val
        def update(root, lb, rb, val):
            if root is None: return
            if lb >= root.rb or rb <= root.lb: return
            if root.lazy > 0: root.update_lazy()
            if lb <= root.lb and root.rb <= rb:
                root.ret = calc(root.ret, val)
                root.lazy = val
                return
            update(root.left, lb, rb, val)
            update(root.right, lb, rb, val)
            root.ret = calc(root.left.ret, root.right.ret)
        if lb < rb: update(self.root, lb, rb, val)

    def compute_range(self, lb, rb): #compute [lb, rb)
        def compute(root, lb, rb):
            if root is None: return 0
            if lb >= root.rb or rb <= root.lb: return 0
            if lb <= root.lb and root.rb <= rb: return root.ret
            if root.lazy > 0: root.update_lazy()
            return calc(compute(root.left, lb, rb), compute(root.right, lb, rb))
        return compute(self.root, lb, rb) if lb < rb else 0
