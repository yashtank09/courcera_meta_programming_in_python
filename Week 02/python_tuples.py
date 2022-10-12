"""
    Tuple is a collection of Python objects much like a list.
    The sequence of values stored in a tuple can be of any type, and they are indexed by integers.
    Values of a tuple are syntactically separated by ‘commas’.
    Although it is not necessary, it is more common to define a tuple by closing the sequence of values in parentheses.

    More about Tuples: https://www.geeksforgeeks.org/tuples-in-python/
"""
# Creating a Tuple
Tuple1 = ("String", 12, 3.4, False)
Tuple2 = "String", 12, 3.4, False

print("This is type checking of Tuple: ", type(Tuple1))

# Printing tuple
print(Tuple1)
print(Tuple2)

# we can not change the value of any index because
# tuples are immutable
# Tuple1[2] = 44 # it will raise an error

# empty tuple
Tuple3 = ()
print("Initial empty Tuple: ", Tuple3)

# Creating a tuple with the use of list
My_List = [1, 2, 3, 4, 5, 6]
print("\nTuple using List: ", tuple(My_List))

# Creating a Tuple with the use of built-in function
Tuple4 = tuple('IronMan')
print("\nTuple with built-in function: ", Tuple4)

# Accessing value of tuple
print("Accessing tuple value using index: ", Tuple1[2])

# Assigning tuple value to other variables
Tuple5 = ("Google", "Microsoft", "Deloit")
A, B, C = Tuple5
print(A)
print(B)
print(C)

# Concatenation of Tuples, we can concatenate tuples with '+' operator
CombinedTuple = Tuple1 + Tuple5

print("\nPrinting combined tuple: ", CombinedTuple)

# index() built-in method
# Find in the tuple and returns the index of the given value where it’s available
Tuple6 = [1, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9, 10, 2, 2, 4]
print("\nPrinting index of value using index() function.")
print(CombinedTuple.index("Google"))
print(CombinedTuple.index(False))

# count() built-in method
# Returns the frequency of occurrence of a specified value
print("\nPrinting frequency of given value: ", Tuple6.count(2))

# lets using methods of list
Tup1 = (5, 'Welcome', 7, 'Geeks')

# You can see more methods of tuples in the link given above
