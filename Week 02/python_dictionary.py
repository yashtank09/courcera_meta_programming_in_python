"""
    Dictionary in Python is a collection of keys values, used to store data values like a map, which, unlike other data types which hold only a single value as an element.
    Dictionary holds key:value pair. Key-Value is provided in the dictionary to make it more optimized.

    syntax:
        my_dict = {<key> : <value>, <key2> : <value2>}

    More about Dictionary: https://www.geeksforgeeks.org/python-dictionary/
"""

# Demonstrating dictionary
my_dict = {1: "Moon", 2: "Uranus", 3: "Earth"}

print("This is dictionary with the key value pair: ", my_dict)

# Accessing separate element using key value
print("\nAccessing value from dictionary: ", my_dict[1])
print("Accessing value from dictionary: ", my_dict[3])

# Empty dictionary
my_dict2 = {}

print("\nThis is an empty dict: ", type(my_dict2))

# creating dictionary with dict() method
my_dict3 = dict({1: "BMW", 2: "TATA", 3: "VOLVO"})

print("\nDictionary using dict() built-in method: ", my_dict3)

# creating dictionary with each item as a pair
my_dict3 = dict([(1, "BMW"), (2, "TATA"), (3, "VOLVO")])

print("\nDictionary using dict() built-in method: ", my_dict3)

# Nested dictionary
my_dict4 = {1: "Cricket", 2: "Hockey", 3: {1: "Chess", 2: "Table Tennis", 3: "Snack Leader", 4: "Carom"},
            4: "Foot Ball"}

print(my_dict4)

# Accessing separate element from nested dictionary
print("\nAccessing nested dictionary's value: ", my_dict4[3][2])
print("\nAccessing nested dictionary's value: ", my_dict4[3][4])

# Modify dictionary value
my_dict4[4] = "Drag Racing"

print("\nModified value: ", my_dict4)

# Modifying nested dictionary values
my_dict4[3][2] = "Monopoly"

print("\nModified value: ", my_dict4)

# Updating dictionary by adding a new pair of key and value
my_dict4[5] = "Wally Ball"

print("\nModified value: ", my_dict4)

# Overriding key value
my_dict4[5] = "Tennis"

print("\nModified value: ", my_dict4)

# Creating new nested dictionary in current dictionary
my_dict4[6] = {1: "Swimming", 2: "Rock Climbing", 3: "River Drafting"}

print("\nModified value: ", my_dict4)

# Creating dictionary using String key
my_dict6 = {"Name": "Yash", "Address": "Gandhigram, Junagadh", "Number": 7984248787}

print("\nString Key value: ", my_dict6)

# Operations on dictionary

# clear() – Remove all the elements from the dictionary
my_dict6.clear()

print("\nCleared Dictionary: ", my_dict6)

# copy() – Returns a copy of the dictionary
my_dict7 = {1: "Moon", 2: "Uranus", 3: "Earth", 4: "Mars"}

# get() – Returns the value of specified key
print("\nReturns value of specified key:", my_dict7.get(1))
print("\nReturns value of specified key:", my_dict7.get(4))

# copy() – Returns a copy of the dictionary
Dict1 = my_dict7.copy()

print("\nCopied dictionary:", Dict1)

# items() – Returns a list containing a tuple for each key value pair
print("\nList containing a tuple for each key value pair: ", Dict1.items())

# keys() – Returns a list containing dictionary’s keys
print("\nList of keys in dictionary:", Dict1.keys())

# pop() – Remove the element with specified key
Dict1.pop(3)
print("\nUpdated dictionary:", Dict1)

# popitem() – Removes the last inserted key-value pair
Dict1.popitem()
print("\nAfter Popped value: ", Dict1)

# update() – Updates dictionary with specified key-value pairs
Dict1.update({3: "Jupyter"})

# values() – Returns a list of all the values of dictionary
print("\nPrinting list of all values: ", Dict1.values())

# for more about `dictionaries` you can find the link above
