"""
- Declaring a variable is in python is very simple.
    Just name the variable

    Assign the required value to it

    The data type of the variable will be automatically determined from the value assigned, we need not define it explicitly.
"""

# Declaring variable
A = 1 + 4

# printing value by calling print statement
print(A)

# backward slash is helps interpreter to read next line
x = 1 + 2 \
    + 3
print(x)

# Naming convention, camel case
# myName

x = "Hello Yash!"
print(x)

# Declaring Multiple variable and assigning single value
a = b = c = 10

print(a)
print(b)
print(c)

# Declaring multiple variables in single line
a, b, c = 10, 20, 30

print(a)
print(b)
print(c)

# Deleting variable using `del` statement
s = "Hello"
print(s)
del s
# print(s)  # will raise an error: s is not define
