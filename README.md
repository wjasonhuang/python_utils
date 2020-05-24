# The Python Standard Library
https://docs.python.org/3/library/

# Python for Everybody (PY4E)
https://www.py4e.com/materials

# Notes
## Parameter Passing for Mutable & Immutable Objects
https://medium.com/@tyastropheus/tricky-python-ii-parameter-passing-for-mutable-immutable-objects-10e968cbda35

## Raw String
- Python raw string is created by prefixing a string literal with ‘r’ or ‘R’.
- Python raw string treats backslash ( \\ ) as a literal character. 


## Class Variable vs Instance Variable
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
