"""
    The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function.
    It is used to pass a non-key worded, variable-length argument list.
        - The syntax is to use the symbol * to take in a variable number of arguments; by convention, it is often used with the word args.

    More about *args: https://www.geeksforgeeks.org/args-kwargs-python/
"""


# Python program to illustrate *args for a variable
def myFun(*args):
    for arg in args:
        print(arg)


myFun("Hello", "Yash", "How are you!")


# with first extra arguments
def myArgs(arg, *args):
    print("First argument: ", arg)
    count = 1
    for i in args:
        print(f"This is argument No.{count}: {i}")
        count = count + 1


myArgs("Hello", "How are you!", "Yash", 55)


# calculating total of given integer arguments
def total_Number(*args):
    total = 0
    for i in args:
        total += i
    return total


print("Total of every number is: ", total_Number(10, 20, 30, 40))
