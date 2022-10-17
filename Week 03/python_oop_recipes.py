"""

        Whenever a class is instantiated __new__ and __init__ methods are called.
        __new__ method will be called when an object is created and __init__ method will be called to initialize the object.
        In the base class object, the __new__ method is defined as a static method which requires to pass a parameter cls.
        cls represents the class that is needed to be instantiated, and the compiler automatically provides this parameter at the time of instantiation.

    class Recipes():
    def __new__(cls, *args, **kwargs):
        pass

    def __int__(self):
        pass

    More about: https://www.geeksforgeeks.org/__new__-in-python/
"""


# instantiate a custom object
# creating a class recipes
class Recipe:
    # this is a parameterized constructor or in python this is __init__ method which will execute at the time of instance is created
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def contents_dish(self):
        print("The " + self.dish + " has " + str(self.items) + " and takes " + str(
            self.time))  # have to convert `items` and `time` to string

# passing value to __init__()/ constructor method
pizza = Recipe('Pizza', ['Tomato', 'Cheese', 'Olives'], 33)

print(pizza.items)

print(pizza.contents_dish())
