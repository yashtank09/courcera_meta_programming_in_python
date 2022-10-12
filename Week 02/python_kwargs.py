"""
    The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list.
    We use the name kwargs with the double star.
    The reason is that the double star allows us to pass through keyword arguments (and any number of them).
        - A keyword argument is where you provide a name to the variable as you pass it into the function.
    More about **kwargs: https://www.geeksforgeeks.org/args-kwargs-python/
"""


# Python program to illustrate *kwargs
def sum_of(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return round(sum, 2)


# we can enter n number of arguments with key value pair
print(sum_of(coffee=1.99, cack=2.3, juice=2.3))
