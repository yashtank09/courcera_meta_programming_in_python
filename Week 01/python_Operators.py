"""
    More about operators: https://www.geeksforgeeks.org/python-operators/
    Python Operators in general are used to perform operations on values and variables.
    These are standard symbols used for the purpose of logical and arithmetic operations.
"""

# Demonstrating Arithmetic Operators
a = 22
b = 33

# `+`   Addition: adds two operands
addition = a + b

# `–`	Subtraction: subtracts two operands
sub = a - b

# `*`	Multiplication: multiplies two operands
multi = a * b

a2 = 3
b2 = 2
# `/`	Division (float): divides the first operand by the second
division = a2 / b2

# `//`	Division (floor): divides the first operand by the second
floordivision = a2 // b2

# `%`	Modulus: returns the remainder when the first operand is divided by the second
mod = a2 % b2

# `**`	Power: Returns first raised to power second
power = a2 ** b2

# Demonstrating of comparison operators

X = 21
Y = 23

# `>`	Greater than: True if the left operand is greater than the right
print(X > Y)

# `<`	Less than: True if the left operand is less than the right
print(X < Y)

# `==`	Equal to: True if both operands are equal
print(X == Y)

# `!=`	Not equal to – True if operands are not equal
print(X != Y)

# `>=`	Greater than or equal to True if the left operand is greater than or equal to the right
print(X >= Y)

# `<=`	Less than or equal to True if the left operand is less than or equal to the right
print(X <= Y)

# `is` 	x is the same as y
print(X is Y)

# `is not`	x is not the same as y
print(X is not Y)

# Demonstrating Logical Operators

P = True
Q = False

# `and`	Logical AND: True if both the operands are true
# Print P and Q is False
print(P and Q)

# `or`	Logical OR: True if either of the operands is true
# Print P or B is True
print(P or Q)

# `not`	Logical NOT: True if the operand is false
# Print not P is False
print(not P)

# Demonstrating Bitwise Operators
M = 10
N = 4

# `&`	Bitwise AND
# Print bitwise AND operation
print(M & N)

# `|`	Bitwise OR
# Print bitwise OR operation
print(M | N)

# `~`	Bitwise NOT
# Print bitwise NOT operation
print(~ M)

# `^`	Bitwise XOR
# print bitwise XOR operation
print(M ^ N)

# `>>`	Bitwise right shift
# print bitwise right shift operation
print(M >> 2)

# `<<`	Bitwise left shift
# print bitwise left shift operation
print(N << 2)

# Assignment operators: https://www.geeksforgeeks.org/assignment-operators-in-python/
# Examples of Assignment operators

S = 10
T = 5

# Assigning value of S and T to V using `=` operator
V = S + T
print(V)

# We can also assign it in this way looks as S = S + T, also we can do with other arithmatic and Bitwise operator also
S += T
print(S)
