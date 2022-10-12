"""
    Python Lists are just like dynamically sized arrays, declared in other languages (vector in C++ and ArrayList in Java).
    In simple language, a list is a collection of things, enclosed in [ ] and separated by commas.

    The list is a sequence data type which is used to store the collection of data.

    More about List: https://www.geeksforgeeks.org/python-lists/
"""
# here we are creating a list using []
var = ["Yash", "Banana", "For", "Java", "Python"]

# printing list in []
print(var)

# print separate elements of list using index numbers
print(var[2])  # will print element of index 2: 'For'
print(var[3])  # will print element of index 3: 'Java'

# printing a length of a list
print("Length of a list `var`: ", len(var))

# print list's members separately
print(*var, sep=", ")  # will print like this: Yash, Banana, For, Java, Python

# list with different datatypes
var2 = ["Games", 22, 32.2, True, 8, "Marvel"]
print("List with the use of mixed values: ")
print(var2)
print("List printed using index: ")
print(var2[3])
print(var2[1])

var2[2] = 1.9

# list after assigning new value to index
print("list after assigning new value to index: ", var2)

# demonstration for creating a list
# creating a blank list
List = []
print("Blank List: ")
print(List)

# Creating a list of numbers
List = [10, 20, 14]
print("\nList of numbers: ")
print(List)

# Creating a list of strings and accessing using index
List = ["Yash", "No", "Rohit", "Kohli"]
print("\nList Items: ")
print(List[1])
print(List[2])

# Complexity for creating a list
# Time complexity: O(1)
# Space complexity: O(n)

# nested list
List = ["Tony", ["Thor", "Star Loard", "Gamora", "Rocket"], "Steave", "Banner"]
print(List)

# printing multidimensional list using index numbers
print(List[1][2])  # will print 'Gamora'

# List operations
List_Adding = []

# Adding elements in python list

# Using append() function
# Only one element at a time can be added to the list by using append() at the end of the list.
List_Adding.append(1)
List_Adding.append(2)
List_Adding.append(3)
List_Adding.append(4)

for i in range(5, 14):
    List_Adding.append(i)

# printing updated list
print(List_Adding)

# appending another list to a list
List_Adding_sub = ["yash", "peter"]

List_Adding.append(List_Adding_sub)

# printing appended list
print(List_Adding)

# Using insert() function
# insert function takes two arguments for adding as index and value
List_insert = [1, 2, 3, 4]
print("\nInitial list: ", List_insert)

# adding elements at the specific position
List_insert.insert(2, 8)
List_insert.insert(0, "Added")

# print updated list
print("This is updated list: ", List_insert)

# Using extend() function
# we can extend more values we want to add in the given list
List_extend = [1, 2, 3, 4]

# adding multiple element to the list at the end
List_extend.extend(["Yash", "Captain", 22.2, True])

# printing updated list
print("\nList after performing extend operation: ", List_extend)

# Reversing a list using reverse() function
List_extend.reverse()

# printing reversed list
print("\nThis is reversed list: ", List_extend)

# Removing elements from the List

# Using remove() method
# remove(<element it self>)
Remove_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

Remove_list.remove(4)
Remove_list.remove(9)

# printing updated list
print("\nPrinting updated list: ", Remove_list)

# Using pop() method
# Removing element from the last using the pop() method
Remove_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

Remove_list.pop()

print("\nList after popping an element: ", Remove_list)

# Removing element at the specific location from the list using the pop(<index>) method
Remove_list.pop(0)

print("\nList after popping an indexed element: ", Remove_list)

# there are more method of the list you can review it on above link given in the comment section.
