'''
https://docs.python.org/3/library/bisect.html
Binary search in a sorted array in ascending order

bisect.bisect_left(a, x, lo=0, hi=len(a)) - the left insertion point for x in a to maintain sorted order
bisect.bisect_right(a, x, lo=0, hi=len(a)) - the right insertion point for x in a to maintain sorted order
bisect.insort_left(a, x, lo=0, hi=len(a)) - insert x in a at the left insertion point
bisect.insort_right(a, x, lo=0, hi=len(a)) - insert x in a at the right insertion point

def bisect_left(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x: lo = mid+1
        else: hi = mid
    return lo

def bisect_right(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid]: hi = mid
        else: lo = mid+1
    return lo
'''

import bisect
help(bisect)
a = [0,1,1,3,4]
print(len(a))
print(bisect.bisect_left(a, 1))
print(bisect.bisect_right(a, 1))
print(bisect.bisect_left(a, -1))
print(bisect.bisect_left(a, 10))
bisect.insort_left(a, 6)
print(a)
