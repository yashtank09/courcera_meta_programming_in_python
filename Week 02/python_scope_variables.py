"""
    Scope of variable

    More about scope of variable: https://www.geeksforgeeks.org/python-scope-of-variables/
"""


# Local scope of variable.

def get_total(a, b):
    # local variable declared inside a function
    total = a + b
    return total


print(get_total(5, 7))
# output: 7

# Accessing variable outside the function:
print(total)


# Name Error: name 'total' is not defined

# Enclosing scope of variable

def get_total2(c, d):
    # enclosed variable declared inside a function
    total = c + d

    def double_it():
        # local variable
        double = total * 2
        print(double)

    double_it()
    # double variable will not be accessible

    print(double)
    # double will not be accessible

    return total


# Global variable

special = 5


def get_total3(x, y):
    # enclosed scope variable declared inside a function
    total = x + y
    print(special)

    def double_it2():
        # local variable
        double = total * 2
        print(special)

    double_it2()

    return total

# Built in scope

# Built-in scope refers to the reserved keywords that Python uses for its built-in functions, such as print, def, for, in, and so forth.
# Functions with built-in scope can be accessed at any level.
