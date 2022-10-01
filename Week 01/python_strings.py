"""
String:
    A sequence of characters in single or double quotes
    can declare as
    'We are open'
    "24 hours a day!"
"""
# Single quot declaration
singleQuat = 'Yash'
print(singleQuat)

# Double quot declaration
doubleQuat = "Tank"
print(doubleQuat)

# Concatenating two stings
print(singleQuat + doubleQuat)

# Single line declaration
string_Var1 = "Hello this is Single line declaration."

print(string_Var1)

# Double line declaration
string_Var2 = "Hello this is multi " \
              "line declaration of " \
              "string variables."

print(string_Var2)

# Reassigning a string value
# name variable is assigned with the value of John
name = 'John'
print(name)  # will print `John`

name = 'Paul'
print(name)  # will print `Paul`

# Accessing string characters using index numbers
print(name[0])
print(name[1])
print(name[2])
print(name[3])

# len() function is representing number of characters in the string
print(len(name))

# input() This function looks for the default input device, your keyboard, and captures the value. This value can then be assigned or used.
print("where do you live?")
location = input()
print("So you live in "+location)
