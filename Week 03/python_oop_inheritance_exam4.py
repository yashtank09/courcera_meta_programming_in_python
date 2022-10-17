# Example 4
class A:
    def d(self):
        return "Function inside A"


class B:
    def d(self):
        return "Function inside B"


class C:
    def d(self):
        return "Function inside C"


# class D inherits class A and B
class D(A, B):
    def d(self):
        return "Function inside D"


# class E inherits class B and C
class E(B, C):
    def d(self):
        return "Function inside E"


# class D inherits class E and D and C
class F(E, D, C):
    pass


# creating instance of class F
f = F()

# calling method d() using the reference of class F
print(f.d())
print(F.mro())

"""
The code here is simple. class F directly inherits from its immediate superclass and the first class that is passed to it.
The second line then demonstrates the return from the mro() function.
The examples in this reading demonstrate how code in which multiple inheritance is used, can get complicated and very messy, very fast.
Multiple inheritance, with all the advantages and flexibility that it provides, should only be used once you have a strong command of Python as a language to avoid creating 'spaghetti code' that's difficult to understand and update.
"""