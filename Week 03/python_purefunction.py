# this is traditional function
my_list = [1, 2, 3]


def add_to_list(item):
    return my_list.append(item)


add_to_list(4)

# printing `my_list`
print("Output of traditional function:-")
print(my_list)
# this is not pure function, because the data is manipulated at the global scope from inside the scope of the function.

# Let's try to turn it into pure function
my_list2 = [1, 2, 3]


def add_to_list_2(items):
    my_list2.append(items)
    return my_list2


new_List2 = add_to_list_2(4)
print("Output of improved traditional function:-")
print(my_list2)
print(new_List2)

# It's still not pure function, because even though it's returning a new variable, it still has a reference to the my_list

# Let's try something else
my_list3 = [1, 2, 3]


def add_to_list_3(lst, items):
    lst.append(items)
    return lst


new_List3 = add_to_list_3(my_list3, 4)

print("Output of much improved traditional function:-")
print(my_list3)
print(new_List3)

# Once again both list contain updated value, because it's still using that list as an argument and still being updated within the function

# Now creating a Pure function
my_list4 = [1, 2, 3]


def add_to_list_4(lst, items):
    nl = lst.copy()
    nl.append(items)
    return nl


new_List4 = add_to_list_4(my_list4, 4)

print("Output of Pure function:-")
print(my_list4)
print(new_List4)
