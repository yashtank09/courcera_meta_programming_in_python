"""
    Exercise: Define a Class

        Learning Objectives
            - You have encountered the basic principles of Object-Oriented programming and in some preliminary ways demonstrated how the different principles can be put into practice with the help of classes, the building blocks of OOP.
            - Let us now look at the structure of these classes.

            - Here you will learn how to create classes and objects with the help of examples. Let's first look at the basic members of a class. These can be the attributes or the data members, the methods, and additionally the comments that you can include.
            - These members can be shown with the help of an example below. Let us imagine you want to make a class of some house. You begin by creating a class for it.
"""


# Example 1
class House:
    """
    This is a stud for a representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    """
    num_rooms = 5
    bathrooms = 2

    def cost_evaluation(self, rate):
        # print(self.num_rooms)
        cost = self.num_rooms * rate
        return cost


home = House()
print(home.num_rooms)
print(home.num_rooms)

home.num_rooms = 8
print(home.num_rooms)
print(House.num_rooms)

House.num_rooms = 4
print(home.num_rooms)
print(House.num_rooms)

# calculating cost of house
print("Cost of house is: ", home.cost_evaluation(210000))
