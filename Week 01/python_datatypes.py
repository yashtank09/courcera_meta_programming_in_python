"""
Data types are the classification or categorization of data items.
It represents the kind of value that tells what operations can be performed on a particular data.
Since everything is an object in Python programming, data types are actually classes and variables are instance (object) of these classes.

Hierarchy: https://media.geeksforgeeks.org/wp-content/uploads/20191023173512/Python-data-structure.jpg
"""

# Displaying variables and their types
a_int = 10
print(type(a_int))
print(a_int)

b_float = 3.8
print(type(b_float))
print(b_float)

c_complexNumber = 10 + 10j
print(type(c_complexNumber))
print(c_complexNumber)

d_string = "Hello Yash! aka tyj"
print(type(d_string))
print(d_string)

e_list = ['Yash', 33, 22.3, 'List']
print(type(e_list))
print(e_list)

f_tuples = ('Yash', 44, 99.2, 'Tuples')
print(type(f_tuples))
print(f_tuples)

g_sets = {'Yash', 33.2, 11, 'Sets'}
print(type(g_sets))
print(g_sets)

# Type conversion / Type Casting
# is the method to convert the variable data type into a certain data type in order to the operation required to be performed by users.

# Implicit type conversion
# In this,  methods, Python converts data type into another data type automatically. In this process, users don’t have to involve in this process.

# Demonstration of Implicit type conversion

# Python automatically converts `A1` to int
A1 = 78
print(A1)
print(type(A1))

# Python automatically converts `B1` to float
B1 = 3.0
print(B1)
print(type(B1))

# Python automatically converts `C1` to float as it is a float addition
C1 = A1 + B1
print(C1)
print(type(C1))

# Python automatically converts `D1` to float as it is a float multiplication
D1 = A1 * B1
print(D1)
print(type(D1))

# Explicit Type Casting
# Python need user involvement to convert the variable data type into certain data type in order to the operation required.
# Mainly in type casting can be done with these data type functions:

# Demonstration of Explicit Type casting

# int variable
A2 = 5

# typecast to float
N1 = float(A2)

print(N1)
print(type(N1))

# Float variable
A3 = 5.6

# typecast to int
N2 = int(A3)

print(N2)
print(type(N2))

# int variable
A4 = 23

# typecast to string
N3 = str(A4)

print(N3)
print(type(N3))

# string variable
A5 = "5"

# typecast to int
N4 = int(A5)

print(N4)
print(type(N4))

# string variable
A6 = "5.9"

# typecast to int
N5 = float(A6)

print(N5)
print(type(N5))

# there are more type conversions
# ord():
# hex():
# oct():
# tuple():
# set():
# list():
# dict():
