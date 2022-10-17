"""
Exercise: Classes and object exploration
In this reading, you will explore the behaviour of functions, objects and classes in Python and how the flow of execution of different program statements works to enable better understanding.

You will perform minor modifications in the given code to observe how it changes the output.

First, set up a file called class_explore.py that contains the following piece of code. Alternatively, you can use the interactive environment here.

"""


class A:
    def __init__(self, c):
        print("---------Inside class A----------")
        self.c = c

    print("Print inside A.")

    def alpha(self):
        c = self.c + 1
        return c


# print(dir(A))
print("Instantiating A..")
a = A(1)
print(a.alpha())


class B:
    def __init__(self, a):
        print("---------Inside class B----------")
        self.a = a

    print(a.alpha())
    d = 5
    print(d)
    print(a)


print("\n\nInstantiating B..")
b = B(a)
print(a)
