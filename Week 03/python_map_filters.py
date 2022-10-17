# filtering in coffee menu using `map` & `filter`
menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]


# finding word that starts with letter `c`
def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee


print("Map")
# Here we are assigning map object to new variable
maping_coffee = map(find_coffee, menu)
print(maping_coffee)  # print an object of created map

# iterating map object
for x in maping_coffee:
    print(x)

print("Filter")
# Here we are assigning filter object to new variable
filter_coffee = filter(find_coffee, menu)
print(filter_coffee)  # print an object of created filter

# iterating filter object
for x in filter_coffee:
    print(x)

"""
    filter & map are same but their result will be different.
        - Maps take all objects in a list and applies a function.
        - Filter do the same, but take the result and creates a new list with only the true values.
"""
