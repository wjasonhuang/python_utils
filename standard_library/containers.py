"""
https://docs.python.org/3/tutorial/datastructures.html
tuple
list
string
set
dict
"""

'''
list.append(x) = a[len(a):] = [x]
list.extend(iterable) = a[len(a):] = iterable
list.insert(i, x)
list.remove(x)                          remove first item with value x
list.pop([i])                           i default to -1, pop last item O(1), pop first item O(N)
list.clear() = del a[:]
list.index(x[, start[, end]])
list.count(x)
list.sort(key=None, reverse=False)
list.reverse()
list.copy() = a[:]
'''

print('----------list----------')
a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
del a[3:-1]
print(a)

a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(a.pop(), a)
print(a.pop(-2), a)

a = [0, 1, 2, 2, 4, 2, 4, 4, 3, 3]
print(a, a.index(3), a.count(4))

a = [9, 8, 7, 6, 5, 4, 4, 4, 1, 0]
a.insert(3, -1)
print(a)
a.remove(4)
print(a)
a.clear()
print(a)

'''
https://docs.python.org/3/library/stdtypes.html#string-methods
str.capitalize()                        return a string with first character capitlaized
str.title()                             return a string with words start with an uppercase character
str.strip([chars])
str.lstrip([chars])
str.rstrip([chars])
str.upper()
str.lower()
str.swapcase()

str.join(iterable)                      the separator between elements is the string providing this method
str.split(sep=None, maxsplit=-1)        the default separator is whitespace
str.rsplit(sep=None, maxsplit=-1)
str.splitlines([keepends])
str.partition(sep)
str.rpartition(sep)
str.replace(old, new[, count])

str.startswith(prefix[, start[, end]])
str.endswith(suffix[, start[, end]])

str.count(sub[, start[, end]])          count in s[start:end]
str.find(sub[, start[, end]])           -1 if not found
str.rfind(sub[, start[, end]])
str.index(sub[, start[, end]])          like find() but raise ValueError when not found
str.rindex(sub[, start[, end]])

str.isalnum()                           true if all characters in the string are alphanumeric
str.isalpha()                           true if all characters in the string are alphabetic
str.isdigit()
str.isnumeric()
str.isspace()                           true if there are only whitespace characters in the string
str.islower()
str.isupper()
'''

print('----------string----------')
print(' '.join(['a', 'bc', 'def']))
print('ababa'.partition('b'))
print('ababa'.split('b'))
print('ababa'.split('b', maxsplit=1))
print(' a\t bab\t\n a\n'.split())
print('Alibaba'.replace('a', 'o'))
print('hello the little'.title())

'''
set operations: set(), in, -, |, &, ^, <, <=, >, >=
set.add(x)
set.remove(x)                           throw KeyError if x not in set
set.discard(x)                          does nothing if x not in set
set.issubset(x) or <=                   true if the set is a subset of x
set.issuperset(x) or >=                 true if the set is a superset of x
set.isdisjoint(x)                       true if the set has no elements in common with x
'''

print('----------set----------')
a, b = set('abracadabra'), set('alacazam')
print(a, b)  # unique letters in a
print(a - b, b - a)  # letters in a but not in b
print(a | b)  # letters in a or b or both
print(a & b)  # letters in both a and b
print(a ^ b)  # letters in a or b but not both
print({x for x in 'abracadabra' if x not in 'abc'})
a, b, c, d = set([1, 2, 3]), set([1, 2]), set([1, 2, 3]), set([4, 5])
print(a < b, a > b, a < c, a <= c, a < d, a >= d)
print(a.issuperset(c), b.issubset(a), d.isdisjoint(a))
