'''
https://docs.python.org/3/library/collections.html
deque
Counter
namedtuple()
ChainMap
OrderedDict
defaultdict
UserDict
UserList
UserString
'''

'''
deque: list-like container with fast appends and pops on either end

deque(iterable, maxlen = None)
when a bounded deque is full, new items added will cause the same number of items to be popped off the other end

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

from collections import deque

print('----------deque----------')
d = deque('hello')
d.append('2w')
d.extendleft('2w')
print(d)
print(d.popleft(), d)
d.rotate(4)
print(d)
d = deque('hello', maxlen=5)
print(d)
d.appendleft(999)
print(d)
d.extend('123')
print(d)
print(list(d))

'''
Counter: dict subclass for counting hashable objects

Counter([iterable-or-mapping])
elements()
most_common([n])                    returns all elements in the counter if n is omitted
subtract([iterable-or-mapping])
update([iterable-or-mapping])       opposite of subtract
+, -, &, |
'''

from collections import Counter

print('----------Counter----------')
a = Counter()                           # a new, empty counter
b1 = Counter('gallahad')                # a new counter from an iterable
b2 = Counter(['g','a','l','l','a','h','a','d', 'aa'])
c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
d = Counter(cats=4, dogs=8)             # a new counter from keyword args
print(a, b1, b2, c)
print(d, d['birds'])
d['cats'] = 0                           # counter entry with a zero count
print(d)
del d['cats']                           # del actually removes the entry
print(d)

c = Counter(a=4, b=2, c=0, d=-2)
print(list(c.elements()))               # will ignore elements with count < 1
print(Counter('abracadabra').most_common(3))

c = Counter(a=4, b=2, c=0, d=-2)
c.subtract(Counter(a=1, b=2, c=3, d=4))
print(c)
c.subtract('aade')
print(c)

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(['a', 'b', 'b', 'c'])
print(c+d, c-d)                         # will ignore elements with count < 1
print(c&d, c|d)                         # will ignore elements with count < 1
