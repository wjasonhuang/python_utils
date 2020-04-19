- https://www.py4e.com/materials

# Parameter Passing for Mutable & Immutable Objects
- https://medium.com/@tyastropheus/tricky-python-ii-parameter-passing-for-mutable-immutable-objects-10e968cbda35

# Coordinate Compression
coords = [1000,5,-2340,61]
idx = {x: i for i, x in enumerate(sorted(coords))}
print(idx)

# Sort with Comp Function

import functools
def cmp(a, b):
    l = (a[0] - a[1]) - (b[0] - b[1])
    if l != 0:
        return -l
    else:
        return b[0] - a[0]
job.sort(key=functools.cmp_to_key(cmp))


# Class Variable vs Instance Variable
class Example:
    class_variable = 1

    def __init__(self, new_class_variable, instance_variable):
        Example.class_variable = new_class_variable
        self.instance_variable = instance_variable


a = Example(1, 'A')
b = Example(2, 'B')
Example.class_variable = 3
print(a.class_variable, a.instance_variable)
print(b.class_variable, b.instance_variable, '\n')
