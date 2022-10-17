# Example 1
class A:
    def a(self):
        return "Function inside A"


class B:
    def a(self):
        return "Function inside B"


# class C is inherits class B and A
class C(B, A):
    pass


# Driver code
# creating an instance
c = C()

# It will call it's first super class method
print(c.a())
"""
    Class C inherits from classes B and A.
    When I don't find any function a() inside class C, I should search for classes B and A and its important that I do it in that order.
"""