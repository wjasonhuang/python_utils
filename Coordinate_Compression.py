'''
coords is usually a set
'''

coords = [1000,5,-2340,61]
index = {x: i for i, x in enumerate(sorted(coords))}
print(index)
