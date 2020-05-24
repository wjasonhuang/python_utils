"""
https://docs.python.org/3/tutorial/classes.html
"""

### Class Variable vs Instance Variable
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
