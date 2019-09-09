'''
https://docs.python.org/3/library/collections.html
'''

import collections

'''
deque: list-like container with fast appends and pops on either end

deque(iterable, maxlen = None)
append(x)
appendleft(x)
extend(iterable)        append elements from iterable
extendleft(iterable)    appendleft elements from iterable in reversing order
clear()
count(x)
index(x)                returns the first match or raises ValueError if not found
insert(i, x)
pop()
popleft()
remove(x)               remove the first match or raises a ValueError if not found
reverse()
rotate(n)               rotate the deque n steps to the right, if n is negative, rotate to the left
                        = d[-n:] + d[:-n]
maxlen                  maximum size of a deque or None if unbounded, can't change after initialization
'''

d = collections.deque('hello')
d.append('2w')
d.extendleft('2w')
print(d)
print(d.popleft(), d)
d.rotate(4)
print(d)
d = collections.deque('hello', maxlen=5)
print(d)
d.appendleft(2)
print(d)
