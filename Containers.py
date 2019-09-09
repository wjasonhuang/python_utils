'''
https://docs.python.org/3/tutorial/datastructures.html
tuple
list
set
dict
'''

'''
list.append(x) = a[len(a):] = [x]
list.extend(iterable) = a[len(a):] = iterable
list.insert(i, x)
list.remove(x)
list.pop([i])
list.clear() = del a[:]
list.index(x[, start[, end]])
list.count(x)
list.sort(key=None, reverse=False)
list.reverse()
list.copy() = a[:]
'''

print('----------list----------')
a = [9,8,7,6,5,4,3,2,1,0]
del a[3:-1]
print(a)

a = [9,8,7,6,5,4,3,2,1,0]
print(a.pop(), a)
print(a.pop(-2), a)

a = [0,1,2,2,4,2,4,4,3,3]
print(a, a.index(3), a.count(4))

a = [9,8,7,6,5,4,4,4,1,0]
a.insert(3,-1)
print(a)
a.remove(4)
print(a)
a.clear()
print(a)


'''
set operations: set(), in, -, |, &, ^
'''

print('----------set----------')
a, b = set('abracadabra'), set('alacazam')
print(a, b)                               # unique letters in a
print(a - b, b - a)                       # letters in a but not in b
print(a | b)                              # letters in a or b or both
print(a & b)                              # letters in both a and b
print(a ^ b)                              # letters in a or b but not both
print({x for x in 'abracadabra' if x not in 'abc'})
