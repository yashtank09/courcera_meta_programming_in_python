"""
    Exception handling
     -
     - Syntax errors, which are caused by human error, and exceptions which are known errors that need to be handled.

     Syntax Error: As the name suggests this error is caused by the wrong syntax in the code. It leads to the termination of the program.
"""

# Syntax error example
# Here is the list of planets
'''
Milky_way = ["Mercury", "Venus", "Earth", "Mars", "Jupyter", "Saturn", "Uranus", "Neptune", "Pluto"]

for i in Milky_way  # Here it will raise SyntaxError: invalid syntax
    print(i)
'''

# Handling exception using try and except statements
"""
    :- Exceptions are known errors that need to be handled.
    Try and except statements are used to catch and handle exceptions in Python.
    Statements that can raise exceptions are kept inside the try clause and the statements that handle the exception are written inside except clause.
"""

# try and except
a = [1, 2, 3, 4]

try:
    print("Second Element = %d" % (a[1]))
    # This will throw an exception
    print("Trying to find fourth element = %d" % (a[4]))
# Here this will execute when ever an error occurred
except IndexError:
    print("Something went wrong an error occurred")

# There are some built-in class for error handling

# IndexError
# using previous list
try:
    item = a[4]
    print(item)
# This is the way of showing which error has occurred
except IndexError as e:
    print("Something went wrong Error: ", e)


# ZeroDivisionError
# function for dividing a number
def divide_by(x, y):
    return x / y


try:
    print("Answer is: ", divide_by(10 / 0))
except ZeroDivisionError as e:
    print("An Error occurred: ", e)


# Another method
def divide_by(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print("An Error occurred: ", e)


print("Answer is: ", divide_by(10 / 0))


# NameError with ArithmeticError

# Function for division by value-3
def func(a):
    # condition for checking user input is grater than 3
    if a < 4:
        # throws arithmetic exception if a = 3
        b = a / (a - 3)

    print("Value of b = ", b)


try:
    func(3)
    # func(7)
# Multiple except blocks
except ArithmeticError as e:
    print("An arithmetic error occurs: ", e)
except NameError as n:
    print("An naming error occurs: ", n)


# Try with Else Clause
# The code enters the else block only if the try clause does not raise an exception.

# A function which returns a/b
def funcA(p, q):
    try:
        c = ((p + q) / (p - q))
    except ArithmeticError:
        print("a/b An Arithmetic error occurs.")
    else:
        print(c)


# Drive program to test above function
funcA(2.0, 3.0)
funcA(3.0, 3.0)

# FileExistsError

try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except FileExistsError as e:
    print("Something went wrong:", e)
except FileNotFoundError as e:
    print("Something went wrong:", e)
