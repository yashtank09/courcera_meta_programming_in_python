# Example 3
class A:
    def c(self):
        return "Function inside A"


class B:
    def c(self):
        return "Function inside B"


# class C is inherits class A and B
class C(A, B):
    def c(self):
        return "Function inside C"


# class D is inherits class A and C
class D(A, C):
    pass

# creating instance of class D
d = D()

# calling method c() of class D
print(d.a)

"""
Traceback (most recent call last):
  File "C:\Yash Stuff\Learning Stuff\Projects\courcera_meta_programming_in_python\Week 03\python_oop_inheritance_exam3.py", line 16, in <module>
    class D(A, C):
TypeError: Cannot create a consistent method resolution
order (MRO) for bases A, C
------------------------------------------------------------------------------------------------------------------------
Note that this throws an error. In the code above, class D inherits from both class A and class C.
Class C is its immediate superclass, but since this is multiple inheritance, the rules are more complicated and it also has to check the classes passed to it for precedence.
In this particular case, class D is unable to resolve the order that should be followed, while resolving the value for the variable in cases where the variable is not present in the class of the given object.
It results in a TypeError because it's unable to create method resolution order (MRO). MRO is Python’s way of resolving the order of precedence of classes while dealing with inheritance.
"""
