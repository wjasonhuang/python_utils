'''
https://docs.python.org/3/tutorial/datastructures.html
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
a = [9,8,7,6,5,4,3,2,1,0]
del a[-1]
print(a)

a = [9,8,7,6,5,4,3,2,1,0]
del a[3:-1]
print(a)

a = [9,8,7,6,5,4,3,2,1,0]
a.pop()
print(a)
a.pop(-2)
print(a)

a = [0,1,2,2,4,2,4,4,3,3]
print(a.index(3))
print(a.count(4))

a = [9,8,7,6,5,4,4,4,1,0]
a.insert(3,-1)
print(a)
a.remove(4)
print(a)
a.clear()
print(a)
