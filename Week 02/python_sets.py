"""
    A Set is an unordered collection data type that is iterable, mutable and has no duplicate elements.

    Sets are define in {}

    More about sets: https://www.geeksforgeeks.org/sets-in-python/
"""
# Demonstrating sets
my_set = {"Yash", "YouTube", "Facebook", "Snapchat", "Yash"}

print(my_set)

# adding value in sets
my_set.add("Pinterest")

print("Updated set after adding value: ", my_set)

# Removing value from sets

# using remove() method
my_set.remove("Facebook")

# using discard() method
my_set.discard("Snapchat")

print("\nNew updated set after removing elements: ", my_set)

# Mathematical operations
set_a = {1, 3, 4, 5, 7, 8}
set_b = {2, 3, 4, 6, 7, 9}

# Union of sets

# using built-in method
print("\nUnion of set a and b : ", set_a.union(set_b))

# using `|` operator
print(set_a | set_b)

# Intersection of sets

# using built-in method
print("\nIntersection of sets: ", set_a.intersection(set_b))

# using `&` operator
print(set_a & set_b)

# Difference of sets

# using built-in method
print("\nDifference of sets: ", set_a.difference(set_b))

# using `-` operator
print(set_a - set_b)

# Symmetric difference of sets

# using built-in method
print("\nSymmetric Difference of sets: ", set_a.symmetric_difference(set_b))

# using `^` operator
print(set_a ^ set_b)
