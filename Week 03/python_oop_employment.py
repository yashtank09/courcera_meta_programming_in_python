"""
    Parent class vs. Child class

    Inheritance:
        Inheritance is the capability of one class to derive or inherit the properties from another class.

    Benefits of inheritance are:
        - It represents real-world relationships well.
        - It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
        - It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.

    Types of Inheritance:

        Multiple Inheritance:
            class A:
                pass
            class B(A):
                pass

        Multi-level Inheritance:
            class A:
                a = 1

            class B:
                b = 2

            class C(A, B):
                pass

            c = C()
            print(c.a, c.b)

    More About: https://www.geeksforgeeks.org/inheritance-in-python/
"""


# Demonstrating inheritance
class employee:
    # employee class which takes two arguments name and last
    def __init__(self, name, last):
        self.name = name
        self.last = last


# inheriting class employee to Supervisor
class Supervisor(employee):
    def __init__(self, name, last, password):
        # super() function returns objects represented in the parent’s class and is very useful in  multiple and multilevel inheritances to find which class the child class is extending first.
        super().__init__(name,
                         last)  # here it will also call super class constructor/__init__ method, as we are overloading __init__/constructor
        self.password = password


# inheriting class employee to chef
class chef(employee):
    # created method for leave application/request to supervisor
    def leave_request(self, days):
        return "May I take a leave for " + str(days) + " days."


# created instance of 'Supervisor' class
adrian = Supervisor("Adrian", "A", "apple")

# creating instances of 'chef' class
john = chef("John", "J")
payal = chef("Payal", "P")
sachin = chef("Sachin", "S")

# calling instance methods
print(sachin.leave_request(5))
print(adrian.password)
print(payal.name)


# Built-in function
# There are two built-in functions that can come in handy when trying to find the relationship between different classes and objects: issubclass() and isinstance().
class A:
    pass


class B(A):
    pass


# issubclass() is demonstrated below
print(issubclass(B, A))  # True
print(issubclass(B, list))  # False
print(issubclass(B, (list, A)))  # True

# isinstance() is demonstrated below
b = B()
a = A()
print(isinstance(b, B))  # True
print(isinstance(a, A))  # True
print(isinstance(a, B))  # False
