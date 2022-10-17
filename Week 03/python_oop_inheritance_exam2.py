# Example 2
class A:
    def b(self):
        return "Function inside A"


class B:
    def b(self):
        return "Function inside B"


# class C inherits class A and B
class C(A, B):
    # also try out with commenting this method of class C
    def b(self):
        return "Function inside C"

    pass


# class D inherits class C
class D(C):
    pass

# creating instance of class D
d = D()

# it will call method b() of class C
print(d.b())

"""
Class D inherits from class C, which in turn inherits from classes A and B.
Class D accesses the immediate superclass of class D, which is class C and resolves the value of the variable once it's found in that superclass.
Now let’s say I comment out the declaration inside class C.

# def b(self):
#     return "Function inside C" 

And replace it with the pass keyword to keep the code functional.
Since there was no value present inside class C either, the function call above would go to A.
That is because class C will point to class A as having higher precedence while inheriting.
Now let's take another example of a similar scenario.
"""