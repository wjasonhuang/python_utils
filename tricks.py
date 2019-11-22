'''
coordinate compression
coords is usually a set
'''

coords = [1000,5,-2340,61]
idx = {x: i for i, x in enumerate(sorted(coords))}
print(idx)


'''
sort with comp function
'''
import functools
def cmp(a, b):
    l = (a[0] - a[1]) - (b[0] - b[1])
    if l != 0:
        return -l
    else:
        return b[0] - a[0]
job.sort(key=functools.cmp_to_key(cmp))


'''
class variable vs instance variable
'''

class Example:
    class_variable = 1
    
    def __init__(self, new_class_variable, instance_variable):
        Example.class_variable = new_class_variable
        self.instance_variable = instance_variable

a = Example(1, 'A')
print(a.class_variable, a.instance_variable, '\n')

b = Example(2, 'B')
print(a.class_variable, a.instance_variable)
print(b.class_variable, b.instance_variable, '\n')

Example.class_variable = 3
print(a.class_variable, a.instance_variable)
print(b.class_variable, b.instance_variable, '\n')

a.class_variable = 4
print(a.class_variable, a.instance_variable)
print(b.class_variable, b.instance_variable, '\n')
