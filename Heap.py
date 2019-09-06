'''
https://docs.python.org/3/library/heapq.html
heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k >= 0

heapq.heappush(heap, item)
heapq.heappop(heap)
heapq.heappushpop(heap, item)
heapq.heapify(x)
heapq.heapreplace(heap, item) - pop first then push

General purpose functions based on heaps
heapq.merge(*iterables, key=None, reverse=False)
heapq.nlargest(n, iterable, key=None)
heapq.nsmallest(n, iterable, key=None)
'''

import heapq
help(heapq)
'---------- Initialization ----------'
l = []
heapq.heappush(l, 1)
print(l)

l = [10,9,8,7,6,5,4,3,2,1]
heapq.heapify(l)
print(l)

'---------- Operations ----------'
print(heapq.heappop(l))
print(l)

heapq.heappush(l, 11)
print(l)

print(heapq.heappushpop(l, 0))
print(l)

print(heapq.heapreplace(l, 0))
print(l)

'----------MAX HEAP---------'
l = [10,9,8,7,6,5,4,3,2,1]
rl = [(-i, i) for i in l]
heapq.heapify(rl)
print(rl)
print(heapq.heappop(rl))
print(rl)
heapq.heappush(rl, (-11,11))
print(rl)
